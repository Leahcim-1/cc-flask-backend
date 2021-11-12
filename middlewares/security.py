import json
from flask_dance.contrib.google import make_google_blueprint, google

"""
read client secret from the local client secret json file 
"""
with open('client_secret.json','r') as myfile:
    data = myfile.read()

obj = json.loads(data)


def security():
    blueprint = make_google_blueprint(
        client_id=obj["web"]["client_id"],
        client_secret=obj['web']['client_secret'],
        scope=["openid email profile"]
    )
    return blueprint
