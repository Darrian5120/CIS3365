import flask
from flask import request, make_response, render_template
from flask import Flask, render_template
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

######### Helpful sites ###############
#https://kanchanardj.medium.com/how-to-display-database-content-in-your-flask-website-8a62492ba892
#https://medium.com/analytics-vidhya/flask-html-template-with-mysql-2f3b9405d0e2
def create_connection():
    conn = pyodbc.connect('Driver={SQL Server};'
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

# Customer page
@app.route('/customers', methods = ['POST','GET']) 
def customers():
    cursor.execute("SELECT * FROM Customer")
    data = cursor.fetchall()
    return render_template('customers.html', data = data)


if __name__ == '__main__':
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=DESKTOP-9PNG3JO;'
                        'Database=CoogTechSolutions;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()
    app.run()