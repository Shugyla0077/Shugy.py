import pygame
import random

pygame.init()
cell = 24
gw, gh = 22, 18
w, h = gw*cell, gh*cell
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake simple")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

walls = set()
for x in range(gw):
    walls.add((x, 0)); walls.add((x, gh-1))
for y in range(gh):
    walls.add((0, y)); walls.add((gw-1, y))

def draw_cell(xy, col):
    x, y = xy
    pygame.draw.rect(screen, col, (x*cell, y*cell, cell, cell))

def empty_cell(snake):
    bad = set(snake) | walls
    free = [(x,y) for x in range(gw) for y in range(gh) if (x,y) not in bad]
    return random.choice(free)

snake = [(5,5),(4,5),(3,5)]
dir_now = (1,0)
dir_next = (1,0)
food = empty_cell(snake)
score = 0
eaten = 0
level = 1
running = True

while running:
    clock.tick(8 + (level-1)*2)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
            if e.key == pygame.K_UP and dir_now!=(0,1): dir_next=(0,-1)
            if e.key == pygame.K_DOWN and dir_now!=(0,-1): dir_next=(0,1)
            if e.key == pygame.K_LEFT and dir_now!=(1,0): dir_next=(-1,0)
            if e.key == pygame.K_RIGHT and dir_now!=(-1,0): dir_next=(1,0)

    dir_now = dir_next
    head = (snake[0][0]+dir_now[0], snake[0][1]+dir_now[1])
    if not (0<=head[0]<gw and 0<=head[1]<gh): break
    if head in walls or head in snake: break

    snake.insert(0, head)
    if head == food:
        score += 10
        eaten += 1
        if eaten % 4 == 0: level += 1
        food = empty_cell(snake)
    else:
        snake.pop()

    screen.fill((18,18,18))
    for wpos in walls: draw_cell(wpos, (60,60,60))
    for i, s in enumerate(snake):
        draw_cell(s, (0,200,0) if i==0 else (0,130,0))
    draw_cell(food, (200,0,0))
    hud = font.render(f"Score:{score}  Level:{level}", True, (255,215,0))
    screen.blit(hud, (10, 8))
    pygame.display.flip()

screen.fill((0,0,0))

end = font.render(f"GAME OVER  Score:{score}  Level:{level}", True, (255,255,255))
screen.blit(end, end.get_rect(center=(w//2, h//2)))
pygame.display.flip()
pygame.time.wait(1500)
pygame.quit()