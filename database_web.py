import flask
from flask import Flask, jsonify, request, make_response, render_template, url_for, redirect
import pyodbc
from collections import defaultdict
import json
import datetime
import sys

############################################## READ ME #####################################
# RUN THIS PROGRAM AND THEN OPEN BROWSER AND PASTE http://127.0.0.1:5000/ TO YOUR BROWSER
# MAKE SURE YOU HAVE ALL HTML PAGES DOWNLOADED AND CHANGE YOUR CONNECTION STRING TO YOUR OWN
# Every category should have a CRUD operation, please pick one to code with python AND html
# Recycle other's code and make sure your code works before pushing to github and include useful comments
############################################################################################
# Customer, Supplier, Vehicle, Employee
# EVERYONE MUST ALSO ENTER THEIR 4 REPORTS

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
@app.route('/customers/new-customer', methods = ['POST','GET']) # Finished
def new_customer():
    message = ''
    if request.method == 'POST':
        lname = request.form.get("lname")
        fname = request.form.get("fname")
        bname = request.form.get("bname")
        active = request.form.get("active")
        business = request.form.get("business")
        if lname and fname is not None:
            # new customer default
            phone = request.form.get("phone")
            email = request.form.get("email")
            address = request.form.get("addy1")
            address2 = request.form.get("addy2")
            zip_code = request.form.get("zip")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            query = "INSERT INTO Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME, ACTIVE_ID, BUSINESS_ID, C_ADDRESS_LINE1, C_ADDRESS_LINE2, C_CITY, STATE_NAME,  C_ZIP, COUNTRY_NAME, C_PHONE, C_EMAIL) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
            vals = (lname, fname, bname, active, business, address, address2, city, state, zip_code, country, phone, email)
            data = cursor.execute(query, vals)
            customer_id = cursor.fetchone()[0]
            conn.commit()
            # new customer state
            query = "SELECT STATE_ID FROM STATE WHERE STATE_NAME = ?"
            val = (state)
            cursor.execute(query, val)
            data = cursor.fetchall()
            print(data)
            query = "INSERT INTO CUSTOMER_STATE (CUSTOMER_ID, STATE_ID) VALUES ({},{})".format(customer_id, data[0][0])
            cursor.execute(query)
            conn.commit()
            message = "New customer entered successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('newcustomer.html')

# modify exisitng customer by entering id
# FIXME- find out how to only update one field
@app.route('/customers/update', methods = ['POST','GET']) # FINISHED
def update_customer():
    # send list of customer id's to gui dropdown
    sql = "SELECT CUSTOMER_ID, C_FNAME, C_LNAME FROM Customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    customers = []
    for customer in rows:
        customers.append(customer)
    sql = "SELECT ACTIVE_ID, ACTIVE_NAME FROM CUSTOMER_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    statuses = []
    for status in rows:
        statuses.append(status[1])
    sql = "SELECT BUSINESS_ID, BUSINESS FROM CUSTOMER_TYPE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    types = []
    for type in rows:
        statuses.append(type[1])
    sql = "SELECT STATE_ID, STATE_NAME FROM STATE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    states = []
    for state in rows:
        states.append(state[1])
    if request.method == 'POST':
        # convert customer id to int for sql statement
        customer_id = request.form.get('customer')
        print(customer_id)
        x = customer_id.split(", ")
        y = int(x[0][1:])
        # get table, column, and new value data
        field = request.form.get('tblname')
        value = request.form.get('value')
        if field == "SUPPLIER SET ACTIVE_ID":
            value = request.form.get('status')
            cursor.execute("SELECT ACTIVE_ID FROM CUSTOMER_STATUS WHERE ACTIVE_NAME = '{}'".format(value))
            status = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE CUSTOMER_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
        if field == "CUSTOMER SET BUSINESS_ID":
            value = request.form.get('type')
            cursor.execute("SELECT BUSINESS_ID FROM CUSTOMER_TYPES WHERE BUSINESS = '{}'".format(value))
            type = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE CUSTOMER_ID = ?".format(field)
            vals = (type, y)
            cursor.execute(sql, vals)
            conn.commit()
        if field == 'state':
            value = request.form.get('state')
            print(value)
            query = "SELECT STATE_ID FROM STATE WHERE STATE_NAME = ?"
            val = value
            print(val)
            cursor.execute(query, val)
            data = cursor.fetchone()[0]
            print(data)
            print(y)
            sql = "INSERT INTO CUSTOMER_STATE (CUSTOMER_ID, STATE_ID) VALUES (?,?)"
            vals = (y, data)
            cursor.execute(sql, vals)
            conn.commit()
        else:
            sql = "UPDATE {} = ? WHERE CUSTOMER_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
        return render_template('customers.html')
        #return redirect(url_for('edit_customer', customer_id=customer_id))
    return render_template('updatecustomer.html', customers=customers,types=types,statuses=statuses,states=states)

# remove customer from db by setting status to inactive
@app.route('/customers/delete-customer',methods = ['POST','GET']) # FINISHED
def delete_customer():
    # send list of customer id's to gui dropdown
    sql = "SELECT CUSTOMER_ID, C_FNAME, C_LNAME FROM Customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    customers = []
    for customer in rows:
        customers.append(customer)
    if request.method == 'POST':
        # convert customer id to int for sql statement
        customer_id = request.form.get('customer')
        print(customer_id)
        x = customer_id.split(", ")
        y = int(x[0][1:])
        # set inactive partial delete
        sql = "UPDATE Customer SET ACTIVE_ID = 2 WHERE CUSTOMER_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Customer removed Sucessfully'
        return render_template('deletecustomer.html', customers=customers, message = message)
        #return redirect(url_for('edit_customer', customer_id=customer_id))
    return render_template('deletecustomer.html', customers=customers)

# view all customers
@app.route('/customers/view-customers', methods = ['GET'])#FINISHED 
def view_customers():
    cursor.execute("""
        SELECT *

        FROM Customer
        JOIN CUSTOMER_TYPE
        ON Customer.BUSINESS_ID = CUSTOMER_TYPE.BUSINESS_ID
        JOIN CUSTOMER_STATUS
        ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID

        
        ORDER BY CUSTOMER.ACTIVE_ID, Customer.CUSTOMER_ID
    """)
    data = cursor.fetchall()
    return render_template('viewCustomers.html', data = data)

