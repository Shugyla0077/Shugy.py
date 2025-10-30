import pygame

pygame.init()

w, h = 664, 360
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Двигающийся мяч")

ball_color = (255, 0, 0)
bg_color = (255, 255, 255)

ball_x, ball_y = w // 2, h // 2
ball_radius = 25
ball_speed = 20

running = True
while running:
    screen.fill(bg_color)

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius > 0:
                ball_y -= ball_speed
            if event.key == pygame.K_DOWN and ball_y + ball_radius < h:
                ball_y += ball_speed
            if event.key == pygame.K_LEFT and ball_x - ball_radius > 0:
                ball_x -= ball_speed
            if event.key == pygame.K_RIGHT and ball_x + ball_radius < w:
                ball_x += ball_speed

    pygame.display.update()
