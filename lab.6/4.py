import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Collector")

# Игрок
player_x, player_y = WIDTH//2, HEIGHT//2
player_size = 30
speed = 5

# Круг
circle_x = random.randint(20, WIDTH-20)
circle_y = random.randint(20, HEIGHT-20)
circle_r = 12

# Счёт
score = 0
font = pygame.font.SysFont(None, 40)

run = True
while run:
    pygame.time.delay(15)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += speed

    # Границы окна
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # Проверка столкновения с кругом
    dist = math.sqrt((player_x + player_size//2 - circle_x)**2 + (player_y + player_size//2 - circle_y)**2)
    if dist < player_size//2 + circle_r:
        score += random.randint(1, 5)
        circle_x = random.randint(20, WIDTH-20)
        circle_y = random.randint(20, HEIGHT-20)

    # Рисование
    win.fill((0, 0, 0))
    pygame.draw.polygon(win, (0,200,255), [
        (player_x + player_size//2, player_y),
        (player_x, player_y + player_size),
        (player_x + player_size, player_y + player_size)
    ])
    pygame.draw.circle(win, (255,50,50), (circle_x, circle_y), circle_r)
    win.blit(font.render(f"Score: {score}", True, (255,255,255)), (20,20))

    pygame.display.update()

pygame.quit()
