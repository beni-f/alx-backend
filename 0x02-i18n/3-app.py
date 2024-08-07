#!/usr/bin/env python3
"""
Get locale from request
"""
from flask_babel import Babel, _
from flask import Flask, request, render_template


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
        Simple route
    """
    return render_template('3-index.html')
