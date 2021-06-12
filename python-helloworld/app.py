from datetime import datetime
import json
import logging

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    log_message(datetime.now(), request.path)
    return "Hello World!"


@app.route('/status')
def status():

    resp = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    log_message(datetime.now(), request.path)
    return resp


@app.route('/metrics')
def metrics():

    resp = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    log_message(datetime.now(), request.path)

    return resp


def log_message(log_datetime, endpoint):
    logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)
    message = str(log_datetime) + " " + str(endpoint) + " endpoint was reached"
    logging.debug(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
