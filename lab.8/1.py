import pygame, sys, random, time
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# --- Константы ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Начальная скорость врагов
SCORE = 0
COINS = 0
FPS = 60

# --- Цвета ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# --- Шрифт ---
font = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# --- Окно ---
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# --- Звук ---
pygame.mixer.music.load("Shugy.py/lab.8/sounds/background.wav")
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound("Shugy.py/lab.8/sounds/crash.wav")

# --- Фон ---
background = pygame.image.load("Shugy.py/lab.8/images/AnimatedStreet.png")

# --- Игрок ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Shugy.py/lab.8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (165, 524)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

# --- Враг ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Shugy.py/lab.8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SPEED
        self.rect.y += SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# --- Монеты ---
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = random.randint(15, 30)  
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (self.size // 2, self.size // 2), self.size // 2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-1500, -100))

    def move(self):
        self.rect.y += SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = random.randint(-1500, -100)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

# --- Объекты игры ---
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, coin)

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

# --- Событие увеличения скорости ---
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

# --- Игровой цикл ---
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Отрисовка фона
    DISPLAYSURF.blit(background, (0, 0))

    # Движение и отрисовка всех объектов
    player.move()
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Обработка столкновений
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        pygame.mixer.music.stop()
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (150, 250))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Сбор монет
    collected_coins = pygame.sprite.spritecollide(player, coins, False)
    for collected in collected_coins:
        COINS += 1
        collected.rect.top = random.randint(-1500, -100)
        collected.rect.center = (random.randint(40, SCREEN_WIDTH - 40), collected.rect.top)

    # Увеличение скорости врагов после 5 монет
    if COINS >= 5:
        SPEED += 1
        COINS = 0  # Сбросить количество монет

    # Отображение счёта
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)
