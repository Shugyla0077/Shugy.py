import pygame
pygame.init()

clock = pygame.time.Clock()

W, H = 564, 360
ball_r = 25  
ball_x = W / 2
ball_y = H / 2

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Red Ball")

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_RIGHT]:
        ball_x += 10
        if ball_x + ball_r > W:     
            ball_x = W - ball_r    
    
    if keys[pygame.K_LEFT]:
        ball_x -= 10
        if ball_x - ball_r < 0:
            ball_x = ball_r
    
    if keys[pygame.K_DOWN]:
        ball_y += 10
        if ball_y + ball_r > H:
            ball_y = H - ball_r
    
    if keys[pygame.K_UP]:
        ball_y -= 10
        if ball_y - ball_r < 0:
            ball_y = ball_r

    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(ball_x), int(ball_y)), ball_r)
    pygame.display.update()

pygame.quit()
