import json
f\
    = open("test.json","r")
data = f.read()
jsonObj = json.loads(data)