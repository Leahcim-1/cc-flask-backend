import json
from flask_dance.contrib.google import make_google_blueprint, google

with open('client_secret.json','r') as myfile:
    data = myfile.read()

obj = json.loads(data)

print(obj['web'])

def security():
    blueprint = make_google_blueprint(
        client_id=obj["web"]["client_id"],
        client_secret=obj['web']['client_secret'],
        scope=["openid email profile"]
    )
    return blueprint
