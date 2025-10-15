def camel_to_snake(string):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', string).lower()

string = "camelCaseExample"
result = camel_to_snake(string)
print(result)
