def is_good_movie(movie):
    """Проверяет, если IMDB оценка фильма больше 5.5"""
    return movie["imdb"] > 5.5

# Пример использования:
movie = {
    "name": "The Dark Knight",
    "imdb": 9.0,
    "category": "Action"
}

print(is_good_movie(movie))  # Выведет: True

movie2 = {
    "name": "The Room",
    "imdb": 3.7,
    "category": "Drama"
}

print(is_good_movie(movie2))  # Выведет: False
