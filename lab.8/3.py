import pygame
pygame.init()

#Display settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))

mouse = True

# Class for drawing
class drawing(object):
 
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6
         
    # Drawing Function
    def draw(self, win, pos):
        if mouse:
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        elif not mouse:
            pygame.draw.rect(win,self.color,(pos[0],pos[1],50,50))
            
        if self.color == (255, 255, 255):
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), 20)
        
        pygame.draw.rect(win, (0, 0, 0), (0, 0, WIDTH-100, HEIGHT),5)
 
    # detecting clicks
    def click(self, win, list):
        global mouse
        pos = pygame.mouse.get_pos()
 
        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 400:
            if pos[1] > 25:
                self.draw(win, pos)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            for button in list:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        self.color = button.color2
                if pos[0] > 407 and pos[0] < 407 + 40:
                    if pos[1] > 214 and pos[1] < 214 + 40:
                        mouse = False
                if pos[0] > 453 and pos[0] < 453 + 40:
                    if pos[1] > 214 and pos[1] < 214 + 40:
                        mouse = True
                        


class button(object):
 
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text

    def draw(self, win):
 
        pygame.draw.rect(win, self.color, (self.x, self.y,self.width, self.height), self.outline)
        pygame.draw.rect(win, (255, 255, 255), (410, 446, 80, 35))

def draw(win):
    drawing1.click(win, Buttons_color)
 

    for button in Buttons_color:
        button.draw(win)
 
    pygame.display.update()

drawing1 = drawing()

#Colored buttons
redButton = button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0))
blueButton = button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255))
greenButton = button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0))
orangeButton = button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0))
yellowButton = button(407, 122, 40, 40, (255, 255, 0), (255, 255, 0))
purpleButton = button(453, 122, 40, 40, (112, 48, 160), (112, 48, 160))
blackButton = button(407, 168, 40, 40, (0, 0, 0), (0, 0, 0))
whiteButton = button(453, 168, 40, 40, (0, 0, 0), (255, 255, 255), 1)
rectangleButton = button(407, 214, 40, 40, (0,0,0), (0,0,0))

Buttons_color = [blueButton, redButton, greenButton, orangeButton,
                 yellowButton, purpleButton, blackButton, whiteButton,rectangleButton]

running = True
while running:
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    pygame.draw.circle(screen, (0,0,0), (476, 237), 20)

    draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()