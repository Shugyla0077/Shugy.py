pattern = r'(?=[A-Z])'
string = "CamelCaseString"
result = re.split(pattern, string)
print(result)