@app.route ('/customers/inactive-report' , methods = ['GET'])
def inactive_report():
    cursor.execute("""
        SELECT Customer.C_FNAME AS 'First Name', Customer.C_LNAME AS 'Last Name', CUSTOMER_TYPE.BUSINESS AS 'Type', 
        CUSTOMER_STATUS.ACTIVE_NAME,
        Customer.C_PHONE AS 'Phone', Customer.C_EMAIL AS 'Email'

        FROM Customer
        JOIN CUSTOMER_STATUS
        ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID
        JOIN SERVICE_ORDER
        ON Customer.CUSTOMER_ID = SERVICE_ORDER.CUSTOMER_ID
        JOIN CUSTOMER_TYPE
        ON CUSTOMER_TYPE.BUSINESS_ID = Customer.BUSINESS_ID

        WHERE Customer.ACTIVE_ID = 2 OR Customer.ACTIVE_ID = 4 /*OR SERVICE_ORDER.ORDER_DATE < GETDATE()*/
        ORDER BY CUSTOMER.C_LNAME, CUSTOMER.C_FNAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_inactivecustomer.html', data = data)

# report active customer (jahidul)
@app.route ('/customers/activecustomer-report' , methods = ['GET'])
def activecustomer_report():
    cursor.execute("""
        SELECT CUSTOMER.C_FNAME AS 'First Name',
		CUSTOMER.C_LNAME AS 'Last Name',
		CUSTOMER.C_ADDRESS_LINE1 AS 'Customer Address',
		CUSTOMER.C_CITY AS 'City',
		CUSTOMER.STATE_NAME AS 'State',
		CUSTOMER.C_ZIP AS 'ZIP Code',
		CUSTOMER_STATUS.ACTIVE_NAME AS 'Customer Status'
		
		FROM CUSTOMER
		JOIN CUSTOMER_STATUS
		ON CUSTOMER.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID
		JOIN CUSTOMER_TYPE
		ON CUSTOMER.BUSINESS_ID = CUSTOMER_TYPE.BUSINESS_ID
		JOIN CUSTOMER_STATE
		ON CUSTOMER.CUSTOMER_ID = CUSTOMER_STATE.CUSTOMER_ID
		JOIN STATE
		On STATE.STATE_ID = CUSTOMER_STATE.STATE_ID
		
		WHERE CUSTOMER_STATUS.ACTIVE_ID IN (1,3)
		ORDER BY CUSTOMER.C_LNAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_activecustomer.html', data = data)
	
# Customer owed (jerry)
@app.route ('/customers/customerowed-report' , methods = ['GET'])
def customerowed_report():
    cursor.execute("""
        SELECT
		CUSTOMER.C_FNAME AS 'First Name',
		CUSTOMER.C_LNAME AS 'Last Name',
		CUSTOMER.C_BUSINESS_NAME AS 'Business Name',
		SERVICE.SERVICE_TYPE AS 'Service Type',
		INVOICE.AMT_OWED AS 'Amount Owed',
		INVOICE.INVOICE_DATE AS 'Invoice Date',
		MAKE.MAKE_NAME AS 'Make',
		MODEL.MODEL_NAME AS 'Model',
		VEHICLE.V_LICENSE_PLATE AS 'License Plate'

		FROM CUSTOMER
		JOIN SERVICE_ORDER ON CUSTOMER.CUSTOMER_ID = SERVICE_ORDER.CUSTOMER_ID
		JOIN INVOICE ON SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID
		JOIN SERVICE_LINE ON SERVICE_ORDER.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
		JOIN SERVICE ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID
		JOIN VEHICLE_SERVICE ON SERVICE.SERVICE_ID = VEHICLE_SERVICE.SERVICE_ID
		JOIN VEHICLE ON VEHICLE_SERVICE.V_ID = VEHICLE.V_ID
		JOIN MODEL ON VEHICLE.MODEL_ID = MODEL.MODEL_ID
		JOIN MAKE ON MODEL.MAKE_ID = MAKE.MAKE_ID

		WHERE INVOICE.AMT_OWED > 0;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_customerowed.html', data = data)

# report uninsured customer policy (kyle)
@app.route ('/customers/uninsuredcuspolicy-report' , methods = ['GET'])
def uninsuredcuspolicy_report():
    cursor.execute("""
        SELECT
		Customer.CUSTOMER_ID AS 'Customer Id',
		Customer.C_FNAME AS 'First Name',
		Customer.C_LNAME AS 'Last Name',
		Customer.C_BUSINESS_NAME AS 'Business Name',
		INSURANCE_COMPANY.INSURANCE_NAME AS 'Insurance Name',
		INSURANCE_POLICY.POLICY_NAME AS 'Policy Name',
		VEHICLE.V_VIN AS 'VIN'


		FROM Customer
		JOIN POLICY
		ON Customer.CUSTOMER_ID = POLICY.CUSTOMER_ID
		JOIN INSURANCE_POLICY
		ON POLICY.POLICY_ID = INSURANCE_POLICY.POLICY_ID
		JOIN INSURANCE_COMPANY
		ON POLICY.INSURANCE_ID = INSURANCE_COMPANY.INSURANCE_ID
		JOIN VEHICLE
		ON POLICY.V_ID = VEHICLE.V_ID

		WHERE (Customer.ACTIVE_ID = 1 OR Customer.ACTIVE_ID = 3) AND POLICY.POLICY_ID = 9
		ORDER BY Customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_uninsuredcuspolicy.html', data = data)

# report business customer report (maddy)
@app.route ('/customers/businesscustomer-report' , methods = ['GET'])
def businesscustomer_report():
    cursor.execute("""
        DECLARE
		@business BIT

		SELECT @business = 1
		SELECT 
		Customer.CUSTOMER_ID AS 'Customer ID', 
		Customer.C_LNAME AS 'Customer Last Name', 
		Customer.C_FNAME AS 'Customer First Name', 
		Customer.C_BUSINESS_NAME AS 'Customer Business Name', 
		Customer_Type.BUSINESS AS 'Business Customer',
		Service_Order.SERVICE_ORDER_ID AS 'Service Order ID',
		Customer_Status.ACTIVE_NAME as 'Active/Inactive Status'

		FROM CUSTOMER
		JOIN CUSTOMER_TYPE ON Customer.BUSINESS_ID = Customer_Type.BUSINESS_ID
		JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = Customer_Vehicle.CUSTOMER_ID
		JOIN SERVICE_ORDER ON Customer.CUSTOMER_ID = Service_Order.CUSTOMER_ID
		JOIN CUSTOMER_STATUS ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID

		WHERE Customer_Type.BUSINESS_ID = @business

		ORDER BY Customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_businesscustomer.html', data = data)

# report customer location (mustafa)
@app.route ('/customers/customerlocation-report' , methods = ['GET'])
def customerlocation_report():
    cursor.execute("""
        SELECT 
		Customer.CUSTOMER_ID AS 'Customer ID', 
		Customer.C_FNAME AS 'First Name',
		Customer.C_LNAME AS 'Last Name',
		Customer.C_ADDRESS_LINE1 AS 'Street Name',
		Customer.C_CITY AS 'City',
		STATE.STATE_NAME AS 'State',
		Customer.C_ZIP AS 'Zip Code',
		COUNTRY.COUNTRY_NAME AS 'Country'

		FROM CUSTOMER
		JOIN CUSTOMER_STATE ON CUSTOMER.CUSTOMER_ID = CUSTOMER_STATE.CUSTOMER_ID
		JOIN STATE ON CUSTOMER_STATE.STATE_ID = STATE.STATE_ID
		JOIN COUNTRY ON STATE.COUNTRY_ID = COUNTRY.COUNTRY_ID


		ORDER BY Customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_customerlocation.html', data = data)

# report customer payment type & amount for specific service (mustafa)
@app.route ('/customers/customerpayservice-report' , methods = ['GET'])
def customerpayservice_report():
    cursor.execute("""
        SELECT 
		Customer.CUSTOMER_ID AS 'Customer ID',
		Customer.C_BUSINESS_NAME AS 'Business Name',
		Customer.C_FNAME AS 'Customer First Name',
		Customer.C_LNAME AS 'Customer Last Name',
		INVOICE_PAYMENT.PMT_AMOUNT AS 'Payment Amount',
		PAYMENT.PMT_TYPE AS 'Payment Type',
		SERVICE.SERVICE_TYPE AS 'Service Type'


		FROM Customer
		JOIN SERVICE_ORDER ON Customer.CUSTOMER_ID = SERVICE_ORDER.CUSTOMER_ID
		JOIN INVOICE ON SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID
		JOIN INVOICE_PAYMENT ON INVOICE.INVOICE_ID = INVOICE_PAYMENT.INVOICE_ID AND INVOICE.SERVICE_ORDER_ID = INVOICE_PAYMENT.SERVICE_ORDER_ID
		JOIN PAYMENT ON INVOICE_PAYMENT.PMT_ID=PAYMENT.PMT_ID
		JOIN SERVICE_LINE ON SERVICE_ORDER.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
		JOIN SERVICE ON SERVICE_LINE.SERVICE_ID=SERVICE.SERVICE_ID

		order by [CUSTOMER ID];
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_customerpayservice.html', data = data)

################################### VEHICLES ##################################################
@app.route('/vehicles', methods = ['GET']) 
def vehicles():
    return render_template('vehicles.html')

@app.route ('/vehicles/new-vehicle', methods = ['POST', 'GET'])#FINISHED
def new_vehicle():
    # dropdowns
    ###
    cursor.execute("""
        SELECT MAKE.MAKE_NAME, MODEL.MODEL_NAME
        FROM MAKE
        JOIN MODEL
        ON MAKE.MAKE_ID = MODEL.MAKE_ID;
    """)
    #https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
    #https://stackoverflow.com/questions/18351921/how-to-populate-a-cascading-dropdown-with-jquery
    # create json for jquery
    data = {}
    for (make, model) in cursor:
        data.setdefault(make, []).append(model)
    #####################
    sql = "SELECT MAKE_ID, MAKE_NAME FROM MAKE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    makes = []
    for make in rows:
        makes.append(make[1])
    sql = "SELECT CONDITION_ID, CONDITION FROM VEHICLE_CONDITION"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conditions = []
    for condition in rows:
        conditions.append(condition)
    sql = "SELECT CUSTOMER_ID, C_FNAME, C_LNAME FROM Customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    customers = []
    for customer in rows:
        customers.append(customer)
    sql = "SELECT INSURANCE_ID, INSURANCE_NAME FROM INSURANCE_COMPANY"
    cursor.execute(sql)
    rows = cursor.fetchall()
    companies = []
    for company in rows:
        companies.append(company)
    sql = "SELECT POLICY_ID, POLICY_NAME FROM INSURANCE_POLICY"
    cursor.execute(sql)
    rows = cursor.fetchall()
    policies = []
    for policy in rows:
        policies.append(policy)

    if request.method == 'POST':
        vin = request.form.get("vin")
        make = request.form.get("make")
        cursor.execute("SELECT MAKE_ID FROM MAKE WHERE MAKE_NAME = '{}'".format(make))
        make = cursor.fetchone()[0]
        model = request.form.get("model")
        cursor.execute("SELECT MODEL_ID FROM MODEL WHERE MODEL_NAME = '{}'".format(model))
        model = cursor.fetchone()[0]
        year = (request.form.get("year"))
        license_plate = request.form.get("plate")
        color = request.form.get("color")
        active = int(request.form.get("active"))
        if vin is not None:#and make and model and year and license_plate is not None:
            condition_id = request.form.get('condition')
            x1 = condition_id.split(", ")
            cond = int(x1[0][1:])
            # insert vehicle table
            query = "INSERT INTO VEHICLE (V_VIN, MAKE_ID, MODEL_ID, V_YEAR, V_LICENSE_PLATE, V_COLOR, ACTIVE_ID, CONDITION_ID) OUTPUT INSERTED.V_ID VALUES (?,?,?,?,?,?,?,?)"
            vals = (vin, make, model, year, license_plate, color, active, cond)
            cursor.execute(query, vals)
            v_id = cursor.fetchone()[0]
            conn.commit()
            # insert customer_vehicle table
            customer_id = request.form.get('customer')
            x = customer_id.split(", ")
            cust = int(x[0][1:])
            query = "INSERT INTO CUSTOMER_VEHICLE (V_ID, CUSTOMER_ID) VALUES (?,?)"
            vals = (v_id, cust)
            cursor.execute(query, vals)
            conn.commit()
            # insert policy
            date = request.form.get('date')
            policy = request.form.get('policy')
            x2 = condition_id.split(", ")
            pol = int(x2[0][1:])
            company = request.form.get('company')
            x3 = condition_id.split(", ")
            comp = int(x3[0][1:])
            query = "INSERT INTO POLICY (CUSTOMER_ID, V_ID, INSURANCE_ID, POLICY_ID, EXPIRATION_DATE) VALUES (?,?,?,?,?)"
            vals = (cust, v_id, comp, pol, date)
            cursor.execute(query, vals)
            conn.commit()
            return render_template ('newvehicle.html', makes = makes, customers=customers, conditions=conditions, companies = companies, policies = policies, data = data)
    return render_template ('newvehicle.html', makes = makes, customers=customers, conditions=conditions, companies = companies, policies = policies, data = data)

# modify existing vehicle by entering vin
@app.route ('/vehicles/update-vehicle' , methods = ['POST' , 'GET'])
def update_vehicles():
   # send list of customer id's to gui dropdown
    cursor.execute("""
        SELECT V_ID, V_VIN, V_LICENSE_PLATE, MAKE_NAME, MODEL_NAME
        FROM VEHICLE
        JOIN MAKE
        ON VEHICLE.MAKE_ID=MAKE.MAKE_ID
        JOIN MODEL
        ON VEHICLE.MODEL_ID=MODEL.MODEL_ID
    """)
    rows = cursor.fetchall()
    vehicles = []
    for vehicle in rows:
        vehicles.append(vehicle)
    sql = "SELECT MAKE_ID, MAKE_NAME FROM MAKE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    makes = []
    for make in rows:
        #makes.append([x for x in make])
        makes.append(make[1])
    sql = "SELECT MODEL_ID, MODEL_NAME FROM MODEL"
    cursor.execute(sql)
    rows = cursor.fetchall()
    models = []
    for model in rows:
        models.append(model[1])
    sql = "SELECT CONDITION_ID, CONDITION FROM VEHICLE_CONDITION"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conditions = []
    for condition in rows:
        conditions.append(condition[1])
    sql = "SELECT CUSTOMER_ID, C_FNAME, C_LNAME FROM Customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    customers = []
    for customer in rows:
        customers.append(customer[2])
    sql = "SELECT INSURANCE_ID, INSURANCE_NAME FROM INSURANCE_COMPANY"
    cursor.execute(sql)
    rows = cursor.fetchall()
    companies = []
    for company in rows:
        companies.append(company[1])
    sql = "SELECT POLICY_ID, POLICY_NAME FROM INSURANCE_POLICY"
    cursor.execute(sql)
    rows = cursor.fetchall()
    policies = []
    for policy in rows:
        policies.append(policy[1])
    sql = "SELECT ACTIVE_ID, ACTIVE_NAME FROM VEHICLE_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    statuses = []
    for status in rows:
        statuses.append(status[1])
    ####################################################
    if request.method == 'POST':
        # convert customer id to int for sql statement
        v_id = request.form.get('vehicle')
        x = v_id.split(", ")
        y = int(x[0][1:])
        # get table, column, and new value data
        field = request.form.get('tblname')
        value = request.form.get('value')
        if field == "VEHICLE SET MAKE_ID":
            value = request.form.get('make')
            cursor.execute("SELECT MAKE_ID FROM MAKE WHERE MAKE_NAME = '{}'".format(value))
            make = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (make, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "VEHICLE SET MODEL_ID":
            value = request.form.get('model')
            cursor.execute("SELECT MODEL_ID FROM MODEL WHERE MODEL_NAME = '{}'".format(value))
            model = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (model, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "VEHICLE SET CONDITION_ID":
            value = request.form.get('condition')
            cursor.execute("SELECT CONDITION_ID FROM VEHICLE_CONDITION WHERE CONDITION = '{}'".format(value))
            condition = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (condition, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "CUSTOMER_VEHICLE SET CUSTOMER_ID": # FIXME
            value = request.form.get('customer')
            cursor.execute("SELECT CUSTOMER_ID FROM CUSTOMER_VEHICLE WHERE CUSTOMER_LNAME = '{}'".format(value))
            customer = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (customer, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "VEHICLE SET ACTIVE_ID":
            value = request.form.get('status')
            cursor.execute("SELECT ACTIVE_ID FROM VEHICLE_STATUS WHERE ACTIVE_NAME = '{}'".format(value))
            status = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (status, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "POLICY SET INSURANCE_ID":
            value = request.form.get('company')
            cursor.execute("SELECT INSURANCE_ID FROM INSURANCE_COMPANY WHERE INSURANCE_NAME = '{}'".format(value))
            company = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (company, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        if field == "POLICY SET POLICY_ID":
            value = request.form.get('policy')
            cursor.execute("SELECT POLICY_ID FROM INSURANCE_POLICY WHERE POLICY_NAME = '{}'".format(value))
            policy = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (policy, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
        else:
            sql = "UPDATE {} = ? WHERE V_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)
    return render_template('updatevehicle.html', vehicles=vehicles,makes=makes,models=models,customers=customers, conditions=conditions, companies = companies, policies = policies,statuses=statuses)

# remove vehicle from db by setting status to inactive  
@app.route ('/vehicles/delete-vehicle' , methods =['POST' , 'GET']) #FINISHED
def delete_vehicle():
    cursor.execute("""
        SELECT V_ID, V_VIN, V_LICENSE_PLATE, MAKE_NAME, MODEL_NAME
        FROM VEHICLE
        JOIN MAKE
        ON VEHICLE.MAKE_ID=MAKE.MAKE_ID
        JOIN MODEL
        ON VEHICLE.MODEL_ID=MODEL.MODEL_ID
    """)
    rows = cursor.fetchall()
    vehicles = []
    for vehicle in rows:
        vehicles.append(vehicle)
    if request.method == 'POST':
        vehicle_id = request.form.get('vehicle')
        x = vehicle_id.split(", ")
        y = int(x[0][1:])
        sql = "UPDATE Vehicle SET ACTIVE_ID = 2 WHERE V_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Vehicle removed sucessfully'
        return render_template('deletevehicle.html', vehicles = vehicles, message = message)
    return render_template('deletevehicle.html', vehicles = vehicles)

#view all vehicles
@app.route ('/vehicles/view-vehicles' , methods = ['GET'])#FINISHED
def view_vehicles():
    cursor.execute ("""
        SELECT VEHICLE.V_ID, VEHICLE.V_VIN, VEHICLE.V_LICENSE_PLATE, VEHICLE.V_YEAR, MAKE.MAKE_NAME, 
        MODEL.MODEL_NAME, VEHICLE.V_COLOR, VEHICLE_CONDITION.CONDITION, VEHICLE_STATUS.ACTIVE_NAME, 
        INSURANCE_COMPANY.INSURANCE_NAME,INSURANCE_POLICY.POLICY_NAME, POLICY.EXPIRATION_DATE
        FROM VEHICLE
        JOIN VEHICLE_STATUS
        ON VEHICLE.ACTIVE_ID = VEHICLE_STATUS.ACTIVE_ID
        JOIN VEHICLE_CONDITION
        ON VEHICLE.CONDITION_ID = VEHICLE_CONDITION.CONDITION_ID
        JOIN MAKE
        ON VEHICLE.MAKE_ID=MAKE.MAKE_ID
        JOIN MODEL
        ON VEHICLE.MODEL_ID=MODEL.MODEL_ID
        JOIN POLICY
        ON VEHICLE.V_ID=POLICY.V_ID
        JOIN INSURANCE_COMPANY
        ON POLICY.INSURANCE_ID=INSURANCE_COMPANY.INSURANCE_ID
        JOIN INSURANCE_POLICY
        ON POLICY.POLICY_ID=INSURANCE_POLICY.POLICY_ID
    """)
    data = cursor.fetchall()
    return render_template ('viewvehicles.html' , data = data)
## vehicle part report 
@app.route('/vehicles/vehiclepart-report', methods = ['GET']) 
def vehicle_part_report():
    cursor.execute("""
        SELECT VEHICLE.V_VIN AS 'VIN', VEHICLE.V_YEAR AS 'Year', MAKE.MAKE_NAME AS 'Make', 
        MODEL.MODEL_NAME AS 'Model', SERVICE.SERVICE_TYPE AS 'Service', SUPPLIER.SUPPLIER_NAME AS 'Supplier', PART.PART_NAME AS 'Part'

        FROM VEHICLE
        JOIN VEHICLE_SERVICE
        ON VEHICLE.V_ID = VEHICLE_SERVICE.V_ID
        JOIN MAKE
        ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
        JOIN MODEL
        ON VEHICLE.MODEL_ID = MODEL.MODEL_ID
        JOIN SERVICE
        ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
        JOIN SERVICE_LINE
        ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
        JOIN SERVICE_LINE_PART
        ON  SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_LINE_PART.SERVICE_ORDER_ID AND SERVICE_LINE.SERVICE_ID = SERVICE_LINE_PART.SERVICE_ID
        JOIN PART
        ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
        JOIN SUPPLIER_PART
        ON PART.PART_ID = SUPPLIER_PART.PART_ID
        JOIN SUPPLIER
        ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

        ORDER BY SERVICE.SERVICE_TYPE, PART.PART_NAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_vehiclepart.html', data = data)

## customer vheicle status report 
@app.route('/vehicles/CustomerVehicleStatusReport', methods = ['GET']) 
def customer_vehicle_status_report():
    cursor.execute("""
        SELECT 
        Customer.CUSTOMER_ID AS "ID",
        Customer.C_FNAME AS "First Name",
        Customer.C_LNAME AS "Last Name",
        VEHICLE.V_VIN AS"VEHICLE VIN" , 
        VEHICLE.V_MAKE AS "MAKE",
        VEHICLE.V_MODEL AS "MODEL",
        VEHICLE.V_YEAR AS "YEAR",
        VEHICLE_STATUS.ACTIVE AS "STATUS"


        FROM Customer 
        JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
        JOIN VEHICLE ON CUSTOMER_VEHICLE.V_VIN = VEHICLE.V_VIN
        JOIN VEHICLE_STATUS ON VEHICLE.V_VIN = VEHICLE_STATUS.V_VIN

        ORDER BY VEHICLE_STATUS.ACTIVE
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_CustomerVehicleStatusReport.html', data = data)

#### VEHICLE SERVICE REPORT #####
@app.route('/vehicles/vehicleservice-report', methods = ['GET']) 
def view_service_report():
    cursor.execute("""
        SELECT
        VEHICLE.V_VIN AS "Vehicle Vin",
        CUSTOMER.C_FNAME AS "First Name",
        CUSTOMER.C_LNAME AS "Last Name",
        SERVICE.SERVICE_ID AS "Service ID",
        SERVICE.SERVICE_TYPE AS "Service Type",
        SERVICE_STATUS.ACTIVE AS "Service Status"

        FROM VEHICLE
        JOIN VEHICLE_SERVICE
        ON VEHICLE.V_VIN = VEHICLE_SERVICE.V_VIN
        JOIN SERVICE
        ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
        JOIN SERVICE_STATUS
        ON SERVICE.SERVICE_ID = SERVICE_STATUS.SERVICE_ID
        JOIN CUSTOMER_VEHICLE
        ON VEHICLE.V_VIN = CUSTOMER_VEHICLE.V_VIN
        JOIN CUSTOMER
        ON CUSTOMER_VEHICLE.CUSTOMER_ID = CUSTOMER.CUSTOMER_ID

        ORDER BY SERVICE_STATUS.ACTIVE;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('viewCustomers.html', data = data)

# report active & inactive insurance (jahidul)
@app.route ('/vehicles/activeinactivepolicy-report' , methods = ['GET'])
def activeinactivepolicy_report():
    cursor.execute("""
        SELECT CV.Customer_id AS "Customer id", V.V_VIN AS 'Vehicle VIN',
		IP.Policy_name as 'Policy name',
		Case when VP.EXPIRATION_DATE<GETDATE() then 'Inactive' else 'Active' end As 'Policy Status',
		VP.EXPIRATION_DATE As 'Expire in this day'
		
		FROM Vehicle V
		JOIN Vehicle_STATUS VS
		ON V.ACTIVE_ID = VS.ACTIVE_ID
		JOIN CUSTOMER_Vehicle CV
		ON CV.V_ID = V.V_ID
		JOIN Policy VP
		ON V.V_ID = VP.V_ID
		JOIN INSURANCE_POLICY IP
		ON VP.POLICY_ID= IP.POLICY_ID
		
		WHERE VS.ACTIVE_ID in (1,2)
		ORDER BY 4;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_activeinactivepolicy.html', data = data)

# report customer vehicles state (kyle)
@app.route ('/vehicles/vehiclestate-report' , methods = ['GET'])
def vehiclestate_report():
    cursor.execute("""
        SELECT
		Customer.CUSTOMER_ID AS "Customer ID",
		Customer.C_FNAME AS 'First Name',
		Customer.C_LNAME AS 'Last Name',
		STATE.STATE_NAME AS 'STATE',
		CUSTOMER_VEHICLE.V_VIN AS 'VIN',
		MAKE.MAKE_NAME AS 'Make',
		MODEL.MODEL_NAME AS 'Model',
		VEHICLE.V_YEAR AS 'Year',
		VEHICLE.V_LICENSE_PLATE AS 'License Plate'

		FROM Customer
		JOIN CUSTOMER_STATE
		ON Customer.CUSTOMER_ID = CUSTOMER_STATE.CUSTOMER_ID
		JOIN STATE
		ON CUSTOMER_STATE.STATE_ID = STATE.STATE_ID
		JOIN CUSTOMER_VEHICLE
		ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
		JOIN VEHICLE
		ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID
		JOIN MAKE
		ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
		JOIN MODEL
		ON VEHICLE.MODEL_ID = MODEL.MODEL_ID

		ORDER BY CUSTOMER_CONTACT_INFO.STATE_NAME, Customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_vehiclestate.html', data = data)
	
# report vehicle insurance (jerry)
@app.route ('/vehicles/vehicleinsurance-report' , methods = ['GET'])
def vehicleinsurance_report():
    cursor.execute("""
        SELECT
		VEHICLE.V_VIN AS 'VIN',
		CUSTOMER.C_LNAME AS 'Customer First Name',
		CUSTOMER.C_FNAME AS 'Customer Last Name',
		MAKE.MAKE_NAME AS 'Make',
		MODEL.MODEL_NAME AS 'Model',
		VEHICLE.V_YEAR AS 'Year',
		INSURANCE_COMPANY.INSURANCE_NAME AS 'Insurance',
		INSURANCE_COMPANY.I_PHONE AS 'Insurance Phone Number'

		FROM VEHICLE
		JOIN POLICY
		ON VEHICLE.V_ID = POLICY.V_ID
		JOIN INSURANCE_COMPANY
		ON POLICY.INSURANCE_ID = INSURANCE_COMPANY.INSURANCE_ID
		JOIN CUSTOMER
		ON POLICY.CUSTOMER_ID = CUSTOMER.CUSTOMER_ID
		JOIN MAKE
		ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
		JOIN MODEL
		ON VEHICLE.MODEL_ID = MODEL.MODEL_ID
		JOIN VEHICLE_STATUS
		ON VEHICLE.ACTIVE_ID = VEHICLE_STATUS.ACTIVE_ID

		WHERE VEHICLE_STATUS.ACTIVE_ID = 1 OR VEHICLE_STATUS.ACTIVE_ID = 3
		ORDER BY CUSTOMER.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_vehicleinsurance.html', data = data)

# report customer vehicle condition at shop (mustafa)
@app.route ('/vehicles/vehiclecondition-report' , methods = ['GET'])
def vehiclecondition_report():
    cursor.execute("""
        SELECT 
		Customer.CUSTOMER_ID AS 'Customer ID', 
		VEHICLE.V_ID AS 'Vehicle ID',
		MAKE.MAKE_NAME AS 'Vehicle Make',
		MODEL.MODEL_NAME AS 'Vehicle Model',
		VEHICLE.V_YEAR AS 'Vehicle Year',
		VEHICLE_CONDITION.CONDITION AS 'Vehicle Condition Upon Arrival'

		FROM Customer 
		JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
		JOIN VEHICLE ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID
		JOIN VEHICLE_CONDITION ON VEHICLE.CONDITION_ID = VEHICLE_CONDITION.CONDITION_ID
		JOIN MAKE ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
		JOIN MODEL ON VEHICLE.MODEL_ID = MODEL.MODEL_ID
		
		order by customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_vehiclecondition.html', data = data)

# report customer vehicle status (mustafa)
@app.route ('/vehicles/vehiclestatus-report' , methods = ['GET'])
def vehiclestatus_report():
    cursor.execute("""
        SELECT 
		Customer.CUSTOMER_ID AS 'Customer ID',
		Customer.C_FNAME AS 'First Name',
		Customer.C_LNAME AS 'Last Name',
		VEHICLE.V_ID AS 'Vehicle ID', 
		MAKE.MAKE_NAME AS 'Make',
		MODEL.MODEL_NAME AS 'Model',
		VEHICLE.V_YEAR AS 'Year',
		VEHICLE_STATUS.ACTIVE_NAME AS 'Status',
		SERVICE.SERVICE_TYPE AS 'Service Being/ Have Been/ Or Will Be Done'

		FROM Customer 
		JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
		JOIN VEHICLE ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID
		JOIN VEHICLE_STATUS ON VEHICLE.Active_ID = VEHICLE_STATUS.Active_ID
		JOIN VEHICLE_SERVICE ON VEHICLE.V_ID = VEHICLE_SERVICE.V_ID
		JOIN SERVICE ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
		JOIN MAKE ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
		JOIN MODEL ON VEHICLE.MODEL_ID = MODEL.MODEL_ID

		ORDER BY [Customer ID];
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_vehiclestatus.html', data = data)

################################### EMPLOYEES ##################################################
@app.route('/employees', methods = ['GET']) 
def employees():
    return render_template('employees.html')

# Employee insert/create FINISHED @anthony
@app.route ('/employees/new-employee', methods = ['POST', 'GET'])
def new_employee():
    sql = "SELECT ACTIVE_NAME FROM EMPLOYEE_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    actives = []
    for active in rows:
        actives.append(active[0])
    sql = "SELECT ROLE_NAME FROM ROLE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    roles = []
    for role in rows:
        roles.append(role[0])
    if request.method == 'POST':
        lname = request.form.get("lname")
        fname = request.form.get("fname")
        role = request.form.get("role")
        active = request.form.get("active")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("addy1")
        address2 = request.form.get("addy2")
        zip_code = request.form.get("zip")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        if lname and fname is not None:   
            cursor.execute("SELECT ROLE_ID FROM ROLE WHERE ROLE_NAME = '{}'".format(role))
            role = cursor.fetchone()[0]
            cursor.execute("SELECT ACTIVE_ID FROM EMPLOYEE_STATUS WHERE ACTIVE_NAME = '{}'".format(active))
            active = cursor.fetchone()[0]
            # new employee default
            query = "INSERT INTO EMPLOYEE (EMPLOYEE_LNAME, EMPLOYEE_FNAME, ROLE_ID, ACTIVE_ID, E_ADDRESS_LINE1, E_ADDRESS_LINE2, E_CITY, E_STATE, E_ZIP, E_COUNTRY, E_PHONE, E_EMAIL) OUTPUT INSERTED.EMPLOYEE_ID VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
            vals = (lname, fname, role, active, address, address2, city, state, zip_code, country, phone, email)
            cursor.execute(query, vals)
            conn.commit()
            return render_template ('employees.html')
    return render_template ('newemployee.html',roles=roles,actives=actives)
    
# ask for help here
# modify existing employee by entering id
@app.route ('/employees/update-employee' , methods = ['POST' , 'GET'])
def update_employee():
    cursor.execute("SELECT EMPLOYEE_ID, EMPLOYEE_FNAME, EMPLOYEE_LNAME FROM Employee")
    rows = cursor.fetchall()
    employees = []
    for employee in rows:
        employees.append(employee)
    sql = "SELECT ACTIVE_ID, ACTIVE_NAME FROM EMPLOYEE_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    statuses = []
    for status in rows:
        statuses.append(status[1])
    sql = "SELECT ROLE_NAME FROM ROLE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    roles = []
    for role in rows:
        roles.append(role[0])
    if request.method == 'POST':
        employee_id = request.form.get ('employee')
        print(employee_id)
        x = employee_id.split(", ")
        y = int (x[0][1:])
        field = request.form.get('tblname')
        value = request.form.get('value')
        if field == "EMPLOYEE SET ACTIVE_ID":
            value = request.form.get('status')
            cursor.execute("SELECT ACTIVE_ID FROM EMPLOYEE_STATUS WHERE ACTIVE_NAME = '{}'".format(value))
            status = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE EMPLOYEE_ID = ?".format(field)
            vals = (status, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('employees.html')
        if field == "EMPLOYEE SET ROLE_ID":
            value = request.form.get('role')
            print(value)
            cursor.execute("SELECT ROLE_ID FROM ROLE WHERE ROLE_NAME = '{}'".format(value))
            role = cursor.fetchone()[0]
            print(role)
            sql = "UPDATE {} = ? WHERE EMPLOYEE_ID = ?".format(field)
            vals = (role, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('employees.html')
        else: 
            sql = "UPDATE {} = ? WHERE EMPLOYEE_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('suppliers.html')
    return render_template ('updateemployee.html', employees=employees,statuses=statuses,roles=roles)
    
                
# remove employee from db by setting status to inactive
@app.route ('/employees/delete-employee' , methods =['POST' , 'GET'])
def delete_employee():
    sql = "SELECT EMPLOYEE_ID, EMPLOYEE_FNAME, EMPLOYEE_LNAME FROM Employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    employees = []
    for employee in rows:
        employees.append(employee)
    if request.method == 'POST':
        employee_id = request.form.get('employee')
        print(employee_id)
        x = employee_id.split(", ")
        y = int(x[0][1:])
        print(y)
        sql = "UPDATE EMPLOYEE SET ACTIVE_ID = 4 WHERE EMPLOYEE_ID = ?"
        vals = y
        cursor.execute(sql, vals)
        conn.commit()
        return render_template('employees.html')
    return render_template('deleteemployee.html', employees = employees)
           

#view all employees
@app.route ('/employees/view-employees' , methods = ['GET'])
def view_employees():
    cursor.execute ("""
        SELECT EMPLOYEE_ID, EMPLOYEE_FNAME, EMPLOYEE_LNAME, ROLE.ROLE_NAME,
        EMPLOYEE_STATUS.ACTIVE_NAME, E_ADDRESS_LINE1, E_ADDRESS_LINE2, E_CITY,
        E_STATE, E_ZIP, E_COUNTRY, E_PHONE, E_EMAIL
        FROM Employee
        JOIN EMPLOYEE_STATUS
        ON EMPLOYEE_STATUS.ACTIVE_ID=EMPLOYEE.ACTIVE_ID
        JOIN ROLE
        ON ROLE.ROLE_ID=EMPLOYEE.ROLE_ID
    """)
    data = cursor.fetchall()
    return render_template ('viewemployee.html' , data = data)

# employee part report
@app.route ('/employees/employeepart-report' , methods = ['GET'])
def employee_part_report():
    cursor.execute("""
        SELECT SUPPLIER.SUPPLIER_NAME AS 'Supplier', PART.PART_NAME AS 'Part', EMPLOYEE.EMPLOYEE_ID AS 'Employee ID', 
        EMPLOYEE.EMPLOYEE_LNAME AS 'Last Name', EMPLOYEE.EMPLOYEE_FNAME AS 'First Name', COUNT(PART.PART_ID) AS 'Part Amount'

        FROM EMPLOYEE
        JOIN Employee_Status
        ON Employee_Status.ACTIVE_ID = EMPLOYEE.ACTIVE_ID
        JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
        ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
        JOIN SERVICE_LINE
        ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID AND EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ID = SERVICE_LINE.SERVICE_ID
        JOIN SERVICE_LINE_PART
        ON SERVICE_LINE_PART.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID AND SERVICE_LINE_PART.SERVICE_ID = SERVICE_LINE.SERVICE_ID
        JOIN PART
        ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
        JOIN SUPPLIER_PART
        ON PART.PART_ID = SUPPLIER_PART.PART_ID
        JOIN SUPPLIER
        ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

        WHERE Employee_Status.ACTIVE_ID = 1
        GROUP BY SUPPLIER.SUPPLIER_NAME, PART.PART_NAME, EMPLOYEE.EMPLOYEE_ID,EMPLOYEE.EMPLOYEE_LNAME, EMPLOYEE.EMPLOYEE_FNAME
        ORDER BY PART.PART_NAME, EMPLOYEE_LNAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeepart.html', data = data)



### EMPLOYEE STATUS ####
@app.route ('/employees/employeestatus-report' , methods = ['GET'])
def employeestatus_report():
    cursor.execute("""
        SELECT 
        EMPLOYEE.EMPLOYEE_ID AS "Employee ID",
        EMPLOYEE.EMPLOYEE_FNAME AS "First Name",
        EMPLOYEE.EMPLOYEE_LNAME AS "Last Name",
        EMPLOYEE_LOOKUP.EMPLOYEE_CURR_SERVICE AS "Employee Current Service",
        EMPLOYEE_STATUS.ACTIVE AS "Employee Status"

        FROM EMPLOYEE
        JOIN EMPLOYEE_STATUS
        ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_STATUS.EMPLOYEE_ID
        JOIN EMPLOYEE_LOOKUP
        ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_LOOKUP.EMPLOYEE_ID

        ORDER BY EMPLOYEE_STATUS.ACTIVE;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeestatus.html', data = data)
    
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeestatus.html', data = data)

# employee by service (jerry)
@app.route ('/employees/employeeservice-report' , methods = ['GET'])
def employeeservice_report():
    cursor.execute("""
        SELECT
		EMPLOYEE.EMP_FNAME AS 'First Name',
		EMPLOYEE.EMP_LNAME AS 'Last Name',
		SERVICE_ORDER.SERVICE_ORDER_ID AS 'Service Order ID',
		SERVICE.SERVICE_TYPE AS 'Service',
		SERVICE_ORDER.ORDER_DATE AS 'Order Date'

		FROM EMPLOYEE
		JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
		ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
		JOIN SERVICE_LINE
		ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
		JOIN SERVICE_ORDER
		ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
		JOIN SERVICE_ORDER_STATUS
		ON SERVICE_ORDER.ACTIVE_ID = SERVICE_ORDER_STATUS.ACTIVE_ID
		JOIN SERVICE
		ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID

		WHERE SERVICE_ORDER.ACTIVE_ID = 1 OR SERVICE_ORDER.ACTIVE_ID = 3
		ORDER BY SERVICE_ORDER.ORDER_DATE;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeeservice.html', data = data)
	
# report employee service order assignment (kyle)
@app.route ('/employees/empservorderassign-report' , methods = ['GET'])
def empservorderassign_report():
    cursor.execute("""
        SELECT
		EMPLOYEE.EMPLOYEE_ID AS 'Employee ID',
		EMPLOYEE.EMPLOYEE_LNAME AS 'Last Name',
		EMPLOYEE.EMPLOYEE_FNAME AS 'First Name',
		ROLE.ROLE_NAME AS 'Role',
		SERVICE.SERVICE_TYPE AS 'Service',
		SERVICE_ORDER.SERVICE_ORDER_ID AS 'Order ID',
		SERVICE_ORDER.ORDER_DATE AS 'Order Date'

		FROM EMPLOYEE
		JOIN ROLE
		ON EMPLOYEE.ROLE_ID = ROLE.ROLE_ID
		JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
		ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
		JOIN SERVICE_LINE
		ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
		JOIN SERVICE
		ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID
		JOIN SERVICE_ORDER
		ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID

		WHERE EMPLOYEE.ACTIVE_ID = 1 OR EMPLOYEE.ACTIVE_ID = 3
		ORDER BY EMPLOYEE.EMPLOYEE_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_empservorderassign.html', data = data)
	
# report employee role (maddy)
@app.route ('/employees/employeerole-report' , methods = ['GET'])
def employeerole_report():
    cursor.execute("""
        SELECT DISTINCT
		Employee.EMPLOYEE_ID AS 'Employee ID',
		Employee.EMPLOYEE_LNAME AS 'Employee Last Name',
		Employee.EMPLOYEE_FNAME AS 'Employee First Name',
		Role.ROLE_NAME AS 'Role',
		Employee_Status.Active_Name AS 'Active Status'

		FROM EMPLOYEE
		JOIN ROLE ON EMPLOYEE.ROLE_ID = ROLE.ROLE_ID
		JOIN EMPLOYEE_STATUS ON EMPLOYEE.ACTIVE_ID = EMPLOYEE_STATUS.ACTIVE_ID
		JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID

		ORDER BY Role.ROLE_NAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeerole.html', data = data)

################################### SERVICES ##################################################
@app.route('/services', methods = ['GET']) 
def services():
    return render_template('services.html')

@app.route('/services/view-services', methods = ['GET'])
def view_services():
    cursor.execute ("SELECT * FROM CoogTechSolutions.dbo.SERVICE")
    data = cursor.fetchall()
    return render_template ('viewservices.html' , data = data)

# add service deafult
# Not finish dont know how to add service line
@app.route('/services/new-service', methods = ['POST', 'GET'])
def new_service():
    message = ''
    if request.method == 'POST':
        sertype = request.form.get("sertype")
        cost = request.form.get("cost")
        active = request.form.get("active")
        if sertype and cost is not None:
            # default service
            query = "INSERT INTO Service (SERVICE_TYPE, COST, ACTIVE_ID) OUTPUT INSERTED.SERVICE_ID VALUES (?, ?, ?)"
            vals = (sertype, cost, active)
            data = cursor.execute(query, vals)
            service_id = cursor.fetchone()[0]
            conn.commit()
            
            
# add service line 
           
# add service order 
            
# add invoice 
            
# modify service
@app.route('/service/upate', methods = ['POST', 'GET'])
def update_service():
    sql = "SELECT SERVICE_ID, SERVICE_TYPE, COST, ACTIVE_ID FROM Service"
    cursor.execute(sql)
    rows = cursor.fetchall()
    services = []
    for service in rows:
        services.append(service)
    if request.method == 'POST':
        service_id = request.form.get('service')
        print(service_id)
        x = service_id.split(", ")
        y = int(x[0][1:])
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE SERVICE_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service edited sucessfully' 
        return render_template('updateservice.html', services = services, message = message)   
    return render_template('updateservice.html', services = services)

# modify service line
@app.route('/service/upate-serviceline', methods = ['POST', 'GET'])
def update_serviceline():
    sql = "SELECT SERVICE_ORDER_ID, SERVICE_ID, QUANTITY, LINE_COST, ACTIVE_ID FROM service_line"
    cursor.execute(sql)
    rows = cursor.fetchall()
    servicelines = []
    for serviceline in rows:
        servicelines.append(serviceline)
    if request.method == 'POST':
        serviceline_id = request.form.get('serviceline')
        print(serviceline_id)
        x = serviceline_id.split(", ")
        y = int(x[0][1:])
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE SERVICE_ORDER_ID = ?, SERVICE_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service line edited sucessfully' 
        return render_template('updateserviceline.html', servicelines = servicelines, message = message)   
    return render_template('updateserviceline.html', servicelines = servicelines)


# modify service order
@app.route('/service/upate-serviceorder', methods = ['POST', 'GET'])
def update_serviceorder():
    sql = "SELECT SERVICE_ORDER_ID, CUSTOMER_ID, ORDER_DATE, ACTIVE_ID FROM service_order"
    cursor.execute(sql)
    rows = cursor.fetchall()
    serviceorders = []
    for serviceorder in rows:
        serviceorders.append(serviceorder)
    if request.method == 'POST':
        serviceorder_id = request.form.get('serviceorder')
        print(serviceorder_id)
        x = serviceorder_id.split(", ")
        y = int(x[0][1:])
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE SERVICE_ORDER_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service order edited sucessfully' 
        return render_template('updateserviceorder.html', serviceorders = serviceorders, message = message)   
    return render_template('updateserviceorder.html', serviceorders = serviceorders)

# modify invoice 
@app.route('/service/upate-invoice', methods = ['POST', 'GET'])
def update_invoice():
    sql = "SELECT INVOICE_ID, SERVICE_ORDER_ID, TOTAL_COST, INVOICE_DATE, AMT_OWNED, ACTIVE_ID FROM Invoice"
    cursor.execute(sql)
    rows = cursor.fetchall()
    invoices = []
    for invoice in rows:
        invoices.append(invoice)
    if request.method == 'POST':
        invoice_id = request.form.get('invoice')
        print(invoice_id)
        x = invoice_id.split(", ")
        y = int(x[0][1:])
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE INVOICE_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Invoice edited sucessfully' 
        return render_template('updateinvoice.html', invoices = invoices, message = message)   
    return render_template('updateinvoice.html', invoices = invoices)
        
        

# remove service from db by settiing status to inactive
@app.route('/services/delete-service', methods = ['POST', 'GET'])
def delete_sevice():
    
    sql = "SELECT SERVICE_ID, SERVICE_TYPE FROM Service"
    cursor.execute(sql)
    row = cursor.fetchall()
    service = []
    for service in rows:
        services.append(service)
    if request.method == 'POST':
        
        service_id = request.form.get('service')
        print(employee_id)
        x = service_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE Service SET ACTIVE_ID = 2 WHERE SERVICE_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service removed sucessfully'
        return render_template('deleteservice.html', services = services, message = message)
        
    return render_template('deleteservice.html', services = services)

# Service line delete to inactive
@app.route('/services/delete-serviceline', methods = ['POST', 'GET'])
def delete_serviceline():
    
    sql = "SELECT SERVICE_ORDER_ID, SERVICE_ID, QUANTITY, LINE_COST FROM service_line"
    cursor.execute(sql)
    row = cursor.fetchall()
    servicelines = []
    for serviceline in rows:
        servicelines.append(serviceline)
    if request.method == 'POST':
        
        serviceline_id = request.form.get('serviceline')
        print(serviceline_id)
        x = serviceline_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE service_line SET ACTIVE_ID = 2 WHERE SERVICE_ORDER_ID = ?, SERVICE_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service line removed sucessfully'
        return render_template('updateserviceline.html', servicelines = servicelines, message = message)
        
    return render_template('updateserviceline.html', servicelines = servicelines)

# Service Order delete to inactive
@app.route('/services/delete-serviceorder', methods = ['POST', 'GET'])
def delete_serviceorder():
    
    sql = "SELECT SERVICE_ORDER_ID, ORDER_DATE FROM service_order"
    cursor.execute(sql)
    row = cursor.fetchall()
    serviceorders = []
    for serviceorder in rows:
        serviceorders.append(serviceline)
    if request.method == 'POST':
        
        serviceorder_id = request.form.get('serviceorder')
        print(serviceorder_id)
        x = serviceorder_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE service_order SET ACTIVE_ID = 2 WHERE SERVICE_ORDER_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Service order removed sucessfully'
        return render_template('updateserviceorder.html', serviceorders = serviceorders, message = message)
        
    return render_template('updateserviceorder.html', serviceorders = serviceorders)

# Invoice delete to inactive
@app.route('/services/delete-invoice', methods = ['POST', 'GET'])
def delete_invoice():
    
    sql = "SELECT INVOICE_ID, TOTAL_COST, INVOICE_DATE FROM Invoice"
    cursor.execute(sql)
    row = cursor.fetchall()
    invoices = []
    for invoice in rows:
        invoices.append(invoice)
    if request.method == 'POST':
        
        invoice_id = request.form.get('invoice')
        print(invoice_id)
        x = invoice_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE Invoice SET ACTIVE_ID = 2 WHERE INVOICE_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Invoice removed sucessfully'
        return render_template('updateinvoice.html', invoices = invoices, message = message)
        
    return render_template('updateinvoice.html', invoices = invoices)

@app.route ('/services/revenue-report' , methods = ['GET'])
def revenue_report():
    cursor.execute("""
        SELECT Customer.CUSTOMER_ID AS 'Customer ID', Customer.C_LNAME AS 'Last Name', Customer.C_FNAME AS 'First Name',
        ACCOUNT_REVENUE.REVENUE_NAME AS 'Revenue Name', SERVICE.SERVICE_TYPE AS 'Service NameE',  SERVICE.COST AS 'Cost',
        PAYMENT_REVENUE.REVENUE_VALUE AS 'Revenue Value'

        FROM CUSTOMER
        JOIN SERVICE_ORDER
        ON CUSTOMER.CUSTOMER_ID = SERVICE_ORDER.CUSTOMER_ID
        JOIN SERVICE_LINE
        ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
        JOIN SERVICE
        ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
        JOIN INVOICE
        ON SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID
        JOIN INVOICE_PAYMENT
        ON INVOICE.SERVICE_ORDER_ID = INVOICE_PAYMENT.SERVICE_ORDER_ID AND INVOICE.INVOICE_ID = INVOICE_PAYMENT.INVOICE_ID
        JOIN PAYMENT
        ON INVOICE_PAYMENT.PMT_ID = PAYMENT.PMT_ID
        JOIN PAYMENT_REVENUE
        ON INVOICE_PAYMENT.PMT_ID = PAYMENT_REVENUE.PMT_ID AND INVOICE_PAYMENT.INVOICE_ID = PAYMENT_REVENUE.INVOICE_ID AND INVOICE_PAYMENT.SERVICE_ORDER_ID = PAYMENT_REVENUE.SERVICE_ORDER_ID
        JOIN ACCOUNT_REVENUE
        ON PAYMENT_REVENUE.REVENUE_ID = ACCOUNT_REVENUE.REVENUE_ID

        ORDER BY INVOICE.INVOICE_DATE;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_revenue.html', data = data)

# report monthly total service order (jahidul)
@app.route ('/services/monthlytotalserviceorder-report' , methods = ['GET'])
def monthlytotalserviceorder_report():
    cursor.execute("""
        SELECT
		count(SERVICE_ORDER.SERVICE_ORDER_ID) AS 'Total Orders',
		FORMAT(SERVICE_ORDER.ORDER_DATE,'MM/yyyy') As 'Month and Year',
		Sum(INVOICE.TOTAL_COST) AS 'Cost',
		INVOICE_STATUS.ACTIVE_NAME AS 'Invoice Status',
		SERVICE_ORDER_STATUS.ACTIVE_NAME As 'Progress Status'
		
		From SERVICE_ORDER
		Join INVOICE
		On SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID
		Join SERVICE_ORDER_STATUS
		On SERVICE_ORDER.ACTIVE_ID = SERVICE_ORDER_STATUS.ACTIVE_ID
		Join INVOICE_STATUS
		On INVOICE_STATUS.ACTIVE_ID = INVOICE.ACTIVE_ID
		
		Where INVOICE_STATUS.ACTIVE_NAME='Fully paid'
		group by INVOICE_STATUS.ACTIVE_NAME, FORMAT(SERVICE_ORDER.ORDER_DATE,'MM/yyyy'),SERVICE_ORDER_STATUS.ACTIVE_NAME
		order by 2;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_monthlytotalserviceorder.html', data = data)
	
# report service active premium customer (kyle)
@app.route ('/services/serviceactivepremcust-report' , methods = ['GET'])
def serviceactivepremcust_report():
    cursor.execute("""
        SELECT
		Customer.CUSTOMER_ID AS 'Customer ID',
		Customer.C_FNAME AS 'First Name',
		Customer.C_LNAME AS 'Last Name',
		Customer.C_BUSINESS_NAME AS 'Business Name',
		SERVICE_ORDER.SERVICE_ORDER_ID AS 'Service ID',
		SERVICE_ORDER.DATE  AS 'Date',
		INVOICE.AMT_OWED AS 'Amount Owed'

		FROM Customer
		JOIN SERVICE_ORDER
		ON Customer.CUSTOMER_ID = SERVICE_ORDER.CUSTOMER_ID
		JOIN INVOICE
		ON SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID

		WHERE CUSTOMER.ACTIVE_ID = 3

		ORDER BY Customer.CUSTOMER_ID;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_serviceactivepremcust.html', data = data)
	
# report repairs (maddy)
@app.route ('/services/repairs-report' , methods = ['GET'])
def repairs_report():
    cursor.execute("""
        DECLARE 
		@serviceRepairs varchar(7),
		@miscRepairs varchar(30)

		SELECT @serviceRepairs = '%REPAIRS%'
		SELECT @miscRepairs = '%REPAIR%'
		SELECT DISTINCT
		Service.SERVICE_ID AS 'Service ID', 
		Service.SERVICE_TYPE AS 'Service Type'

		FROM SERVICE_LINE
		JOIN SERVICE ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID
		JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT ON SERVICE_LINE.SERVICE_ORDER_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ORDER_ID
		JOIN SERVICE_ORDER ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
		JOIN VEHICLE_SERVICE ON SERVICE.SERVICE_ID = VEHICLE_SERVICE.SERVICE_ID

		WHERE Service.SERVICE_TYPE like @serviceRepairs
		OR Service.SERVICE_TYPE like @miscRepairs;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_repairs.html', data = data)

# report service cost (maddy)
@app.route ('/services/servicecost-report' , methods = ['GET'])
def servicecost_report():
    cursor.execute("""
        DECLARE
		@minimumCost float(8)

		SELECT @minimumCost = 1
		SELECT DISTINCT
		Invoice.SERVICE_ORDER_ID AS 'Service Order ID',
		Invoice.TOTAL_COST AS 'Total Cost',
		Invoice.INVOICE_DATE AS 'Invoice Date'

		FROM INVOICE_PAYMENT
		JOIN INVOICE ON INVOICE_PAYMENT.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID AND INVOICE_PAYMENT.INVOICE_ID = INVOICE.INVOICE_ID
		JOIN PAYMENT_STATUS ON INVOICE_PAYMENT.ACTIVE_ID = PAYMENT_STATUS.ACTIVE_ID
		JOIN PAYMENT_REVENUE ON INVOICE_PAYMENT.SERVICE_ORDER_ID = PAYMENT_REVENUE.SERVICE_ORDER_ID
		JOIN PAYMENT ON INVOICE_PAYMENT.PMT_ID = PAYMENT.PMT_ID

		WHERE INVOICE.TOTAL_COST >= @minimumCost

		ORDER BY INVOICE.TOTAL_COST;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_servicecost.html', data = data)

#################################### Suppliers(parts) ###########################################
@app.route('/suppliers', methods = ['GET']) 
def suppliers():
        return render_template('suppliers.html')

@app.route('/suppliers/new-supplierpart', methods = ['POST','GET'])#FINISHED
def new_supplierpart():
    # get info from html
    sql = "SELECT SUPPLIER_ID, SUPPLIER_NAME FROM SUPPLIER"
    cursor.execute(sql)
    rows = cursor.fetchall()
    suppliers = []
    for supplier in rows:
        suppliers.append(supplier[1])
    if request.method == 'POST':
        supplier = request.form.get("supplier")
        part = request.form.get("part")
        cost = request.form.get("cost")
        # get id data
        cursor.execute("SELECT SUPPLIER_ID FROM SUPPLIER WHERE SUPPLIER_NAME = '{}'".format(supplier))
        supplier = cursor.fetchone()[0]
        if supplier and part is not None:
            # insert part
            query = "INSERT INTO PART (PART_NAME) OUTPUT INSERTED.PART_ID VALUES (?)"
            vals = (part)
            data = cursor.execute(query, vals)
            part_id = cursor.fetchone()[0]
            conn.commit()
            # insert supplier_part
            query = "INSERT INTO SUPPLIER_PART (PART_ID, SUPPLIER_ID, PART_COST) VALUES (?,?,?)"
            vals = (part_id, supplier, cost)
            cursor.execute(query, vals)
            conn.commit()
            message = "Item added successfuly"
            return render_template('suppliers.html')
    return render_template('newsupplierpart.html', suppliers=suppliers)

@app.route('/suppliers/new-supplier', methods = ['POST','GET'])#FINISHED
def new_supplier():
    message = ''
    sql = "SELECT ACTIVE_ID, ACTIVE_NAME FROM SUPPLIER_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    actives = []
    for active in rows:
        actives.append(active[1])
    if request.method == 'POST':
        supplier = request.form.get("supplier")
        if supplier is not None:
            # new customer default
            phone = request.form.get("phone")
            email = request.form.get("email")
            address = request.form.get("addy1")
            address2 = request.form.get("addy2")
            zip_code = request.form.get("zip")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            active = request.form.get("active")
            cursor.execute("SELECT ACTIVE_ID FROM SUPPLIER_STATUS WHERE ACTIVE_NAME = '{}'".format(active))
            active = cursor.fetchone()[0]
            query = "INSERT INTO SUPPLIER (SUPPLIER_NAME, ACTIVE_ID, S_ADDRESS_LINE1, S_ADDRESS_LINE2, S_CITY, S_STATE,  S_ZIP, S_COUNTRY, S_PHONE, S_EMAIL) VALUES (?,?,?,?,?,?,?,?,?,?)"
            vals = (supplier, active, address, address2, city, state, zip_code, country, phone, email)
            cursor.execute(query, vals)
            conn.commit()
            message = "New customer entered successfully!"
            return render_template('suppliers.html')
    return render_template('newsupplier.html', actives=actives)

@app.route('/suppliers/update-supplierpart', methods = ['POST','GET'])
def update_supplier():
    # send list of customer id's to gui dropdown
    cursor.execute("SELECT SUPPLIER_ID, SUPPLIER_NAME FROM SUPPLIER")
    rows = cursor.fetchall()
    suppliers = []
    for supplier in rows:
        suppliers.append(supplier)
    sql = "SELECT ACTIVE_ID, ACTIVE_NAME FROM SUPPLIER_STATUS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    statuses = []
    for status in rows:
        statuses.append(status[1])
    ####################################################
    if request.method == 'POST':
        # convert customer id to int for sql statement
        supplier_id = request.form.get('supplier')
        x = supplier_id.split(", ")
        y = int(x[0][1:])
        # get table, column, and new value data
        field = request.form.get('tblname')
        value = request.form.get('value')

        if field == "SUPPLIER SET ACTIVE_ID":
            value = request.form.get('status')
            cursor.execute("SELECT ACTIVE_ID FROM SUPPLIER_STATUS WHERE ACTIVE_NAME = '{}'".format(value))
            status = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE SUPPLIER_ID = ?".format(field)
            vals = (status, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('suppliers.html')
        else: 
            sql = "UPDATE {} = ? WHERE SUPPLIER_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('suppliers.html')
    return render_template('updatesupplier.html', suppliers=suppliers,statuses=statuses)


@app.route('/suppliers/delete-supplier',methods = ['POST','GET'])#FINISHED
def delete_supplier():
     # send list of customer id's to gui dropdown
    sql = "SELECT SUPPLIER_ID, SUPPLIER_NAME FROM SUPPLIER"
    cursor.execute(sql)
    rows = cursor.fetchall()
    suppliers = []
    for supplier in rows:
        suppliers.append(supplier[1])
    if request.method == 'POST':
        # convert customer id to int for sql statement
        supplier = request.form.get('supplier')
        if supplier is not None:
            cursor.execute("SELECT SUPPLIER_ID FROM SUPPLIER WHERE SUPPLIER_NAME = '{}'".format(supplier))
            supplier = cursor.fetchone()[0]
            # set inactive partial delete
            sql = "UPDATE SUPPLIER SET ACTIVE_ID = 2 WHERE SUPPLIER_ID = ?"
            vals = (supplier)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('suppliers.html')
    return render_template('deletesupplier.html', suppliers=suppliers)

# view all Suppliers
@app.route('/suppliers/view-suppliers', methods = ['GET']) #FINISHED
def view_suppliers():
    cursor.execute("""
        SELECT SUPPLIER_ID, SUPPLIER_NAME, S_ADDRESS_LINE1, 
        S_ADDRESS_LINE2, S_CITY, S_STATE, S_ZIP,
        S_COUNTRY, S_PHONE, S_EMAIL,  SUPPLIER_STATUS.ACTIVE_NAME

        FROM SUPPLIER
        JOIN SUPPLIER_STATUS
        ON SUPPLIER.ACTIVE_ID = SUPPLIER_STATUS.ACTIVE_ID

        ORDER BY SUPPLIER.SUPPLIER_NAME
    """)
    data = cursor.fetchall()
    return render_template('viewsuppliers.html', data = data)

# view all Suppliers_part
@app.route('/suppliers/view-parts', methods = ['GET'])#FINISHED 
def view_parts():
    cursor.execute("""
        SELECT SUPPLIER.SUPPLIER_NAME AS "Supplier", PART.PART_NAME AS "Part", 
        SUPPLIER_PART.PART_COST, SUPPLIER_STATUS.ACTIVE_NAME AS "Active"

        FROM SUPPLIER
        JOIN SUPPLIER_STATUS
        ON SUPPLIER.ACTIVE_ID = SUPPLIER_STATUS.ACTIVE_ID
        JOIN SUPPLIER_PART
        ON SUPPLIER.SUPPLIER_ID = SUPPLIER_PART.SUPPLIER_ID
        JOIN PART
        ON SUPPLIER_PART.PART_ID = PART.PART_ID

        ORDER BY SUPPLIER.SUPPLIER_NAME, PART.PART_NAME
    """)
    data = cursor.fetchall()
    return render_template('viewparts.html', data = data)

# report parts rate list with supplier info (jahidul)
@app.route ('/suppliers/partsratelist-report' , methods = ['GET'])
def partsratelist_report():
    cursor.execute("""
        Select PART.PART_NAME,
		SUPPLIER_PART.PART_COST As 'Part Price', 
		SUPPLIER.SUPPLIER_NAME,
		SUPPLIER.S_ADDRESS_LINE1 As 'Address',
		SUPPLIER.S_PHONE As 'Contact no.',
		SUPPLIER.S_EMAIL As 'Email Address',
		SUPPLIER_STATUS.ACTIVE_NAME As 'Supplier Status'
		
		from SUPPLIER
		Join SUPPLIER_STATUS
		On SUPPLIER.ACTIVE_ID=SUPPLIER_STATUS.ACTIVE_ID
		Join SUPPLIER_PART
		On SUPPLIER.SUPPLIER_ID=SUPPLIER_PART.SUPPLIER_ID
		Join PART
		On PART.PART_ID=SUPPLIER_PART.PART_ID
		
		order by 2;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_partsratelist.html', data = data)

################################### VIOLATIONS ##################################################
@app.route('/violations', methods = ['GET']) 
def violation():
    return render_template('violations.html')

# create violation
@app.route('/violations/new-violation', methods = ['POST', 'GET'])
def new_violation():
    cursor.execute("""
        SELECT V_ID, V_VIN, V_LICENSE_PLATE, MAKE.MAKE_NAME, MODEL.MODEL_NAME 
        FROM VEHICLE
        JOIN MAKE
        ON MAKE.MAKE_ID=VEHICLE.MAKE_ID
        JOIN MODEL
        ON MODEL.MODEL_ID=MODEL.MAKE_ID
    """)
    rows = cursor.fetchall()
    vehicles = []
    for vehicle in rows:
        vehicles.append(vehicle)
    cursor.execute("SELECT STATE_NAME FROM STATE")
    rows = cursor.fetchall()
    states = []
    for state in rows:
        states.append(state[0])
    if request.method =='POST':
        vname = request.form.get("vname")
        lawcode = request.form.get("lawcode")
        vehicle = request.form.get("vehicle")
        date = request.form.get("date")
        state = request.form.get("state")
        v_id = request.form.get('vehicle')
        x = v_id.split(", ")
        y = int(x[0][1:])
        if vname and lawcode is not None:
            # new violation
            query = "INSERT INTO VIOLATION (VIOLATION_NAME, LAW_CODE, V_ID, VIOLATION_DATE) OUTPUT INSERTED.VIOLATION_ID VALUES (?,?,?,?)"
            vals = (vname, lawcode, y, date)
            cursor.execute(query, vals)
            vid = cursor.fetchone()[0]
            conn.commit()
            # violation state
            qry = "SELECT STATE_ID FROM STATE WHERE STATE_NAME = '{}'".format(state)
            cursor.execute(qry)
            state_id = cursor.fetchone()[0]
            query = "INSERT INTO STATE_VIOLATION (VIOLATION_ID, STATE_ID) VALUES (?,?)"
            values = (vid, state_id)
            cursor.execute(query, values)
            conn.commit()
            return render_template('violations.html')
    return render_template('newviolation.html', vehicles=vehicles,states=states)

# modify violation
@app.route('/violations/update-violation', methods = ['POST', 'GET'])
def update_violation():
    cursor.execute("""
        SELECT VIOLATION.VIOLATION_ID, VIOLATION.LAW_CODE, STATE.STATE_NAME, VIOLATION_NAME,
        VEHICLE.V_VIN, MAKE.MAKE_NAME, MODEL.MODEL_NAME
        FROM VIOLATION
        JOIN STATE_VIOLATION
        ON VIOLATION.VIOLATION_ID = STATE_VIOLATION.VIOLATION_ID
        JOIN STATE
        ON STATE.STATE_ID = STATE_VIOLATION.STATE_ID
        JOIN VEHICLE
        ON VIOLATION.V_ID = VEHICLE.V_ID
        JOIN MAKE
        ON MAKE.MAKE_ID = VEHICLE.MAKE_ID
        JOIN MODEL
        ON MODEL.MODEL_ID = VEHICLE.MAKE_ID
    """)
    rows = cursor.fetchall()
    violations = []
    for violation in rows:
        violations.append(violation)
    cursor.execute("SELECT STATE_ID, STATE_NAME FROM STATE")
    rows = cursor.fetchall()
    states = []
    for state in rows:
        states.append(state[1])
    cursor.execute("""
        SELECT V_ID, V_VIN, V_LICENSE_PLATE, MAKE_NAME, MODEL_NAME
        FROM VEHICLE
        JOIN MAKE
        ON VEHICLE.MAKE_ID=MAKE.MAKE_ID
        JOIN MODEL
        ON VEHICLE.MODEL_ID=MODEL.MODEL_ID
    """)
    rows = cursor.fetchall()
    vehicles = []
    for vehicle in rows:
        vehicles.append(vehicle[0:4])
    if request.method == 'POST':
        violation_id = request.form.get('violation')
        print(violation_id)
        x = violation_id.split(", ")
        print(x)
        y = int(x[0][1:])
        print(y)
        field = request.form.get('tblname')
        value = request.form.get('value')
        if field == "VIOLATION SET V_ID":
            value = request.form.get('vehicle')
            print(value)
            x = value.split(", ")
            value = int(x[0][1:])
            sql = "UPDATE {} = ? WHERE VIOLATION_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('violations.html')
        if field == "STATE_VIOLATION SET STATE_ID":
            value = request.form.get('state')
            cursor.execute("SELECT STATE_ID FROM STATE WHERE STATE_NAME = '{}'".format(value))
            state = cursor.fetchone()[0]
            sql = "UPDATE {} = ? WHERE VIOLATION_ID = ?".format(field)
            vals = (state, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('violations.html')
        else:
            sql = "UPDATE {} = ? WHERE VIOLATION_ID = ?".format(field)
            vals = (value, y)
            cursor.execute(sql, vals)
            conn.commit()
            return render_template('violations.html')
    return render_template('updateviolation.html', violations=violations,states=states,vehicles=vehicles)

@app.route('/violations/view-violations', methods = ['GET'])
def view_violation():
    cursor.execute("""
        SELECT VIOLATION.VIOLATION_ID, VIOLATION.LAW_CODE, STATE.STATE_NAME, VEHICLE.V_VIN, 
        MAKE.MAKE_NAME, MODEL.MODEL_NAME, VIOLATION.VIOLATION_DATE, VIOLATION_NAME
        FROM VIOLATION
        JOIN STATE_VIOLATION
        ON VIOLATION.VIOLATION_ID = STATE_VIOLATION.VIOLATION_ID
        JOIN STATE
        ON STATE.STATE_ID = STATE_VIOLATION.STATE_ID
        JOIN VEHICLE
        ON VIOLATION.V_ID = VEHICLE.V_ID
        JOIN MAKE
        ON MAKE.MAKE_ID = VEHICLE.MAKE_ID
        JOIN MODEL
        ON MODEL.MODEL_ID = VEHICLE.MAKE_ID
    """)
    data = cursor.fetchall()
    return render_template('viewviolations.html', data = data)

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

# report past violations (jerry)
@app.route ('/violations/pastviolations-report' , methods = ['GET'])
def pastviolations_report():
    cursor.execute("""
        SELECT
		CUSTOMER.C_FNAME AS 'Customer First Name',
		CUSTOMER.C_LNAME AS 'Last Name',
		VEHICLE.V_VIN AS 'Vehicle VIN',
		STATE.STATE_NAME AS 'State',
		VIOLATION.VIOLATION_NAME AS 'Violation',
		VIOLATION.VIOLATION_DATE AS 'Violation Date',
		VIOLATION.LAW_CODE AS 'Law Code'

		FROM CUSTOMER
		JOIN CUSTOMER_VEHICLE ON CUSTOMER.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
		JOIN VEHICLE ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID
		JOIN VIOLATION ON VEHICLE.V_ID = VIOLATION.V_ID
		JOIN STATE_VIOLATION ON VIOLATION.VIOLATION_ID = STATE_VIOLATION.VIOLATION_ID
		JOIN STATE ON STATE_VIOLATION.STATE_ID = STATE.STATE_ID

		ORDER BY VIOLATION.VIOLATION_DATE;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_pastviolations.html', data = data)
