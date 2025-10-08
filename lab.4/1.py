def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2


N = 5
gen = square_generator(N)

for square in gen:
    print(square)
