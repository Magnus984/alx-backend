#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route("/")
def hello_world() -> Response:
    """Renders index.html"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
