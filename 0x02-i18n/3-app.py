#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for languages available for translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Picks best language based on client request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"])
def home():
    """Renders index.html"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
