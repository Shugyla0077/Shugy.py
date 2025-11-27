import psycopg2
import time

# Конфигурация базы данных
DB_CONFIG = {
    "dbname": "snake_game",
    "user": "postgres",
    "password": "20061985",  
    "host": "localhost",
    "port": "5432",
}

# Функция для установления соединения с базой данных
def get_connection():
    print("Connecting to the database...")
    return psycopg2.connect(**DB_CONFIG)

# Функция для инициализации таблиц
def init_db():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        level INT DEFAULT 1
    );
    """
    create_user_scores_table = """
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        score INT NOT NULL,
        level INT NOT NULL,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(create_users_table)
            cur.execute(create_user_scores_table)
        conn.commit()


def get_or_create_user(username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            
            cur.execute("SELECT id, username, level FROM users WHERE username = %s;", (username,))
            user = cur.fetchone()

            if user:
                
                print(f"Welcome back, {username}! Your current level is {user[2]}")
                return user[0], user[2] 
            else:
                
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
                user_id = cur.fetchone()[0]
                print(f"New user created: {username}! Starting at level 1.")
                return user_id, 1  # Новый пользователь, уровень 1

# Функция для сохранения состояния игры
def save_game_state(user_id, score, level):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);",
                (user_id, score, level)
            )
        conn.commit()
    print(f"Game saved. Your score is {score} and level is {level}.")

# Функция для симуляции игры
def start_game():
    # Запрашиваем имя пользователя
    username = input("Enter your username: ")

    # Получаем или создаем пользователя
    user_id, level = get_or_create_user(username)

    # Инициализация начальных значений
    score = 0
    game_running = True

    while game_running:
        print(f"Level {level} - Score: {score}")
        action = input("Press 'p' to pause and save, 'q' to quit, or any key to continue: ").strip().lower()

        if action == 'p':
            save_game_state(user_id, score, level)
            print("Game paused. Your progress is saved.")
            break  
        elif action == 'q':
            print("Game Over!")
            break
        else:
            score += 10  
            if score % 50 == 0:
                level += 1  # Увеличиваем уровень каждые 50 очков
            time.sleep(1)  
    
    
    save_game_state(user_id, score, level)


def print_menu():
    print("\n--- SNAKE GAME MENU ---")
    print("1. Start game")
    print("0. Exit")


def main():
    init_db()  

    while True:
        print_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            start_game()  
        elif choice == "0":
            print("Goodbye!")  
            break
        else:
            print("Unknown option, try again.") 

if __name__ == "__main__":
    main()
