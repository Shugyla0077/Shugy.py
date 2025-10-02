def filter_good_movies(movies):
    """Возвращает список фильмов с оценкой IMDb выше 5.5"""
    return [movie for movie in movies if movie["imdb"] > 5.5]

# Пример использования:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "The Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Room", "imdb": 3.7, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"}
]

good_movies = filter_good_movies(movies)

# Выводим результат
for movie in good_movies:
    print(movie["name"], "-", movie["imdb"])
