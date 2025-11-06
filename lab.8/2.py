import pygame
from random import randrange
pygame.init()

RES= 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0,RES, SIZE)
apple = randrange(0, RES,SIZE), randrange(0, RES, SIZE)
dirs = {"W": True, "A": True, "S": True, "D": True,}
length = 1
snake = [(x,y)]
dx, dy = 0, 0
score = 0
fps = 5
level = 1

screen = pygame.display.set_mode([RES,RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold = True)
font_end = pygame.font.SysFont("Arial", 66, bold = True)
font_level = pygame.font.SysFont("Arial", 26, bold = True)

while True:
    screen.fill(pygame.Color("black"))
    #drawing snake, apple
    [(pygame.draw.rect(screen, pygame.Color("green"),(i, j, SIZE - 2, SIZE-2))) for i,j in snake]
    pygame.draw.rect(screen,pygame.Color('red'),(*apple, SIZE, SIZE))
    #show score and level
    render_score = font_score.render(f"SCORE: {score}", 1, pygame.Color('orange'))
    screen.blit(render_score, (5,5))
    render_level  = font_level.render(f"LEVEL: {level}", 1, pygame.Color('orange'))
    screen.blit(render_level,(5, 30))
    #snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x,y))
    snake = snake[-length:]
    #eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES,SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        if score % 4 == 0:
            level += 1
            fps += 1
    #game over
    if x < 0 or x > RES - SIZE or y > RES - SIZE:
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs["W"]:
        dx, dy = 0, -1
        dirs = {"W": True, "A": True, "S": False, "D": True,}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {"W": True, "A": True, "S": True, "D": False,}
    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W": True, "A": False, "S": True, "D": True,}
    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W": False, "A": True, "S": True, "D": True,}