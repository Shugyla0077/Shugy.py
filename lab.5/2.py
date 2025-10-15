pattern = r"ab{2,3}"
string = "abb"
if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")
