import functools

numbers = [2, 3, 4, 5]

result = functools.reduce(lambda x, y: x * y, numbers)
print(f"Multiplication of all numbers: {result}")
