def snake_to_camel(string):
    return ''.join([string[0].lower()] + [x.upper() if i != 0 else x for i, x in enumerate(string[1:].split('_'))])

string = "snake_case_example"
result = snake_to_camel(string)
print(result)
