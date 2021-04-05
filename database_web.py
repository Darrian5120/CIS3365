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

############################################## READ ME #####################################
# RUN THIS PROGRAM AND THEN OPEN BROWSER AND PASTE http://127.0.0.1:5000/ TO YOUR BROWSER
# MAKE SURE YOU HAVE ALL HTML PAGES DOWNLOADED AND CHANGE YOUR CONNECTION STRING TO YOUR OWN
# Every category should have a CRUD operation, please pick one to code with python AND html
# Recycle other's code and make sure your code works before pushing to github and include useful comments
############################################################################################
# Darrian - customer create(insert), customer delete, customer update, customer report
# Mustafa - vehicles insert, vehicle delete, vehicle update, vehicle stuff
# Brandon - insurance policy create (insert), insurance policy delete, insurance policy update, insurance policy report 
# Anthony - employee create(insert), employee delete, employee update, employee report
# Maddy - supplier create(insert), supplier delete, supplier update, supplier report
# Jerry - 
# Kyle - service create(insert), service delete, service update, service report
# Jahidul - 
# Gian - 
# Zach - violation insert, Report delete, Report update

app = flask.Flask(__name__)
app.config["DEBUG"] = True # browser can see error messages
############################# HOME PAGE ####################################################
# create first route map to url functions. home mapped to '/'
# Home page for the web app where user can choose CRUD operations.
@app.route('/', methods = ['GET']) 
def home():
    return render_template('home.html')

############################# CUSTOMER #####################################################
# Customer home page. Can select multiple CRUD options for customers
# reference customer.html for menu options.
@app.route('/customers', methods = ['GET']) 
def customers():
        return render_template('customers.html')
    
# Reference new customer html page. Allows user to enter the details of new customer
# to the database  
# FIXME - Data does not save to database resets after every server restart
# FIXME - Combine customer and customer contact info
@app.route('/customers/newcustomer', methods = ['POST','GET']) 
def new_customer():
    message = ''
    if request.method == 'POST':
        lname = request.form.get("lname")
        fname = request.form.get("fname")
        bname = request.form.get("bname")
        if lname and fname and bname is not None:
            # new customer default
            query = "INSERT INTO CoogTechSolutions.dbo.Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?)"
            vals = (lname, fname, bname)
            data = cursor.execute(query, vals)
            customer_id = cursor.fetchone()[0]
            conn.commit()
            # new customer status
            query = "INSERT INTO CoogTechSolutions.dbo.CUSTOMER_STATUS (CUSTOMER_ID, C_ACTIVE, ACTIVE) VALUES (?,?,?)"
            status_vals = (customer_id, 1, "ACTIVE")
            data = cursor.execute(query, status_vals)
            conn.commit()
            # new customer contact info
            phone = request.form.get("phone")
            email = request.form.get("email")
            address = request.form.get("addy")
            zip_code = request.form.get("zip")
            city = request.form.get("city")
            state = request.form.get("state")
            query = "INSERT INTO CoogTechSolutions.dbo.CUSTOMER_CONTACT_INFO (CUSTOMER_ID, C_PHONE, C_EMAIL, C_ADDRESS, C_ZIP, C_CITY, STATE_NAME) VALUES (?,?,?,?,?,?,?)"
            contact_vals = (customer_id, phone, email, address, zip_code, city, state)
            data = cursor.execute(query, contact_vals)
            conn.commit()
            # new customer type
            #business = request.form.get("is_biz")
            #query = "INSERT INTO CoogTechSolutions.dbo.CUSTOMER_TYPE (CUSTOMER_ID, IS_BUSINESS) VALUES (?,?)"
            #vals = (customer_id, business)
            # new customer state
            message = "New customer entered successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('newcustomer.html')

# modify exisitng customer by entering id
# FIXME- find out how to only update one field
@app.route('/customers/updatecustomer', methods = ['POST','GET'])
def update_customer():
    message = ''
    if request.method == 'POST':
        customer_id = request.form.get("cid")
        field = request.form.get("field")
        value = request.form.get("value")
        if customer_id and field and value is not None:
            query = "UPDATE CoogTechSolutions.dbo.Customer SET {fld} = ? WHERE CUSTOMER_ID = ?".format(fld = field)
            vals = (value, customer_id)
            data = cursor.execute(query, vals)
            conn.commit()
            message = "Customer edited successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('updatecustomer.html')

# remove customer from db by setting status to inactive
@app.route('/customers/deletecustomer',methods = ['POST','GET'])
def delete_customer():
    message = ''
    if request.method == 'POST':
        friendid = request.form.get("fid")
        if friendid is not None:
            query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_STATUS SET ACTIVE_ID = 2 ACTIVE='INACTIVE' WHERE CUSOTMER_ID = ?"
            vals = (friendid)
            data = cursor.execute(query, vals)
            message = "Customer removed successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('deletecustomer.html')

