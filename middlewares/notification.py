import os
import json

with open ('../client_secret.json','r') as myfile:
        data = myfile.read()

obj = json.loads(data)

print(obj)
client = os.read()