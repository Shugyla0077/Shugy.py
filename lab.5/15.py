import re
pattern= r"[a-z]+_[a-z]+"

string="hello_world this_is_a_test example_case"

matches=re.findall(pattern,string)

print(matches)