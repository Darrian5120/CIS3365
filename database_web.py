import flask
from flask import Flask, request, make_response, render_template, url_for, redirect
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
import pprint 

############################################## READ ME #####################################
# RUN THIS PROGRAM AND THEN OPEN BROWSER AND PASTE http://127.0.0.1:5000/ TO YOUR BROWSER
# MAKE SURE YOU HAVE ALL HTML PAGES DOWNLOADED AND CHANGE YOUR CONNECTION STRING TO YOUR OWN
# Every category should have a CRUD operation, please pick one to code with python AND html
# Recycle other's code and make sure your code works before pushing to github and include useful comments
############################################################################################
# Darrian - update supplier
# Mustafa - vehicles insert, vehicle delete, vehicle update
# Brandon - 
# Anthony - employee create(insert), employee delete, vehicle report, employee update
# Jerry - vehicle update, vehicle report
# Kyle - service create(insert), service delete, employee report, violation report
# Jahidul - 
# Gian - service update, service report
# Zach - violation insert, violation delete, violation update
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
            query = "INSERT INTO Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME, ACTIVE_ID, BUSINESS_ID) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?,?,?)"
            vals = (lname, fname, bname, active, business)
            data = cursor.execute(query, vals)
            customer_id = cursor.fetchone()[0]
            conn.commit()
            # new customer contact info
            phone = request.form.get("phone")
            email = request.form.get("email")
            address = request.form.get("addy1")
            address2 = request.form.get("addy2")
            zip_code = request.form.get("zip")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            query = "INSERT INTO Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME, ACTIVE_ID, BUSINESS_ID, ADDRESS_LINE1, ADDRESS_LINE2, C_CITY, STATE_NAME,  C_ZIP,COUNTRY_NAME, C_PHONE, C_EMAIL) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
            vals = (lname, fname, bname, active, business, address, address2, city, state, zip_code, country, phone, email)
            data = cursor.execute(query, vals)
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
    if request.method == 'POST':
        # convert customer id to int for sql statement
        customer_id = request.form.get('customer')
        print(customer_id)
        x = customer_id.split(", ")
        y = int(x[0][1:])
        # get table, column, and new value data
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE CUSTOMER_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        if field == 'Customer SET STATE_NAME':
            query = "SELECT STATE_ID FROM STATE WHERE STATE_NAME = ?"
            val = value
            cursor.execute(query, val)
            data = cursor.fetchall()
            sql = "UPDATE CUSTOMER_STATE SET STATE_ID = ? WHERE CUSTOMER_ID = ?"
            vals = (data[0][0], y)
            cursor.execute(sql, vals)
            conn.commit()
        message = 'Customer edited Sucessfully'
        return render_template('updatecustomer.html', customers=customers, message = message)
        #return redirect(url_for('edit_customer', customer_id=customer_id))
    return render_template('updatecustomer.html', customers=customers)

