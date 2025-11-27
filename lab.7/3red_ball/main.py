import pygame
pygame.init()

clock = pygame.time.Clock()

W, H = 550, 350
ball_r = 25  
ball_x = W / 2
ball_y = H / 2
margin = 0
circle_color = (255, 0, 0)

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
        if ball_x + ball_r > W - margin:
            ball_x = W - ball_r - margin

    
    if keys[pygame.K_LEFT]:
        ball_x -= 10
        if ball_x - ball_r < margin:
            ball_x = ball_r + margin

    
    if keys[pygame.K_DOWN]:
        ball_y += 10
        if ball_y + ball_r > H - margin:
            ball_y = H - ball_r - margin

    
    if keys[pygame.K_UP]:
        ball_y -= 10
        if ball_y - ball_r <= margin:
            ball_y = ball_r

    if keys[pygame.K_SPACE]:
        if circle_color == (255, 0,0):
            circle_color = (0,0,255)
        else:
            circle_color = (255,0,0)


    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle_color, (int(ball_x), int(ball_y)), ball_r)
    pygame.display.update()

pygame.quit()
