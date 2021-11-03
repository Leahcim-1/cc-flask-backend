from flask import Flask, request, Response
import requests

app = Flask(__name__)

USER_SERVICE_HOST = 'http://127.0.0.1:5000/'


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

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/users")
def users_proxy():
    return proxy(USER_SERVICE_HOST)

@app.route("/api/users/<id>")
def users_proxy_id(id):
    return proxy(USER_SERVICE_HOST)
