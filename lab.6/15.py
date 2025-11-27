import pygame
import datetime
pygame.init ()

W,H=800,800
x=W//2
y=H//2
WHITE=(255,255,255)
sc=pygame.display.set_mode((W,H))

mickey=pygame.image.load("Shugy.py/lab.7/clock/images/main-clock.png")
lefthand=pygame.image.load("Shugy.py/lab.7/clock/images/left-hand.png")
righthand=pygame.image.load("Shugy.py/lab.7/clock/images/right-hand.png")

mickeyRect=mickey.get_rect()

def blitRotateCenter(surf,image,center,angle):
    rotated_image=pygame.transform.rotate(image.angle)
    new_rect=rotated_image.get_rect(center=image.get.rect(center=center).center)
    surf.blit(rotated_image,new_rect)


While True:
   for event in pygame.event.get():
     if event.type==pygame.QUIT:
        exit()

t = datetime.datetime.now()  
minute = int(t.strftime('%M'))*6 -90
second = int(t.strftime('%S'))*6 -90

sc.fill(WHITE)
sc.blit(mickey, (x, y))
sc.blit(mickey, mickeyRect)

blitRotateCenter(sc, leftHand, (x,y), -second) 
blitRotateCenter(sc, rightHand, (x,y), -minute)
pygame.display.update()
