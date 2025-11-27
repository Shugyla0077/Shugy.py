import json


json_string = '{"name": "John", "age": 30, "city": "New York"}'


data = json.loads(json_string)



print(data)
