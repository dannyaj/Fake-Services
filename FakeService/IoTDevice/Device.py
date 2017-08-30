from flask import Flask, request, flash, abort
import json

app = Flask(__name__)

@app.route('/led', methods=['POST'])
def create_token():
    body = request.get_json(force=True)
    if body.get('power') == None:
        abort(400)
    return app.response_class(
        response="OK",
        status=200
    )


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)


