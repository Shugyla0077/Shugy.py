import pygame
import random
import sys
import time

# Инициализация Pygame 
pygame.init()

# Цвета 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 0)  # Дополнительный цвет для "тяжёлой еды"

# Размеры экрана 
dis_width = 800
dis_height = 600

# Настройки змейки 
snake_block = 10 # размер одного блока змейки
initial_speed = 15

# Создание окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Шрифт для текста 
font_style = pygame.font.SysFont("bahnschrift", 25)

# Функция отображения счёта и уровня 
def show_score_level(score, level):
    """Показывает текущий счет и уровень игрока"""
    score_text = font_style.render("Score: " + str(score), True, WHITE)
    level_text = font_style.render("Level: " + str(level), True, WHITE)
    dis.blit(score_text, [0, 0])
    dis.blit(level_text, [0, 30])

# Функция отрисовки змейки
def draw_snake(snake_list):
    """Рисует все сегменты змейки"""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

# Функция генерации еды с разным весом и таймером
def generate_food(snake_list):
    """
    Генерирует еду:
    - Разные веса: обычная (1 очко, синий), тяжелая (3 очка, желтая)
    - Время жизни еды (таймер)
    """
    while True:
        x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        if [x, y] not in snake_list:
            # Рандомный вес еды
            if random.random() < 0.2:  # 20% шанс на тяжелую еду
                weight = 3
                color = YELLOW
            else:
                weight = 1
                color = BLUE
            # Время жизни еды: 5–10 секунд
            lifetime = random.randint(5, 10)
            spawn_time = time.time()
            return {"x": x, "y": y, "weight": weight, "color": color, "lifetime": lifetime, "spawn_time": spawn_time}

# Основной игровой цикл 
def gameLoop():
    # Начальные настройки
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Начальная еда
    food = generate_food(snake_List)

    # Счёт и уровень
    score = 0
    level = 1
    foods_eaten = 0
    snake_speed = initial_speed

    while not game_over:

        # Окно "Game Over"
        while game_close:
            dis.fill(BLACK)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            show_score_level(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка выхода за границы
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Перемещение змейки
        x1 += x1_change
        y1 += y1_change

        dis.fill(BLACK)

        # Проверка времени жизни еды
        if time.time() - food["spawn_time"] > food["lifetime"]:
            food = generate_food(snake_List)  # создаем новую еду

        # Отрисовка еды
        pygame.draw.rect(dis, food["color"], [food["x"], food["y"], snake_block, snake_block])

        # Обновление тела змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка столкновения с самим собой
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        draw_snake(snake_List)
        show_score_level(score, level)
        pygame.display.update()

        # Проверка поедания еды
        if x1 == food["x"] and y1 == food["y"]:
            Length_of_snake += 1
            score += food["weight"]  # прибавляем очки в зависимости от веса еды
            foods_eaten += 1
            food = generate_food(snake_List)

            # Повышение уровня каждые 3 еды
            if foods_eaten % 3 == 0:
                level += 1
                snake_speed += 2

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

# Запуск игры 
gameLoop()