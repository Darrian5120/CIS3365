import flask
from flask import request, make_response, render_template
from flask import Flask
import pyodbc
import pandas as pd 
import datetime
import time
import sys
import requests
import json
import ssl
import datetime
from tabulate import tabulate
import cgi

######### Helpful sites ###############
#https://kanchanardj.medium.com/how-to-display-database-content-in-your-flask-website-8a62492ba892
#https://medium.com/analytics-vidhya/flask-html-template-with-mysql-2f3b9405d0e2

def create_connection():
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=DESKTOP-9PNG3JO;'
                        'Database=CoogTechSolutions;'
                        'Trusted_Connection=yes;')
    #conn = pyodbc.connect('Driver={SQL Server};'
    #                    'Server=CoT-CIS3365-05.cougarnet.uh.edu;'
    #                    'Database=CoogTechSolutions;'
    #                    'UID=;'
    #                    'PWD=;'
    #                    'Trusted_Connection=no;')
    return conn    

app = flask.Flask(__name__)
app.config["DEBUG"] = True # browser can see error messages
# create first route map to url functions. home mapped to '/'
# Home page for the web app where user can choose CRUD operations.
@app.route('/', methods = ['GET']) 
def home():
    return render_template('home.html')

# Customer home page. Can select multiple CRUD options for customers
# reference customer.html for menu options.
@app.route('/customers', methods = ['GET']) 
def customers():
        return render_template('customers.html')
    
# Reference new customer html page. Allows user to enter the details of new customer
# to the database  
@app.route('/customers/newcustomer', methods = ['POST','GET']) 
def new_customer():
    message = ''
    if request.method == 'POST':
        lname = request.form.get("lname")
        fname = request.form.get("fname")
        bname = request.form.get("bname")
        if lname and fname and bname is not None:
            query = "INSERT INTO Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME) VALUES (?,?,?)"
            vals = (lname, fname, bname)
            data = cursor.execute(query, vals)
            message = "New customer entered successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('newcustomer.html')

# view all customers
@app.route('/customers/viewcustomers', methods = ['GET']) 
def view_customers():
    cursor.execute("SELECT * FROM Customer")
    data = cursor.fetchall()
    return render_template('viewCustomers.html', data = data)






    


@app.route('/vehicles', methods = ['POST','GET']) 
def vehicles():
    
    return render_template('vehicles.html')

@app.route('/employees', methods = ['POST','GET']) 
def employees():
    return render_template('employees.html')
    
@app.route('/services', methods = ['POST','GET']) 
def services():
    return render_template('services.html')

@app.route('/reports', methods = ['POST','GET']) 
def reports():
    return render_template('reports.html')



if __name__ == '__main__':
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=DESKTOP-9PNG3JO;'
                        'Database=CoogTechSolutions;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()
    app.run()