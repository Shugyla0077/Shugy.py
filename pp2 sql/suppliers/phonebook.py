
import psycopg2
import csv


DB_CONFIG = {
    "dbname": "phonebook",
    "user": "postgres",
    "password": "20061985",  
    "host": "localhost",
    "port": "5432",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)



def init_db():
    """Создает таблицы, если их еще нет."""
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50)
    );
    """

    create_phone_numbers_table = """
    CREATE TABLE IF NOT EXISTS phone_numbers (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        phone_number VARCHAR(20) NOT NULL UNIQUE
    );
    """

    create_snake_scores_table = """
    CREATE TABLE IF NOT EXISTS snake_scores (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        score INT NOT NULL,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(create_users_table)
            cur.execute(create_phone_numbers_table)
            cur.execute(create_snake_scores_table)
        conn.commit()




def insert_user_from_console():
    """Вставка пользователя и телефона через консоль."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;",
                (first_name, last_name),
            )
            user_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s);",
                (user_id, phone_number),
            )
        conn.commit()
    print("User and phone number added successfully!")


def insert_from_csv():
    """Вставка пользователей из CSV файла.
    Формат CSV: first_name,last_name,phone_number (первая строка может быть заголовком).
    """
    csv_file = input("Enter csv file path: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                
                header = next(reader, None)
                
                if header and len(header) == 3 and header[0].lower() not in ("first_name", "firstname"):
                    
                    first_name, last_name, phone_number = header
                    cur.execute(
                        "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;",
                        (first_name, last_name),
                    )
                    user_id = cur.fetchone()[0]
                    cur.execute(
                        "INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s);",
                        (user_id, phone_number),
                    )

                for row in reader:
                    if len(row) != 3:
                        print("Skipping invalid row:", row)
                        continue
                    first_name, last_name, phone_number = row
                    cur.execute(
                        "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;",
                        (first_name, last_name),
                    )
                    user_id = cur.fetchone()[0]
                    cur.execute(
                        "INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s);",
                        (user_id, phone_number),
                    )

        conn.commit()
    print("Users and phone numbers added from CSV.")




def update_first_name():
    old_name = input("Enter current first name: ")
    new_name = input("Enter new first name: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET first_name = %s WHERE first_name = %s;",
                (new_name, old_name),
            )
            print(f"Updated rows: {cur.rowcount}")
        conn.commit()


def update_phone():
    old_phone = input("Enter current phone number: ")
    new_phone = input("Enter new phone number: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phone_numbers SET phone_number = %s WHERE phone_number = %s;",
                (new_phone, old_phone),
            )
            print(f"Updated rows: {cur.rowcount}")
        conn.commit()




def list_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT u.id, u.first_name, u.last_name, p.phone_number
                FROM users u
                LEFT JOIN phone_numbers p ON u.id = p.user_id
                ORDER BY u.id;
                """
            )
            rows = cur.fetchall()
    if not rows:
        print("No users found.")
        return
    for r in rows:
        print(f"ID: {r[0]}, Name: {r[1]} {r[2]}, Phone: {r[3]}")


def find_by_name():
    pattern = input("Enter name pattern to search (part of first name): ")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT u.id, u.first_name, u.last_name, p.phone_number
                FROM users u
                LEFT JOIN phone_numbers p ON u.id = p.user_id
                WHERE u.first_name ILIKE %s;
                """,
                (f"%{pattern}%",),
            )
            rows = cur.fetchall()
    if not rows:
        print("No users found.")
        return
    for r in rows:
        print(f"ID: {r[0]}, Name: {r[1]} {r[2]}, Phone: {r[3]}")


def find_by_phone():
    phone = input("Enter phone number to search: ")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT u.id, u.first_name, u.last_name, p.phone_number
                FROM users u
                JOIN phone_numbers p ON u.id = p.user_id
                WHERE p.phone_number = %s;
                """,
                (phone,),
            )
            rows = cur.fetchall()
    if not rows:
        print("No users found with this phone.")
        return
    for r in rows:
        print(f"ID: {r[0]}, Name: {r[1]} {r[2]}, Phone: {r[3]}")




def delete_by_name():
    first_name = input("Enter first name to delete: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            
            cur.execute(
                """
                DELETE FROM phone_numbers
                WHERE user_id IN (SELECT id FROM users WHERE first_name = %s);
                """,
                (first_name,),
            )
            
            cur.execute(
                "DELETE FROM users WHERE first_name = %s;",
                (first_name,),
            )
            print(f"Deleted users: {cur.rowcount}")
        conn.commit()


def delete_by_phone():
    phone = input("Enter phone number to delete: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phone_numbers WHERE phone_number = %s;",
                (phone,),
            )
            print(f"Deleted phone records: {cur.rowcount}")
        conn.commit()




def add_snake_score():
    """Добавить результат игры snake для пользователя."""
    user_id = int(input("Enter user id: "))
    score = int(input("Enter score: "))

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO snake_scores (user_id, score) VALUES (%s, %s);",
                (user_id, score),
            )
        conn.commit()
    print("Score added.")


def list_user_scores():
    user_id = int(input("Enter user id: "))

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT s.id, s.score, s.played_at
                FROM snake_scores s
                WHERE s.user_id = %s
                ORDER BY s.played_at DESC;
                """,
                (user_id,),
            )
            rows = cur.fetchall()
    if not rows:
        print("No scores for this user.")
        return
    for r in rows:
        print(f"ScoreID: {r[0]}, Score: {r[1]}, Played at: {r[2]}")


def list_top_scores():
    limit = int(input("How many top scores to show? "))

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT u.first_name, u.last_name, s.score, s.played_at
                FROM snake_scores s
                JOIN users u ON s.user_id = u.id
                ORDER BY s.score DESC
                LIMIT %s;
                """,
                (limit,),
            )
            rows = cur.fetchall()
    if not rows:
        print("No scores yet.")
        return
    for r in rows:
        print(f"Name: {r[0]} {r[1]}, Score: {r[2]}, Played at: {r[3]}")


# ------------------ Меню ------------------

def print_menu():
    print("\n--- PHONEBOOK MENU ---")
    print("1. Insert user from console")
    print("2. Insert users from CSV")
    print("3. Update user first name")
    print("4. Update phone number")
    print("5. List all users")
    print("6. Find users by first name pattern")
    print("7. Find user by phone")
    print("8. Delete users by first name")
    print("9. Delete by phone number")
    print("10. Add snake game score")
    print("11. List user snake scores")
    print("12. Show top snake scores")
    print("0. Exit")


def main():
    init_db() 

    while True:
        print_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            insert_user_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_first_name()
        elif choice == "4":
            update_phone()
        elif choice == "5":
            list_all_users()
        elif choice == "6":
            find_by_name()
        elif choice == "7":
            find_by_phone()
        elif choice == "8":
            delete_by_name()
        elif choice == "9":
            delete_by_phone()
        elif choice == "10":
            add_snake_score()
        elif choice == "11":
            list_user_scores()
        elif choice == "12":
            list_top_scores()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Unknown option, try again.")


if __name__ == "__main__":
    main()
