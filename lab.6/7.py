import pygame

pygame.init()

W, H = 500,500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Hamster Clicker")

clock = pygame.time.Clock()

hamster_radius=40                 
hamster_x = W// 2                    
hamster_y = H// 2  

score=0

font = pygame.font. SysFont=(None,40)

running=True
while running :
    screen.fill(255,255,255)
    pygame.draw.circle(screen, (200, 150, 100), (hamster_x, hamster_y), hamster_radius)

    text = font.render(f"Hamster Coins: {score}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

      
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if (mx - hamster_x) == 2:
                score+=1

            if score == 5:
                hamster_radius *= 2




            # if score==10:


