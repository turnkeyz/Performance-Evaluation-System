from flask import Flask, json, render_template, url_for, request, redirect, jsonify
from flask.helpers import make_response
from connection import Database
import uuid
from __main__ import app, secure_site, db

nav_columns = {"Overview":"admin_overview", "Staff":"admin_staff", "Families":"admin_families", "Business":"admin_business"}


@app.route("/admin/overview", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def admin_overview(auth_data = None):
    staff_table = db.query('Select * FROM staff')
    return render_template('admin.html',auth_data=auth_data, nav_columns= nav_columns, staff_table=staff_table)

@app.route("/admin/staff", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def admin_staff(auth_data = None):
    staff_table = db.query('Select * FROM staff')
    if request.method == 'GET':
        return render_template('/elements/staff_form.html',auth_data=auth_data, nav_columns= nav_columns, staff_table=staff_table)
    elif request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        phoneNumber = request.form['phoneNumber']
        email = request.form['email']
        staff_insert = db.query('INSERT INTO staff(firstName, lastName, phoneNumber, email) Values (%s,%s,%s,%s)',
                                (firstName, lastName, phoneNumber, email))
        # db.cursor.execute(family_insert)
        return render_template('success.html'), {"Refresh": "2; url=/admin/families"}

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    return render_template('admin.html', auth_data=auth_data, nav_columns=nav_columns)

@app.route("/admin/families", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def admin_families(auth_data = None):
    family_table = db.query('Select * FROM family')
    if request.method == 'GET':
        return render_template("family.html",auth_data=auth_data, nav_columns=nav_columns,family_table=family_table)
    elif request.method == 'POST':
        return render_template("")
    
@app.route("/admin/business", methods = ["POST", "GET"])
@secure_site
def admin_business(auth_data = None):
    if request.method == 'GET':
        return render_template("/elements/family_form.html",auth_data=auth_data, nav_columns=nav_columns)
    elif request.method == 'POST':
        familyName = request.form['familyName']
        db.create_family(familyName)
        return render_template('success.html'), {"Refresh": "2; url=/admin/families"}
    return render_template('/elements/family_form.html', auth_data=auth_data, nav_columns=nav_columns)