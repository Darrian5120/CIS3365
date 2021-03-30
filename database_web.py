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
@app.route('/', methods = ['GET']) 
def home():
    return render_template('/website/home.html')

if __name__ == '__main__':
    #conn = create_connection()
    #cursor = conn.cursor()
    app.run()