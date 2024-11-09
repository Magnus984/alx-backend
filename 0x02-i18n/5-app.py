#!/usr/bin/env python3
"""Mock logging in"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"])
def home():
    """Renders index.html"""
    return render_template('5-index.html')


def get_user():
    """returns user dictionary or None"""
    try:
        user_id = int(request.args.get('login_as'))
        return users[user_id]
    except TypeError:
        return None


@app.before_request
def before_request():
    """finds a user if any and set it as a global"""
    user = get_user()
    setattr(g, 'user', user)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
