def spy_game(nums):
    
    seq = [0, 0, 7]
    index = 0
    for num in nums:
        if num == seq[index]:
            index += 1
        if index == len(seq):  
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Выведет: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Выведет: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Выведет: False
