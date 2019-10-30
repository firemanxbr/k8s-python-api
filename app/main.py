"""
Simple Python Flask API
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_route():
    """
    main route
    """
    return "Success!"


@app.route("/ping")
def ping():
    """
    ping route
    """
    return "Ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