# view all customers
@app.route('/customers/viewcustomers', methods = ['GET']) 
def view_customers():
    cursor.execute("SELECT * FROM CoogTechSolutions.dbo.Customer")
    data = cursor.fetchall()
    conn.commit()
    return render_template('viewCustomers.html', data = data)





################################### VEHICLES ##################################################
@app.route('/vehicles', methods = ['GET']) 
def vehicles():
    return render_template('vehicles.html')

@app.route('/customers/viewcustomers', methods = ['GET']) 
def vehicle_part_report():
    cursor.execute("""
    SELECT VEHICLE_SERVICE.V_VIN AS "VIN", VEHICLE.V_YEAR AS "Year", VEHICLE.V_MAKE AS "Make", 
    VEHICLE.V_MODEL AS "Model", SUPPLIER.SUPPLIER_NAME AS "Supplier", PART.PART_NAME AS "Part"

    FROM VEHICLE
    JOIN VEHICLE_SERVICE
    ON VEHICLE.V_VIN = VEHICLE_SERVICE.V_VIN
    JOIN SERVICE
    ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
    JOIN SERVICE_LINE
    ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
    JOIN SERVICE_LINE_PART
    ON  SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_PART.SERVICE_LINE_ID
    JOIN PART
    ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
    JOIN SUPPLIER_PART
    ON PART.PART_ID = SUPPLIER_PART.PART_ID
    JOIN SUPPLIER
    ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

    ORDER BY VEHICLE.V_VIN;""")
    data = cursor.fetchall()
    conn.commit()
    return render_template('viewCustomers.html', data = data)

################################### EMPLOYEES ##################################################
@app.route('/employees', methods = ['GET']) 
def employees():
    return render_template('employees.html')

@app.route ('/employees/newemployee', methods = ['POST', 'GET'])
def new_employee():
    message = ''
    if request.method == 'POST':
        lname = request.form.get ("lname")
        lname = request.form.get ("fname")
        address = request.form.get ("address")
        pnumber = request.form.get ("pnumber")
        jobfunc = requet.form.get ("jobfunc")
        if lname and fname and address and pnumber and jobfunc is not None:
            
            # new employee default
            query = ""
            vals = 
            data = 
            conn.commit()
            
            # new employee status
            query = ""
            vals = 
            data = 
            conn.commit()
            
            # new employee contact info
            
            #
            
            message = "New employee entered successfully!"
            return render_template ('employees.html' , data = data, message = message)
        return render_template ('newemployee.html')
    
    # modify existing employee by entering id
    @app.route ('/employees/updateemployee' , methods = ['POST' , 'GET'])
    def update_employee():
        if request.method == 'POST':
            friendid = request.form.get ("fid")
            field =  request.form.get ("field")
            value = request.form.get ("value")
            if friendid and field and value is not None:
                query = 
                vals = 
                data = 
                conn.commit ()
                message = "Employee edited sucessfully!"
                return render_template ('employees.html' data = data , message = message)
            return render_template ('updateemployee.html')
        
        # remove employee from db by setting status to inactive
        @app.route ('/employees/deleteemloyee' , methods =['POST' , 'GET'])
        def delete_employee():
            message = ''
            friendid = request.form.get ("fid")
            if friendid is not None:
                query = 
                vals = 
                data = 
                conn.commit()
                message = "Employee removed successfully!"
                return render_template ('employees.html' , data = data , message = message)
            return render_template('deleteemployee.html')
        
        #view all employees
        @app.route ('/employees/viewemployee' , methods = ['GET'])
        def view_employee():
            cursor.execute ("SELECT * FROM CoogTechSolutions.dbo.Employee")
            data = cursor.fetchall()
            return render_template ('viewemployee.html' , data = data)
        
################################### SERVICES ##################################################
@app.route('/services', methods = ['GET']) 
def services():
    return render_template('services.html')

################################### VIOLATIONS ##################################################
@app.route('/reports', methods = ['GET']) 
def reports():
    return render_template('reports.html')



if __name__ == '__main__':
    # Connection to school provided server, don't use till final.
    #conn = pyodbc.connect('Driver={SQL Server};'
    #                    'Server=CoT-CIS3365-05.cougarnet.uh.edu;'
    #                    'Database=CoogTechSolutions;'
    #                    'UID=;'
    #                    'PWD=;'
    #                    'Trusted_Connection=no;')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=DESKTOP-9PNG3JO;'
                        'Database=CoogTechSolutions;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()
    app.run()
    conn.close()
