import psycopg2


DB_USER = "postgres"
DB_PASSWORD = "20061985"
DB_HOST = "localhost"
DB_NAME = "mydatabase"


conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()



cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20)
)
""")
conn.commit()

print("Connected to database and table ready.")



def search_pattern():
    pattern = input("Введите шаблон поиска: ")
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(r)
    else:
        print("Ничего не найдено.")


def insert_or_update():
    first = input("Имя: ")
    last  = input("Фамилия: ")
    phone = input("Телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (first, last, phone))
    conn.commit()
    print("Операция выполнена.")


def insert_many():
    n = int(input("Сколько пользователей вставить? "))
    first_list = []
    last_list = []
    phone_list = []
    for i in range(n):
        print(f"\nПользователь #{i+1}")
        first_list.append(input("Имя: "))
        last_list.append(input("Фамилия: "))
        phone_list.append(input("Телефон: "))
    
    
    cur.execute(
        "CALL insert_many_users(%s, %s, %s)",
        (first_list, last_list, phone_list)
    )
    conn.commit()
    print("Массовая вставка выполнена.")


def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for r in rows:
        print(r)


def delete_value():
    val = input("Введите имя/фамилию/телефон для удаления: ")
    cur.execute("CALL delete_by_value(%s)", (val,))
    conn.commit()
    print("Удаление выполнено.")


while True:
    print("\n MENU ")
    print("1) Search by pattern")
    print("2) Insert or update one user")
    print("3) Insert many users")
    print("4) Pagination")
    print("5) Delete by name or phone")
    print("6) Exit")

    choice = input("Choose: ")

    if choice == "1":
        search_pattern()
    elif choice == "2":
        insert_or_update()
    elif choice == "3":
        insert_many()
    elif choice == "4":
        pagination()
    elif choice == "5":
        delete_value()
    elif choice == "6":
        break
    else:
        print("Wrong choice")



cur.close()
conn.close()