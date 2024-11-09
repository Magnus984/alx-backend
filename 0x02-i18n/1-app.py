#!/usr/bin/env python3
"""Setting up babel"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for languages available for translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", methods=["GET"])
def hello_world():
    """Renders index.html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
