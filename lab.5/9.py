pattern = r'([a-z])([A-Z])'
string = "CamelCaseString"
result = re.sub(pattern, r'\1 \2', string)
print(result)
