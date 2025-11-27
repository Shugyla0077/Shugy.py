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

   
    if not game_over:
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < W - paddle_width:
            paddle_x += paddle_speed

       
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
