def solve(numheads, numlegs):
    # Пусть x — количество кур, y — количество кроликов
    # У нас есть две формулы:
    # x + y = numheads (общее количество голов)
    # 2x + 4y = numlegs (общее количество ног)
    
    # Из первого уравнения: x = numheads - y
    # Подставляем в второе уравнение:
    # 2(numheads - y) + 4y = numlegs
    # Упростим уравнение:
    # 2 * numheads - 2y + 4y = numlegs
    # 2 * numheads + 2y = numlegs
    # 2y = numlegs - 2 * numheads
    # y = (numlegs - 2 * numheads) / 2
    
    y = (numlegs - 2 * numheads) // 2  # Количество кроликов
    x = numheads - y  # Количество кур
    
    return x, y


numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)

print(f"Chickens: {chickens}, Rabbits: {rabbits}")
