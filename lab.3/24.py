def average_imdb_by_category(movies, category_name):
    """Вычисляет среднюю IMDB оценку для фильмов в указанной категории"""
    # Фильтруем фильмы по категории
    filtered_movies = [movie for movie in movies if movie["category"].lower() == category_name.lower()]
    
    # Проверяем, что фильмы в категории существуют
    if not filtered_movies:
        return 0  # Если фильмов в категории нет, возвращаем 0
    
    # Вычисляем среднее значение IMDB
    total_imdb = sum(movie["imdb"] for movie in filtered_movies)
    return total_imdb / len(filtered_movies)

# Пример использования:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "The Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Room", "imdb": 3.7, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Joker", "imdb": 8.4, "category": "Drama"}
]

# Запросим среднюю IMDB оценку для категории "Drama"
average_score = average_imdb_by_category(movies, "Drama")
print(f"Average IMDb score for Drama: {average_score}")
