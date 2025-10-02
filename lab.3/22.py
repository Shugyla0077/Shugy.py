def filter_by_category(movies, category_name):
    """Возвращает список фильмов, относящихся к указанной категории"""
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

# Пример использования:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "The Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Room", "imdb": 3.7, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Joker", "imdb": 8.4, "category": "Drama"}
]

# Фильтрация по категории "Drama"
drama_movies = filter_by_category(movies, "Drama")

# Выводим результат
for movie in drama_movies:
    print(movie["name"], "-", movie["category"])
