import json

fileName = "test.json"
jsonString = '{ "name": "Daniel", "email": "test@test.com", "age": 31}'
jsonString = json.loads(jsonString)

file = open(fileName, "w")
json.dump(jsonString, file)
file.close()