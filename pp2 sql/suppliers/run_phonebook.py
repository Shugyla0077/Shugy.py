# run_phonebook.py
from phonebook import insert_user, insert_from_csv

# Вставка данных вручную через консоль
insert_user()

# Или вставка данных из CSV
insert_from_csv('phonebook.csv')  # Путь к твоему CSV-файлу
