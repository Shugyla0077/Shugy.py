this_list=input("Enter numbers: ")
numbers=[int (n)for n in this_list.split()]
print(numbers)
 







this_list=input("Enter numbers: ")
numbers= list(this_list)
print(numbers)




this_list=input("Enter numbers:")
numbers=list(this_list)
print(numbers)






import math

def pythagorean_theorem(a, b):
    
    c = math.sqrt(a**2 + b**2)
    return c

a = 3
b = 4
c = pythagorean_theorem(a, b)
print(f"Гипотенуза: {c}")
