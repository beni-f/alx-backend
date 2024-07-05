#!/usr/bin/env python3
"""
Get locale from request
"""
from flask_babel import Babel, _
from flask import Flask, request, render_template, g
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)


class Config:
    """
        Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        Returns the best choice of language
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
        Simple route
    """
    return render_template('5-index.html')


def get_user():
    """
        Returns a user dictionary or None if
        the ID cannot be found or if login_as is not passed
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
        Before Request
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if(timezone):
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']