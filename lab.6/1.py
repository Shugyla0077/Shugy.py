import pygame, random
pygame.init()

# ------------------------------
#  Экран параметрлері
# ------------------------------
W, H = 600, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Fruit Catch")
clock = pygame.time.Clock()

# ------------------------------
#  Бастапқы объектілер
# ------------------------------
basket_x = 250                 # корзинаның X координатасы
fruit_x = random.randint(0, 580)  # жемістің X позициясы (рандом)
fruit_y = -20                     # жеміс экраннан жоғарыда басталады
fruit_speed = 5                   # жемістің түсу жылдамдығы

score = 0                         # жиналған ұпай
game_over = False                # ойын бітті ме?

font = pygame.font.SysFont(None, 40)  # мәтін шрифті

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:     # терезені жабу
            running = False

        # ------------------------------
        #  Game Over режиміндегі басқару
        # ------------------------------
        if game_over:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    # ---- ОЙЫНДЫ ҚАЙТА БАСТАУ ----
                    basket_x = 250
                    fruit_x = random.randint(0, 580)
                    fruit_y = -20
                    score = 0
                    game_over = False

                if e.key == pygame.K_q:
                    running = False   # шығу

    # --------------------------------------
    #  НЕГІЗГІ ОЙЫН ЛОГИКАСЫ (game_over == False)
    # --------------------------------------
    if not game_over:

        # ------------------------------
        #  Корзинаны басқару
        # ------------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= 7
        if keys[pygame.K_RIGHT] and basket_x < W - 80:
            basket_x += 7

        # ------------------------------
        #  Жемістің түсуі
        # ------------------------------
        fruit_y += fruit_speed

        # ------------------------------
        #  Егер жеміс жерге тисе → Game Over
        # ------------------------------
        if fruit_y > H:
            game_over = True

        # ------------------------------
        #  Коллизияны тексеру (ұстау)
        # ------------------------------
        basket_rect = pygame.Rect(basket_x, 550, 80, 20)    # корзина тік төртбұрыш
        fruit_rect = pygame.Rect(fruit_x, fruit_y, 20, 20)  # жемістің тік төртбұрыш

        if basket_rect.colliderect(fruit_rect):
            score += 1          # ұпай қосылады
            fruit_y = -20       # жеміс қайта жоғардан басталады
            fruit_x = random.randint(0, 580)

        # ------------------------------
        #  Экранды салу
        # ------------------------------
        screen.fill((255, 255, 255))

        # корзина
        pygame.draw.rect(screen, (0, 0, 255), (basket_x, 550, 80, 20))

        # жеміс
        pygame.draw.circle(screen, (255, 0, 0), (fruit_x, fruit_y), 10)

        # ұпай
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(score_text, (10, 10))

    # --------------------------------------
    #  GAME OVER ЭКРАНЫ
    # --------------------------------------
    else:
        screen.fill((0, 0, 0))

        over = font.render("GAME OVER", True, (255, 0, 0))
        scr  = font.render(f"Your Score: {score}", True, (255, 255, 255))
        hint = font.render("Press R to Restart | Q to Quit", True, (255, 255, 255))

        # мәтінді экран ортасына шығару
        screen.blit(over, (W//2 - over.get_width()//2, 220))
        screen.blit(scr, (W//2 - scr.get_width()//2, 280))
        screen.blit(hint, (W//2 - hint.get_width()//2, 340))

    # ------------------------------
    #  Экранды жаңарту
    # ------------------------------
    pygame.display.update()
    clock.tick(60)

pygame.quit()
###
import pygame
import random

pygame.init()

# ------------------------------
# Экран параметрлері
# ------------------------------
W, H = 600, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

# ------------------------------
# Бастапқы объектілер
# ------------------------------
paddle_x = 250
paddle_y = 550
paddle_width = 100
paddle_height = 20
paddle_speed = 7

ball_x = 300
ball_y = 530
ball_radius = 10
ball_dx = 4
ball_dy = -4

score = 0
game_over = False

# Блоктар (көптеген блоктарды экранға қойып, олардың түрін таңдаймыз)
block_width = 60
block_height = 20
blocks = []

for row in range(5):
    for col in range(10):
        block_x = col * (block_width + 10) + 35
        block_y = row * (block_height + 5) + 30
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# Шрифт
font = pygame.font.SysFont(None, 40)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # ------------------------------
    # Ойын логикасы (game_over == False)
    # ------------------------------
    if not game_over:
        # ------------------------------
        # Платформаны басқару
        # ------------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < W - paddle_width:
            paddle_x += paddle_speed

        # ------------------------------
        # Допты жылжыту
        # ------------------------------
        ball_x += ball_dx
        ball_y += ball_dy

        # Доптың экраннан шықпауын тексеру
        if ball_x <= 0 or ball_x >= W - ball_radius:
            ball_dx *= -1
        if ball_y <= 0:
            ball_dy *= -1
        if ball_y >= H - ball_radius:
            if paddle_x <= ball_x <= paddle_x + paddle_width:
                ball_dy *= -1
                score += 1
            else:
                game_over = True

        # ------------------------------
        # Блоктарды бұзу
        # ------------------------------
        ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
        for block in blocks[:]:
            if ball_rect.colliderect(block):
                ball_dy *= -1
                blocks.remove(block)
                score += 10

        # ------------------------------
        # Экранды салу
        # ------------------------------
        screen.fill((0, 0, 0))

        # Платформа
        pygame.draw.rect(screen, (0, 0, 255), (paddle_x, paddle_y, paddle_width, paddle_height))

        # Доп
        pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius)

        # Блоктар
        for block in blocks:
            pygame.draw.rect(screen, (255, 0, 0), block)

        # Ұпай
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    # ------------------------------
    # GAME OVER экран
    # ------------------------------
    else:
        screen.fill((0, 0, 0))

        over = font.render("GAME OVER", True, (255, 0, 0))
        scr = font.render(f"Your Score: {score}", True, (255, 255, 255))
        hint = font.render("Press R to Restart | Q to Quit", True, (255, 255, 255))

        screen.blit(over, (W//2 - over.get_width()//2, 220))
        screen.blit(scr, (W//2 - scr.get_width()//2, 280))
        screen.blit(hint, (W//2 - hint.get_width()//2, 340))

    # Экранды жаңарту
    pygame.display.update()
    clock.tick(60)

pygame.quit()
###