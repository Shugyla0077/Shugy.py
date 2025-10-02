def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6]
result = unique_elements(numbers)
print(f"Unique elements: {result}")
