from datetime import datetime, timedelta


today = datetime.now()


yesterday = today - timedelta(days=1)


tomorrow = today + timedelta(days=1)


print("Вчера:", yesterday.strftime("%Y-%m-%d"))
print("Сегодня:", today.strftime("%Y-%m-%d"))
print("Завтра:", tomorrow.strftime("%Y-%m-%d"))
