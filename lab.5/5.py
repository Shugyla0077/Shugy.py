pattern = r"a.*b"
string = "axxxxb"
if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")
