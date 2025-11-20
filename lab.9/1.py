# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Other variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Count of collected coins

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Load background
background = pygame.image.load(
    "/Users/sugylazambybaj/Desktop/Shugy.py/lab.9/images/AnimatedStreet.png"
)

# Create display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game")

# Audio setup 
pygame.mixer.init()
pygame.mixer.music.load('/Users/sugylazambybaj/Desktop/Shugy.py/lab.9/sounds/background.wav')
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound('/Users/sugylazambybaj/Desktop/Shugy.py/lab.9/sounds/crash.wav')

# Player class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "/Users/sugylazambybaj/Desktop/Shugy.py/lab.9/images/Player.png"
        )
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "/Users/sugylazambybaj/Desktop/Shugy.py/lab.9/images/Enemy.png"
        )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class (updated)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])  # Вес монеты: 1, 2 или 3
        self.image = pygame.Surface((30, 30))
        # Цвет зависит от веса монеты (чтобы визуально отличать)
        if self.weight == 1:
            self.image.fill((255, 255, 0))  # Желтый
        elif self.weight == 2:
            self.image.fill((255, 165, 0))  # Оранжевый
        else:
            self.image.fill((255, 215, 0))  # Золотой

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-1500, -100))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            # Сбросить монету с новым весом и позицией
            self.weight = random.choice([1, 2, 3])
            if self.weight == 1:
                self.image.fill((255, 255, 0))
            elif self.weight == 2:
                self.image.fill((255, 165, 0))
            else:
                self.image.fill((255, 215, 0))

            self.rect.top = random.randint(-1500, -100)
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), self.rect.top)

# Creating sprites
P1 = Player()
E1 = Enemy()

# Создадим несколько монет для разнообразия (5 монет)
coins = pygame.sprite.Group()
for _ in range(5):
    coins.add(Coin())

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)  # Добавляем все монеты в группу

# Event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Константа для увеличения скорости при сборе монет
COINS_TO_INCREASE_SPEED = 10

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Display score and coins
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.mixer.music.stop()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        final_score_text = font_small.render(f"Final Score: {SCORE}, Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_score_text, (50, 320))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Collision with coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        COINS += coin.weight  # Добавляем вес монеты к общему количеству монет
        # Перезапускаем монету (новый вес и позиция)
        coin.weight = random.choice([1, 2, 3])
        if coin.weight == 1:
            coin.image.fill((255, 255, 0))
        elif coin.weight == 2:
            coin.image.fill((255, 165, 0))
        else:
            coin.image.fill((255, 215, 0))
        coin.rect.top = random.randint(-1500, -100)
        coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), coin.rect.top)

    # Увеличиваем скорость врага, если собрал достаточно монет
    if COINS >= COINS_TO_INCREASE_SPEED:
        SPEED += 1
        COINS = 0  # Сбрасываем счётчик монет, чтобы не накапливалась бесконечно

    pygame.display.update()
    FramePerSec.tick(FPS)