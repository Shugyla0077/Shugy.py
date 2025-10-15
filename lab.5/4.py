pattern = r"[A-Z][a-z]+"
string = "Hello"
matches = re.findall(pattern, string)
print(matches)
