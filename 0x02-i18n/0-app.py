#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template
app = Flask(__name__)
app.strict_slashes = True


@app.route('/')
def index():
    """
        Simple route
    """
    return render_template('0-index.html')
