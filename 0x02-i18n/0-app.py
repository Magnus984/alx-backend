#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Renders index.html"""
    return render_template('index.html')
