from flask import Flask, request, Response, redirect, url_for
import requests
from middlewares.security import security
from flask_dance.contrib.google import google

blueprint = security()

app = Flask(__name__)

app.secret_key = "cloud"

app.register_blueprint(blueprint, url_prefix="/login")

USER_SERVICE_HOST = 'http://6259-160-39-145-247.ngrok.io/'


def proxy(new_host):
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, new_host),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route("/api/users")
def users():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    print(resp.json())
    return "You are on Google"

@app.route("/")
def index():
    return "You are on Google"

@app.route("/api/users")
def users_proxy():
    return proxy(USER_SERVICE_HOST)

@app.route("/api/users/<id>")
def users_proxy_id(id):
    return proxy(USER_SERVICE_HOST)
