from flask import Flask, json, render_template, url_for, request, redirect, jsonify
from flask.helpers import make_response
from connection import Database
from __main__ import app, secure_site, db

nav_columns = {}

@app.route("/todos", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def todos(auth_data = None):
    return render_template('todos.html', auth_data = auth_data, nav_columns = nav_columns)