# remove customer from db by setting status to inactive
@app.route('/customers/delete-customer',methods = ['POST','GET'])
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
@app.route('/customers/view-customers', methods = ['GET']) 
def view_customers():
    cursor.execute("""
        SELECT CUSTOMER.CUSTOMER_ID AS "ID", CUSTOMER.C_FNAME, CUSTOMER.C_LNAME,
        CUSTOMER.C_BUSINESS_NAME, CUSTOMER_CONTACT_INFO.C_PHONE, CUSTOMER_CONTACT_INFO.C_EMAIL,
        CUSTOMER_CONTACT_INFO.C_ADDRESS, CUSTOMER_CONTACT_INFO.C_CITY, CUSTOMER_CONTACT_INFO.STATE_NAME,
        CUSTOMER_CONTACT_INFO.C_ZIP, CUSTOMER_STATUS.ACTIVE_NAME 

        FROM Customer
        JOIN CUSTOMER_CONTACT_INFO
        ON Customer.CUSTOMER_ID = CUSTOMER_CONTACT_INFO.CUSTOMER_ID
        JOIN CUSTOMER_STATUS
        ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID

        
        ORDER BY CUSTOMER.ACTIVE_ID, Customer.CUSTOMER_ID
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('viewCustomers.html', data = data)

@app.route ('/customers/inactive-report' , methods = ['GET'])
def inactive_report():
    cursor.execute("""
        SELECT Customer.C_FNAME AS "First Name", Customer.C_LNAME AS "Last Name", 
        CUSTOMER_CONTACT_INFO.C_PHONE AS "Phone", CUSTOMER_STATUS.ACTIVE_NAME

        FROM Customer
        JOIN CUSTOMER_STATUS
        ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID
        JOIN CUSTOMER_CONTACT_INFO
        ON Customer.CUSTOMER_ID = CUSTOMER_CONTACT_INFO.CUSTOMER_ID
        JOIN SERVICE_ORDER
        ON SERVICE_ORDER.CUSTOMER_ID = Customer.CUSTOMER_ID

        WHERE Customer.ACTIVE_ID = 2 OR Customer.ACTIVE_ID = 4 /*OR SERVICE_ORDER.ORDER_DATE < GETDATE()*/
        ORDER BY Customer.ACTIVE_ID, CUSTOMER.C_LNAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_inactivecustomer.html', data = data)

# Report Long term loyal customer
# Not sure if path is correct
@app.route ('/customer/longtermloyalcustomer-report' , methods = ['GET'])
def longtermloyalcustomer_report():
    cursor.execute("""
        SELECT 
        Customer.CUSTOMER_ID AS "ID",
        Customer.C_FNAME AS "First Name",
        Customer.C_LNAME AS "Last Name",
        CUSTOMER_STATUS.ACTIVE AS "Customer Type",
        CUSTOMER_VEHICLE.V_VIN AS "VIN #",
        VEHICLE.V_MAKE AS "Make",
        VEHICLE.V_MODEL AS "Model",
        SERVICE_ORDER.ORDER_DATE AS "First Time Customer Date"

        FROM Customer 
        JOIN CUSTOMER_STATUS
        ON Customer.CUSTOMER_ID = CUSTOMER_STATUS.CUSTOMER_ID
        JOIN CUSTOMER_VEHICLE
        ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
        JOIN VEHICLE
        ON CUSTOMER_VEHICLE.V_VIN = VEHICLE.V_VIN
        JOIN CUSTOMER_ORDER
        ON Customer.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
        JOIN SERVICE_ORDER
        ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID

        WHERE (CUSTOMER_STATUS.C_ACTIVE= 1 OR CUSTOMER_STATUS.C_ACTIVE= 3) AND SERVICE_ORDER.ORDER_DATE < DATEADD(YEAR, -1, GETDATE());
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_longtermloyalcustomer.html', data = data)

################################### VEHICLES ##################################################
@app.route('/vehicles', methods = ['GET']) 
def vehicles():
    return render_template('vehicles.html')

@app.route ('/vehicles/new-vehicle', methods = ['POST', 'GET'])
def new_vehicle():
    message = ''
    sql = "SELECT CUSTOMER_ID, C_FNAME, C_LNAME FROM Customer"
    cursor.execute(sql)
    rows = cursor.fetchall()
    customers = []
    for customer in rows:
        customers.append(customer)
    if request.method == 'POST':
        vin = request.form.get("vin")
        make = request.form.get("make")
        model = request.form.get("model")
        year = request.form.get("year")
        license_plate = request.form.get("plate")
        color = request.form.get("color")
        if vin and make and model and year and license_plate is not None:
            # insert vehicle table
            query = "INSERT INTO VEHICLE (V_VIN, V_MAKE, V_MODEL, V_YEAR, V_LICENSE_PLATE, V_COLOR, ACTIVE_ID) VALUES (?,?,?,?,?,?)"
            vals = (vin, make, model, year, license_plate, color)
            cursor.execute(query, vals)
            conn.commit()
            # insert customer_vehicle table
            customer_id = request.form.get('customer')
            x = customer_id.split(", ")
            y = int(x[0][1:])
            query = "INSERT INTO VEHICLE (V_VIN, CUSTOMER_ID) VALUES (?,?)"
            vals = (vin, y)
            cursor.execute(query, vals)
            conn.commit()
            # insert insurance
            ins = request.form.get("ins_name")
            query = "INSERT INTO INSURANCE_COMPANY (INSURANCE_NAME) VALUES (?)"
            vals = (ins)
            cursor.execute(query, vals)
            conn.commit()
            # insert policy
            policy = request.form.get("policy")
            query = "INSERT INTO INSURANCE_POLICY (POLICY_NAME) VALUES (?)"
            vals = (policy)
            cursor.execute(query, vals)
            conn.commit()
            expiration = request.form.get("exp")
            # FIXME - may remove company_insurance_policy and move to vehicle_policy
            return render_template ('newvehicle.html', customers=customers)
    return render_template ('newvehicle.html', customers=customers)

# modify existing vehicle by entering vin
@app.route ('/vehicles/update-vehicle' , methods = ['POST' , 'GET'])
def update_vehicles():
    if request.method == 'POST':
        v_vin = request.form.get ("v_vin")
        field =  request.form.get ("field")
        value = request.form.get ("value")
        if v_vin and field and value is not None:
            #query = 
            #vals = 
            #data = 
            #conn.commit ()
            message = "Employee edited sucessfully!"
            #return render_template ('employees.html' data = data , message = message)
        return render_template ('updateemployee.html')

# remove vehicle from db by setting status to inactive  
@app.route ('/vehicles/delete-vehicles' , methods =['POST' , 'GET'])
def delete_vehicle():
   
    sql = "SELECT V_ID, V_VIN, V_LICENSE_PLATE FROM VEHICLE"
    cursor.execute(sql)
    rows = cursor.fetchall()
    vehicles = []
    for vehicle in rows:
        vehicles.append(vehicle)
    if request.method == 'POST':
        
        vehicle_id = request.form.get('vehicle')
        print(vehicle_id)
        x = vehicle_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE Vehicle SET ACTIVE_ID = 2 WHERE V_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Vehicle removed sucessfully'
        return render_template('deletevehicel.html', vehicles = vehicles, message = message)
        
    return render_template('deletevehicle.html', vehicles = vehicles)

#view all vehicles
@app.route ('/vehicles/view-vehicles' , methods = ['GET'])
def view_vehicles():
    cursor.execute ("SELECT * FROM CoogTechSolutions.dbo.vehicle")
    data = cursor.fetchall()
    return render_template ('viewvehicles.html' , data = data)
## vehicle part report 
@app.route('/vehicles/vehiclepart-report', methods = ['GET']) 
def vehicle_part_report():
    cursor.execute("""
        SELECT VEHICLE_SERVICE.V_VIN AS 'VIN', VEHICLE.V_YEAR AS 'Year', VEHICLE.V_MAKE AS 'Make', 
        VEHICLE.V_MODEL AS 'Model', SUPPLIER.SUPPLIER_NAME AS 'Supplier', PART.PART_NAME AS 'Part'

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

        ORDER BY VEHICLE.V_VIN;
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

################################### EMPLOYEES ##################################################
@app.route('/employees', methods = ['GET']) 
def employees():
    return render_template('employees.html')

# Employee insert/create FINISHED @anthony
@app.route ('/employees/new-employee', methods = ['POST', 'GET'])
def new_employee():
    message = ''
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
            # new employee default
            query = "INSERT INTO Customer (C_LNAME, C_FNAME, ROLE_ID, ACTIVE_ID, ADDRESS_LINE1, ADDRESS_LINE2, C_CITY, STATE_NAME,  C_ZIP,COUNTRY_NAME, C_PHONE, C_EMAIL) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
            vals = (lname, fname, role, active, address, address2, city, state, zip_code, country, phone, email)
            cursor.execute(query, vals)
            employee_id = cursor.fetchone()[0]
            conn.commit()
            message = "New employee entered successfully!"
            return render_template ('newemployee.html', message = message)
    return render_template ('newemployee.html')
    
# ask for help here
# modify existing employee by entering id
@app.route ('/employees/update-employee' , methods = ['POST' , 'GET'])
def update_employee():
    
    sql = "SELECT EMPLOYEE_ID, E_FNAME, E_LNAME FROM Employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    employees = []
    
    for employee in rows:
        employees.append(employees)
    if request.method == 'POST':
        
        employee_id = request.form.get ('employee')
        print(employee_id)
        x = employee_id.split(", ")
        y = int (x[0][1:])
        
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE EMPLOYEE_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Employee edidted sucessfully'
        
        return render_template('updateemployee.html', employees = employees, message = message)
    
    return render_template ('updateemployee.html', employees = employees)
    
                
# remove employee from db by setting status to inactive
@app.route ('/employees/delete-emloyee' , methods =['POST' , 'GET'])
def delete_employee():
    sql = "SELECT EMPLOYEE_ID, E_FNAME, E_LNAME FROM Employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    employee = []
    for employee in rows:
        employees.append(employee)
    if request.method == 'POST':
        
        employee_id = request.form.get('employee')
        print(employee_id)
        x = employee_id.split(", ")
        y = int(x[0][1:])
        
        sql = "UPDATE Employee SET ACTIVE_ID = 3 WHERE EMPLOYEE_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Employee removed sucessfully'
        
        return render_template('deleteemployee.html', employees = employees, message = message)
        
    return render_template('deleteemployee.html',  employees = employees)
           

#view all employees
@app.route ('/employees/view-employees' , methods = ['GET'])
def view_employees():
    cursor.execute ("SELECT * FROM CoogTechSolutions.dbo.Employee")
    data = cursor.fetchall()
    return render_template ('viewemployee.html' , data = data)

# employee part report
@app.route ('/employees/employeepart-report' , methods = ['GET'])
def employee_part_report():
    cursor.execute("""
        SELECT SUPPLIER.SUPPLIER_NAME AS "Supplier", PART.PART_NAME AS "Part", EMPLOYEE.EMPLOYEE_ID AS "Employee ID", 
        EMPLOYEE.EMPLOYEE_LNAME AS "Last Name", EMPLOYEE.EMPLOYEE_FNAME AS "First Name"

        FROM EMPLOYEE
        JOIN Employee_Status
        ON Employee_Status.EMPLOYEE_ID = EMPLOYEE.EMPLOYEE_ID
        JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
        ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
        JOIN SERVICE_LINE
        ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_LINE_ID = SERVICE_LINE.SERVICE_LINE_ID
        JOIN SERVICE_LINE_PART
        ON SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_PART.SERVICE_LINE_ID
        JOIN PART
        ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
        JOIN SUPPLIER_PART
        ON PART.PART_ID = SUPPLIER_PART.PART_ID
        JOIN SUPPLIER
        ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

        WHERE Employee_Status.ACTIVE_ID = 1
        ORDER BY PART.PART_NAME;
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_employeepart.html', data = data)

# Report New Employee
# not sure if path is right
@app.route ('/employees/newemployee-report' , methods = ['GET'])
def newemployee_report():
    cursor.execute("""
    SELECT 
    EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID AS "Employee ID",
    EMPLOYEE.EMPLOYEE_FNAME AS "First Name",
    EMPLOYEE.EMPLOYEE_LNAME AS "Last Name",
    EMPLOYEE.EMPLOYEE_HIRE_DATE AS "Date Hired",
    EMPLOYEE.EMPLOYEE_PAY_RATE AS "Pay Rate",
    EMPLOYEE.EMPLOYEE_JOB_FUNC AS "Job Type",
    Employee_Status.ACTIVE AS "Status",
    SERVICE_LINE.SERVICE_ID AS "Service ID",
    SERVICE.SERVICE_TYPE AS "Service Worked On"

    FROM EMPLOYEE
    JOIN Employee_Status
    ON EMPLOYEE.EMPLOYEE_ID = Employee_Status.EMPLOYEE_ID
    JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
    ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
    JOIN SERVICE_LINE
    ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_LINE_ID = SERVICE_LINE.SERVICE_LINE_ID    
    JOIN SERVICE
    ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID

    WHERE EMPLOYEE.EMPLOYEE_HIRE_DATE > DATEADD(YEAR, -2, GETDATE());
    """)
    
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_newemployee.html', data = data)

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
        actid = request.form.get("actid")
        if sertype and cost is not None:
            # default service
            query = "INSERT INTO Service (SERVICE_TYPE, COST, ACTIVE_ID) OUTPUT INSERTED.SERVICE_ID VALUES (?, ?, ?)"
            vals = (sertype, cost, actid)
            data = cursor.execute(query, vals)
            service_id = cursor.fetchone()[0]
            conn.commit()
            
            # add service line
            
# modify service
@app.route('/service/upate', methods = ['POST', 'GET'])
def update_service():
    
    sql = "SELECT SERVICE_ID, SERVICE_TYPE, COST, ACTIVE_ID FROM Service"
    cursor.execute(sql)
    rows = cursor.fetchall()
    service = []
    for services in rows:
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

# modify service order

# modify invoice 

        
        

# remove service from db by settiing status to inactive
@app.route('services/delete-service', methods = ['POST', 'GET'])
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
@app.route('services/delete-serviceline', methods = ['POST', 'GET'])
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
@app.route('services/delete-serviceorder', methods = ['POST', 'GET'])
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
@app.route('services/delete-invoice', methods = ['POST', 'GET'])
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
        SELECT Customer.CUSTOMER_ID AS "Customer ID", Customer.C_LNAME AS "Last Name", Customer.C_FNAME AS "First Name",
        ACCOUNT_REVENUE.REVENUE_NAME AS "Revenue Name", SERVICE.SERVICE_TYPE AS "SERVICE NAME", ACCOUNT_REVENUE.REVENUE_VALUE AS "Revenue Value"

        FROM CUSTOMER
        JOIN CUSTOMER_ORDER
        ON CUSTOMER.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
        JOIN SERVICE_ORDER
        ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
        JOIN SERVICE_LINE
        ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
        JOIN SERVICE
        ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
        JOIN INVOICE
        ON Customer.CUSTOMER_ID = INVOICE.CUSTOMER_ID
        JOIN INVOICE_PAYMENT
        ON  INVOICE.INVOICE_ID = INVOICE_PAYMENT.INVOICE_ID
        JOIN PAYMENT
        ON INVOICE_PAYMENT.PMT_NUMBER = PAYMENT.PMT_NUMBER
        JOIN PAYMENT_REVENUE
        ON PAYMENT.PMT_NUMBER = PAYMENT_REVENUE.PMT_NUMBER
        JOIN ACCOUNT_REVENUE
        ON PAYMENT_REVENUE.REVENUE_ID = ACCOUNT_REVENUE.REVENUE_ID

        ORDER BY INVOICE.INVOICE_DATE;""")
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_revenue.html', data = data)

# Report Incomplete Order
# Dont know the path
@app.route ('/services/incompleteorders-report' , methods = ['GET'])
def incompleteorders_report():
    cursor.execute ("""
    SELECT 
    SERVICE_LINE.SERVICE_ID AS "Order ID",
    SERVICE.SERVICE_TYPE AS "Type of Service",
    Customer.C_LNAME AS "Last Name", 
    SERVICE_ORDER.TOTAL_COST AS "Total Cost",
    SERVICE.DATE_START AS "Start Date",
    SERVICE.DATE_END AS "Estimated Finish Date"
    
    From Customer
    JOIN CUSTOMER_ORDER
    ON Customer.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
    JOIN SERVICE_ORDER
    ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
    JOIN SERVICE_LINE
    ON SERVICE_ORDER.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
    JOIN SERVICE
    ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID

    WHERE SERVICE.DATE_END > GETDATE()
    ORDER BY SERVICE.DATE_START;""")
    
    data = cursor.fetchall()
    conn.commit()
    return render_template ('report_incompleteorders.hmtl' , data = data)

# Report Yearly Service Order
# not sure if path is correct
@app.route ('/services/yearlyserviceorder-report' , methods = ['GET'])
def yearlyserviceorder_report():
    cursor.execute ("""
        SELECT
        CUSTOMER_ORDER.SERVICE_ORDER_ID AS "Order ID",
        SERVICE.SERVICE_TYPE AS "Serviced Ordered",
        Customer.C_FNAME AS "First Name",
        Customer.C_LNAME AS "Last Name",
        SERVICE_ORDER.ORDER_DATE AS "Date Ordered",
        SERVICE_LINE.LINE_COST AS "Cost of Service"

        FROM Customer
        JOIN CUSTOMER_ORDER
        ON Customer.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
        JOIN SERVICE_ORDER
        ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
        JOIN SERVICE_LINE
        ON SERVICE_ORDER.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
        JOIN SERVICE
        ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID

        WHERE YEAR(SERVICE_ORDER.ORDER_DATE) = YEAR(GETDATE()) AND SERVICE_ORDER.ORDER_DATE < GETDATE();
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template ('report_yearlyserviceorder.hmtl' , data = data)
#################################### Suppliers(parts) ###########################################
@app.route('/suppliers', methods = ['GET']) 
def suppliers():
        return render_template('suppliers.html')

@app.route('/customers/new-supplier', methods = ['POST','GET'])
def new_supplier():
    # get info from html
    if request.method == 'POST':
        supplier = request.form.get("sup_name")
        part = request.form.get("part_name")
        status = request.form.get("active")
        if supplier and part and status is not None:
            # insert supplier
            query = "INSERT INTO SUPPLIER (SUPPLIER_NAME, ACTIVE_ID) OUTPUT INSERTED.SUPPLIER_ID VALUES (?,?)"
            vals = (supplier, status)
            cursor.execute(query, vals)
            supplier_id = cursor.fetchone()[0]
            conn.commit()
            # insert part
            query = "INSERT INTO PART (PART_NAME) OUTPUT INSERTED.PART_ID VALUES (?)"
            vals = (part)
            cursor.execute(query, vals)
            part_id = cursor.fetchone()[0]
            conn.commit()
            # insert supplier part
            query = "INSERT INTO SUPPLIER_PART (PART_ID, SUPPLIER_ID) OUTPUT INSERTED.PART_ID VALUES (?,?)"
            vals = (part_id, supplier_id)
            cursor.execute(query, vals)
            message = "New Supplier/part entered successfully!"
            return render_template('suppliers.html', message=message)
    return render_template('newsupplier.html')

@app.route('/supplier/update-supplier', methods = ['POST','GET'])
def update_supplier():
    message = ''
    if request.method == 'POST':
        # get info from gui
        supplier_id = request.form.get("SUPPLIER_ID")
        field = request.form.get("tblname")
        value = request.form.get("value")
        # find if id exist
        if supplier_id and field and value is not None:
            sql = "SELECT SUPPLIER_ID FROM SUPPLIER where SUPPLIER_ID = ?" 
            vals = (supplier_id)
            cursor.execute(sql, vals)
            data = cursor.fetchall()
            if not data: # id doesn't exist
                message = "Invalid Supplier ID! Please review Suppliers"
                # update both supplier status fields - MUST COPY FOR STATUS TABLES ########################
                if field == "SUPPLIER_STATUS SET ACTIVE":
                    query = "UPDATE CoogTechSolutions.dbo.{fld} = ? WHERE SUPPLIER_ID = ?".format(fld = field)
                    if value == 'Active' or value == 'ACTIVE':
                        query = "UPDATE CoogTechSolutions.dbo.SUPPLIER_STATUS SET S_ACTIVE = ?, ACTIVE = ? WHERE SUPPLIER_ID = ?".format(fld = field)
                        vals = (1, "ACTIVE", supplier_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('suppliers.html', data=data, message=message)
                    else:
                        query = "UPDATE CoogTechSolutions.dbo.SUPPLIER_STATUS SET S_ACTIVE = ?, ACTIVE = ? WHERE SUPPLIER_ID = ?".format(fld = field)
                        vals = (2, "INACTIVE", supplier_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('suppliers.html', data=data, message=message)
                query = "UPDATE CoogTechSolutions.dbo.{fld} = ? WHERE SUPPLIER_ID = ?".format(fld = field)
                vals = (value, supplier_id)
                data = cursor.execute(query, vals)
                conn.commit()
                message = "Supplier edited successfully!"
                return render_template('suppliers.html', data=data, message=message)
        else: # missing id in gui
            message = "Missing values!"
    return render_template('updatesupplier.html', message = message)

@app.route('/customers/delete-supplier',methods = ['POST','GET'])
def delete_supplier():
     # send list of customer id's to gui dropdown
    sql = "SELECT SUPPLIER_ID, SUPPLIER_NAME FROM SUPPLIER"
    cursor.execute(sql)
    rows = cursor.fetchall()
    suppliers = []
    for supplier in rows:
        suppliers.append(supplier)
    if request.method == 'POST':
        # convert customer id to int for sql statement
        supplier_id = request.form.get('supplier')
        print(supplier_id)
        x = supplier_id.split(", ")
        y = int(x[0][1:])
        # set inactive partial delete
        sql = "UPDATE SUPPLIER SET ACTIVE_ID = 2 WHERE SUPPLIER_ID = ?"
        vals = (y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Supplier removed Sucessfully'
        return render_template('deletesupplier.html', suppliers=suppliers, message = message)
        #return redirect(url_for('edit_customer', customer_id=customer_id))
    return render_template('deletesupplier.html', suppliers=suppliers)


# view all Suppliers
@app.route('/suppliers/view-suppliers', methods = ['GET']) 
def view_suppliers():
    cursor.execute("""
        SELECT SUPPLIER.SUPPLIER_NAME AS "Supplier", PART.PART_NAME AS "Part",
        SUPPLIER_STATUS.ACTIVE_NAME AS "Active"

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
    conn.commit()
    return render_template('report_supplier.html', data = data)

################################### VIOLATIONS ##################################################
@app.route('/violations', methods = ['GET']) 
def violation():
    return render_template('violations.html')

# Update Supplier

# create violation
@app.route('/violations/new-violation', methods = ['POST', 'GET'])
def new_violation():
    message = ''
    if request.method =='POST':
        vioname = request.form.get("vioname")
        lcode = request.form.get("lcode")
        vid = request.form.get("vid")
        viodate = request.form.get("viodate")
        if vioname and lcode is not None:
            
            # new violation default
            query = "INSERT INTO VIOLATION (VIOLATION_NAME, LAW_CODE, V_ID, VIOLATION_DATE) OUTPUT INSERTED.VIOLATION_ID VALUES (?, ?, ?, ?)"
            vals = (vioname, lcode, vid, viodate)
            data = cursor.execute(query, vals)
            violation_id = cursor.fetchone()[0]
            conn.commit()
            
            message = "New violation entered sucessfully"
           return render_template('violation.html', data = data, message = message)
    return render_template('newviolation.html')

# modify violation
@app.route('/violations/update', methods = ['POST', 'GET'])
def update_violation():
    
    sql = "SELECT VIOLATION_ID, VIOLATION_NAME, LAW_CODE FROM VIOLATION"
    cursor.execute(sql)
    rows = cursor.fetchall()
    violations = []
    for violation in rows:
        violations.append(violation)
    if request.method == 'POST':
        
        violation_id = request.form.get('violation')
        print(violation_id)
        x = violation_id.split(", ")
        y = int([0][1:])
        
        field = request.form.get('tblname')
        value = request.form.get('value')
        sql = "UPDATE {} = ? WHERE VIOLATION_ID = ?".format(field)
        vals = (value, y)
        cursor.execute(sql, vals)
        conn.commit()
        message = 'Violation edited sucessfully'
        return render_template('updateviolation.html', violations = violations, message = message)
        
    return render_template('updateviolation.html', violations = violation)

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

