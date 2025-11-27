def squares (a,b):
    for i in range(a, b+1):
      yield i*i
a=1
b=5
for square in squares (a,b):
    print(square)