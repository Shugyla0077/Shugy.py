import pygame
pygame.init()

W = 800
H= 800
win = pygame.display.set_mode((W, H))

size = 50
x = W//2
y = H//2
speed = 5

font = pygame.font.SysFont(None, 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                x = W//2
                y = H//2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_b]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_d]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x + size > W:
        x = W - size
    if y + size > H:
        y = H - size

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, size, size))
    text = font.render("x-" + str(x) + ", y-" + str(y), True, (255, 255, 255))
    win.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()