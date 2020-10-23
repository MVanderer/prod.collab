import os
import sys
from flask import (
    Flask,
    g,
    json,
    jsonify,
    make_response,
    request,
    send_from_directory,
)
from flask_api import status
# from flask_login import login_required

app = Flask(
    __name__,
    static_folder="../../dist"
    )

@app.route("/", methods=["GET", "POST"])
# @login_required
def index():
    from flask import current_app
    return current_app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5656,
        debug=False
    )