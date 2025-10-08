from datetime import datetime

# Определяем две даты
date_1 = datetime(2025, 10, 8, 12, 0, 0)  # Первая дата
date_2 = datetime(2025, 10, 9, 15, 30, 0)  # Вторая дата

# Вычисляем разницу между датами
time_difference = date_2 - date_1

# Конвертируем разницу в секунды
difference_in_seconds = time_difference.total_seconds()

# Выводим результат
print(f"Разница между датами в секундах: {difference_in_seconds} секунд")
