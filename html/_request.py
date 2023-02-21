import requests
import json


result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
print(type(result))


# print(result[0]["title"])

# for i in result:
#     print(i["id"])



 