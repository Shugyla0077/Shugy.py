import re
pattern = r"ab*"
string = "abb"
if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")
