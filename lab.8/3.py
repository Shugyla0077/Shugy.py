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
    tool = 'brush'  # brush, rectangle, circle, eraser
    points = []
    drawing = False
    start_pos = (0, 0)
    
    colors = {
        'red':   (255, 0, 0),
        'green': (0, 255, 0),
        'blue':  (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
    }
    
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((255, 255, 255))  # белый фон
    
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
                    # Инструменты
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка
                    drawing = True
                    start_pos = event.pos
                    if tool in ['brush', 'eraser']:
                        points = [start_pos]
                elif event.button == 3:  # правая кнопка уменьшает кисть
                    brush_radius = max(1, brush_radius - 1)
                elif event.button == 4:  # колёсико вверх — увеличить кисть
                    brush_radius = min(100, brush_radius + 1)
                elif event.button == 5:  # колёсико вниз — уменьшить кисть
                    brush_radius = max(1, brush_radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    color = colors[mode]
                    if tool == 'rectangle':
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(background, color, rect, shape_thickness)
                    elif tool == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_c = int(math.hypot(dx, dy))
                        pygame.draw.circle(background, color, start_pos, radius_c, shape_thickness)
                    drawing = False
                    points = []

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['brush', 'eraser']:
                    pos = event.pos
                    # рисуем линию на фоне, чтобы мазок оставался
                    if points:
                        col = colors[mode] if tool == 'brush' else (255, 255, 255)
                        pygame.draw.line(background, col, points[-1], pos, max(1, brush_radius*2))
                    points.append(pos)
                    points = points[-256:]
        
        # Отрисовка 
        screen.blit(background, (0, 0))
        color_value = colors[mode]
        
        # Превью кисти/ластика в реальном времени (в момент рисования)
        if drawing and tool in ['brush', 'eraser'] and len(points) >= 2:
            draw_lines(screen, points, max(1, brush_radius*2), color_value if tool == 'brush' else (255, 255, 255))
        
        # Превью прямоугольника и круга
        if drawing and tool in ['rectangle', 'circle']:
            current_pos = pygame.mouse.get_pos()
            preview_color = colors[mode]
            if tool == 'rectangle':
                x1, y1 = start_pos
                x2, y2 = current_pos
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                radius_c = int(math.hypot(dx, dy))
                pygame.draw.circle(screen, preview_color, start_pos, radius_c, shape_thickness)
        
        pygame.display.flip()
        clock.tick(60)

def draw_lines(screen, points, width, color):
    # рисуем сегменты между соседними точками
    for i in range(len(points)-1):
        pygame.draw.line(screen, color, points[i], points[i+1], width)

main()