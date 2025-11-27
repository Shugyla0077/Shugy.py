import pygame
import random
pygame.init()

# --- Окно ---
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Поймай треугольники")

# --- Параметры платформы (игрока) ---
platform_width = 120                 # ширина платформы
platform_height = 20                 # высота платформы
platform_x = WIDTH // 2 - platform_width // 2   # начальная позиция (по центру)
platform_y = HEIGHT - 40             # расположение внизу экрана
platform_speed = 6                   # скорость передвижения платформы

# --- Падающие треугольники ---
triangles = []                       # список всех треугольников
triangle_speed = 4                   # скорость падения треугольников
spawn_delay = 40                     # каждые 40 кадров появляется новый треугольник

# --- Счёт ---
score = 0
font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()
running = True
frame = 0

while running:
    clock.tick(60)                   # ограничение FPS = 60
    frame += 1                       # счётчик кадров

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Управление платформой ---
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and platform_x > 0:
        platform_x -= platform_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and platform_x < WIDTH - platform_width:
        platform_x += platform_speed

    # --- Создание новых треугольников ---
    # каждые 40 кадров создаём новый треугольник в случайном месте
    if frame % spawn_delay == 0:
        new_x = random.randint(20, WIDTH - 20)
        triangles.append({"x": new_x, "y": -20})  # начальная позиция сверху

    # --- Движение треугольников и проверка столкновений ---
    for t in triangles[:]:           # используем копию списка
        t["y"] += triangle_speed     # треугольник падает вниз

        # если треугольник вышел за нижнюю границу — удаляем
        if t["y"] > HEIGHT:
            triangles.remove(t)
            continue

        # проверка: поймала ли платформа треугольник
        if (platform_y <= t["y"] + 20 <= platform_y + platform_height) and \
           (platform_x <= t["x"] <= platform_x + platform_width):

            score += random.randint(1, 3)  # добавляем случайные очки (от 1 до 3)
            triangles.remove(t)            # удаляем пойманный треугольник

    # --- Отрисовка ---
    win.fill((20, 20, 20))          # фон

    # Рисуем платформу
    pygame.draw.rect(win, (0, 150, 250),
                     (platform_x, platform_y, platform_width, platform_height))

    # Рисуем падающие треугольники
    for t in triangles:
        points = [
            (t["x"], t["y"]),           # верхняя точка
            (t["x"] - 15, t["y"] + 30), # левая нижняя точка
            (t["x"] + 15, t["y"] + 30)  # правая нижняя точка
        ]
        pygame.draw.polygon(win, (255, 200, 0), points)

    # Рисуем текст со счётом
    text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()
