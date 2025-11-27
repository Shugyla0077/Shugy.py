def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Әр санды қайтарамыз
        count += 1

gen = count_up_to(3)
for number in gen:
    print(number)  # 1, 2, 3
