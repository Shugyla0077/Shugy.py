def average_imdb(movies):
    """Вычисляет среднюю IMDB оценку для списка фильмов"""
    total_imdb = sum(movie["imdb"] for movie in movies)  # Суммируем все IMDb оценки
    return total_imdb / len(movies) if movies else 0  # Возвращаем среднее значение

# Пример использования:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "The Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Room", "imdb": 3.7, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"}
]

average_score = average_imdb(movies)
print(f"Average IMDb score: {average_score}")
