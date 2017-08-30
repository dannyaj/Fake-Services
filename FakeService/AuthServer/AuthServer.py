from flask import Flask, request, flash, abort
import json

app = Flask(__name__)

token = "1kwemikv9ej21mckcork3"

@app.route('/auth', methods=['POST'])
def create_token():
    body = request.get_json(force=True)
    if body.get('username') == "user" and body.get('password') == "password":
        return token

@app.route('/auth/action', methods=['POST'])
def auth_action():
    body = request.get_json(force=True)
    print request.headers.get('Auth-Token')
    print token
    if request.headers.get('Auth-Token') != token:
        abort(403)

    return app.response_class(
        response="OK",
        status=200,
    )


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)


