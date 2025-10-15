pattern = r"[ ,.]"
string = "Hello, world. How are you?"
result = re.sub(pattern, ":", string)
print(result)
