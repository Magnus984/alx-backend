#!/usr/bin/env python3
"""Infer appropriate time zone"""
from flask import Flask, g, request, render_template
from flask_babel import Babel
from pytz import exceptions, timezone as tz

app = Flask(__name__)

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


app.config.from_object(Config)
babel = Babel(app)


@app.route("/", methods=["GET"])
def home():
    """Renders index.html"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Picks best language based on client request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    return (request.accept_languages.best_match(app.config['LANGUAGES']) or
            app.config['BABEL_DEFAULT_LOCALE'])


def get_user():
    """returns user dictionary or None"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except TypeError:
        return None


@app.before_request
def before_request():
    """finds a user if any and set it as a global"""
    user = get_user()
    if user:
        setattr(g, 'user', user)


@babel.timezoneselector
def get_timezone():
    """Gets timezone of user"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return tz(timezone).zone
        except exceptions.UnknownTimeZoneError:
            pass
    user = getattr(g, "user", None)
    if user and user.get('timezone'):
        try:
            return tz(user.get('timezone')).zone
        except exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
