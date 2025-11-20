import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # Настройки
    brush_radius = 5
    shape_thickness = 3
    mode = 'blue'
    tool = 'brush'  # 'brush', 'rectangle', 'circle', 'eraser', новые фигуры
    points = []
    drawing = False
    start_pos = (0, 0)

    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255)
    }

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return

                # Цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:
                    mode = 'black'
                elif event.key == pygame.K_w:
                    mode = 'white'

                # Инструменты (с добавлением новых фигур)
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                elif event.key == pygame.K_5:
                    tool = 'square'
                elif event.key == pygame.K_6:
                    tool = 'right_triangle'
                elif event.key == pygame.K_7:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_8:
                    tool = 'rhombus'

            # Мышь
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool in ['brush', 'eraser']:
                        points.append(start_pos)
                elif event.button == 3:
                    brush_radius = max(1, brush_radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    color = colors[mode]

                    # Существующие фигуры
                    if tool == 'rectangle':
                        rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.rect(background, color, rect, shape_thickness)
                    elif tool == 'circle':
                        radius_c = int(math.hypot(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.circle(background, color, start_pos, radius_c, shape_thickness)

                    # Новые фигуры
                    elif tool == 'square':
                        # Определяем сторону квадрата как max(dx, dy)
                        side = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        rect = pygame.Rect(start_pos, (side if end_pos[0] >= start_pos[0] else -side,
                                                       side if end_pos[1] >= start_pos[1] else -side))
                        pygame.draw.rect(background, color, rect, shape_thickness)

                    elif tool == 'right_triangle':
                        # Прямоугольный треугольник с вершинами start_pos, (end_x, start_y), end_pos
                        triangle_points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
                        pygame.draw.polygon(background, color, triangle_points, shape_thickness)

                    elif tool == 'equilateral_triangle':
                        # Равносторонний треугольник, основание горизонтальное
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        height = abs(dx) * math.sqrt(3)/2
                        if dy < 0:
                            height = -height
                        triangle_points = [start_pos, (start_pos[0]+dx, start_pos[1]), (start_pos[0]+dx/2, start_pos[1]+height)]
                        pygame.draw.polygon(background, color, triangle_points, shape_thickness)

                    elif tool == 'rhombus':
                        # Ромб с диагоналями по горизонтали и вертикали
                        dx = end_pos[0]-start_pos[0]
                        dy = end_pos[1]-start_pos[1]
                        rhombus_points = [
                            (start_pos[0], start_pos[1]-dy//2),
                            (start_pos[0]+dx//2, start_pos[1]),
                            (start_pos[0], start_pos[1]+dy//2),
                            (start_pos[0]-dx//2, start_pos[1])
                        ]
                        pygame.draw.polygon(background, color, rhombus_points, shape_thickness)

                    drawing = False
                    points = []

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['brush', 'eraser']:
                    pos = event.pos
                    points.append(pos)
                    points = points[-256:]

        screen.blit(background, (0, 0))
        color_value = colors[mode]

        if tool in ['brush', 'eraser']:
            draw_lines(screen, points, brush_radius, color_value if tool == 'brush' else (255, 255, 255))

        # Превью прямоугольника, круга и новых фигур
        if drawing and tool in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
            current_pos = pygame.mouse.get_pos()
            preview_color = colors[mode]
            if tool == 'rectangle':
                rect = pygame.Rect(start_pos, (current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'circle':
                radius_c = int(math.hypot(current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                pygame.draw.circle(screen, preview_color, start_pos, radius_c, shape_thickness)
            elif tool == 'square':
                side = max(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                rect = pygame.Rect(start_pos, (side if current_pos[0] >= start_pos[0] else -side,
                                               side if current_pos[1] >= start_pos[1] else -side))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'right_triangle':
                triangle_points = [start_pos, (current_pos[0], start_pos[1]), current_pos]
                pygame.draw.polygon(screen, preview_color, triangle_points, shape_thickness)
            elif tool == 'equilateral_triangle':
                dx = current_pos[0] - start_pos[0]
                height = abs(dx) * math.sqrt(3)/2
                if current_pos[1] < start_pos[1]:
                    height = -height
                triangle_points = [start_pos, (start_pos[0]+dx, start_pos[1]), (start_pos[0]+dx/2, start_pos[1]+height)]
                pygame.draw.polygon(screen, preview_color, triangle_points, shape_thickness)
            elif tool == 'rhombus':
                dx = current_pos[0]-start_pos[0]
                dy = current_pos[1]-start_pos[1]
                rhombus_points = [
                    (start_pos[0], start_pos[1]-dy//2),
                    (start_pos[0]+dx//2, start_pos[1]),
                    (start_pos[0], start_pos[1]+dy//2),
                    (start_pos[0]-dx//2, start_pos[1])
                ]
                pygame.draw.polygon(screen, preview_color, rhombus_points, shape_thickness)

        pygame.display.flip()
        clock.tick(60)

def draw_lines(screen, points, width, color):
    for i in range(len(points)-1):
        pygame.draw.line(screen, color, points[i], points[i+1], width)

def new_func(main):
    main()

new_func(main)