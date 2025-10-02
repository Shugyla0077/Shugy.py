import itertools

def print_permutations():
    
    s = input("Enter a string: ")
    
   
    permutations = itertools.permutations(s)
    
    
    for perm in permutations:
        print(''.join(perm))


print_permutations()
