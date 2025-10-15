pattern = r"[a-z]+_[a-z]+"
string = "lower_case_example"
matches = re.findall(pattern, string)
print(matches)
