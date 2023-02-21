
import json



person_string = '{"name":"Ali ","languages":["python","C#"]}'

# json string to Dict

# result = json.loads(person_string)

# print(type(result))

# result = result["name"]
# result = result["languages"]

with open ("person.json") as f:
    data = json.load(f)
    print(data)





