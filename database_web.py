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
# Mustafa - vehicles insert, vehicle delete, vehicle update
# Brandon - supplier update, supplier report
# Anthony - employee create(insert), employee delete, vehicle report
# Maddy - supplier create(insert), supplier delete, 
# Jerry - vehicle update, vehicle report
# Kyle - service create(insert), service delete, 
# Jahidul - employee update, employee report
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
@app.route('/customers/new-customer', methods = ['POST','GET']) 
def new_customer():
    message = ''
    if request.method == 'POST':
        lname = request.form.get("lname")
        fname = request.form.get("fname")
        bname = request.form.get("bname")
        if lname and fname is not None:
            # new customer default
            query = "INSERT INTO CoogTechSolutions.dbo.Customer (C_LNAME, C_FNAME, C_BUSINESS_NAME) OUTPUT INSERTED.CUSTOMER_ID VALUES (?,?,?)"
            vals = (lname, fname, bname)
            data = cursor.execute(query, vals)
            customer_id = cursor.fetchone()[0]
            conn.commit()
            # new customer status
            active = request.form.get("is_active")
            query = "INSERT INTO CoogTechSolutions.dbo.CUSTOMER_STATUS (CUSTOMER_ID, C_ACTIVE, ACTIVE) VALUES (?,?,?)"
            if active is not None:
                status_vals = (customer_id, 1, "Active")
            else:
                status_vals = (customer_id, 2, "Inactive")
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
            business = request.form.get("is_biz")
            query = "INSERT INTO CoogTechSolutions.dbo.CUSTOMER_TYPE (CUSTOMER_ID, BUSINESS_ID, BUSINESS) VALUES (?,?,?)"
            if business is not None:
                type_vals = (customer_id, 1, "Business")
            else:
                type_vals = (customer_id, 0, "Individual")
            data = cursor.execute(query, type_vals)
            conn.commit()
            # new customer state
            message = "New customer entered successfully!"
            return render_template('customers.html', data=data, message=message)
    return render_template('newcustomer.html')

# modify exisitng customer by entering id
# FIXME- find out how to only update one field
@app.route('/customers/update-customer', methods = ['POST','GET'])
def update_customer():
    message = ''
    if request.method == 'POST':
        # get info from gui
        customer_id = request.form.get("cid")
        field = request.form.get("tblname")
        value = request.form.get("value")
        # find if id exist
        if customer_id and field and value is not None:
            sql = "SELECT CUSTOMER_ID FROM Customer where CUSTOMER_ID = ?" 
            vals = (customer_id)
            cursor.execute(sql, vals)
            data = cursor.fetchall()
            if not data: # id doesn't exist
                message = "Invalid Customer ID! Please review Customers"
            else:
                # update both customer type fields - DO NOT COPY THIS ####################
                if field == "CUSTOMER_TYPE SET BUSINESS":
                    query = "UPDATE CoogTechSolutions.dbo.{fld} = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                    if value == 'Business' or value == 'BUSINESS':
                        query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_TYPE SET BUSINESS_ID = ?, BUSINESS = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                        vals = (1, "BUSINESS", customer_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('customers.html', data=data, message=message)
                    else:
                        vals = ("Individual", customer_id)
                        query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_TYPE SET BUSINESS_ID = ?, BUSINESS = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                        vals = (0, "INDIVIDUAL", customer_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('customers.html', data=data, message=message)
                # update both customer status fields - MUST COPY FOR STATUS TABLES ########################
                if field == "CUSTOMER_STATUS SET ACTIVE":
                    query = "UPDATE CoogTechSolutions.dbo.{fld} = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                    if value == 'Active' or value == 'ACTIVE':
                        query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_STATUS SET C_ACTIVE = ?, ACTIVE = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                        vals = (1, "ACTIVE", customer_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('customers.html', data=data, message=message)
                    else:
                        query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_STATUS SET C_ACTIVE = ?, ACTIVE = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                        vals = (2, "INACTIVE", customer_id)
                        data = cursor.execute(query, vals)
                        conn.commit()
                        return render_template('customers.html', data=data, message=message)
                query = "UPDATE CoogTechSolutions.dbo.{fld} = ? WHERE CUSTOMER_ID = ?".format(fld = field)
                vals = (value, customer_id)
                data = cursor.execute(query, vals)
                conn.commit()
                message = "Customer edited successfully!"
                return render_template('customers.html', data=data, message=message)
        else: # missing id in gui
            message = "Missing values!"
    return render_template('updatecustomer.html', message = message)

# remove customer from db by setting status to inactive
@app.route('/customers/delete-customer',methods = ['POST','GET'])
def delete_customer():
    message = ''
    if request.method == 'POST':
        customer_id = request.form.get("cid")
        # find if id exist
        if customer_id is not None:
            sql = "SELECT CUSTOMER_ID FROM Customer where CUSTOMER_ID = ?" 
            vals = (customer_id)
            cursor.execute(sql, vals)
            data = cursor.fetchall()
            if not data: # id doesn't exist
                message = "Invalid Customer ID! Please review Customers"
            else: 
                query = "UPDATE CoogTechSolutions.dbo.CUSTOMER_STATUS SET C_ACTIVE = ?, ACTIVE= ? WHERE CUSTOMER_ID = ?"
                vals = (2, "INACTIVE", customer_id)
                data = cursor.execute(query, vals)
                conn.commit()
                message = "Customer removed successfully!"
                return render_template('customers.html', data=data, message=message)
        else: # missing id in gui
            message = "Missing values!"
    return render_template('deletecustomer.html', message = message)

# view all customers
@app.route('/customers/view-customers', methods = ['GET']) 
def view_customers():
    cursor.execute("""
        SELECT CUSTOMER.CUSTOMER_ID AS "ID", CUSTOMER.C_FNAME, CUSTOMER.C_LNAME,
        CUSTOMER.C_BUSINESS_NAME, CUSTOMER_CONTACT_INFO.C_PHONE, CUSTOMER_CONTACT_INFO.C_EMAIL,
        CUSTOMER_CONTACT_INFO.C_ADDRESS, CUSTOMER_CONTACT_INFO.C_CITY, CUSTOMER_CONTACT_INFO.STATE_NAME,
        CUSTOMER_CONTACT_INFO.C_ZIP, CUSTOMER_STATUS.ACTIVE 
        FROM Customer
        JOIN CUSTOMER_CONTACT_INFO
        ON Customer.CUSTOMER_ID = CUSTOMER_CONTACT_INFO.CUSTOMER_ID
        JOIN CUSTOMER_STATUS
        ON Customer.CUSTOMER_ID = CUSTOMER_STATUS.CUSTOMER_ID
        WHERE CUSTOMER_STATUS.C_ACTIVE = 1 OR CUSTOMER_STATUS.C_ACTIVE = 3
        ORDER BY CUSTOMER_STATUS.C_ACTIVE, Customer.CUSTOMER_ID
    """)
    data = cursor.fetchall()
    conn.commit()
    return render_template('viewCustomers.html', data = data)

@app.route ('/customers/inactive-report' , methods = ['GET'])
def inactive_report():
    cursor.execute("""
        SELECT Customer.C_FNAME AS "First Name", Customer.C_LNAME AS "Last Name", 
        CUSTOMER_CONTACT_INFO.C_PHONE AS "Phone", CUSTOMER_STATUS.ACTIVE

        FROM Customer
        JOIN CUSTOMER_STATUS
        ON Customer.CUSTOMER_ID = CUSTOMER_STATUS.CUSTOMER_ID
        JOIN CUSTOMER_CONTACT_INFO
        ON Customer.CUSTOMER_ID = CUSTOMER_CONTACT_INFO.CUSTOMER_ID
        JOIN CUSTOMER_ORDER
        ON Customer.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
        JOIN SERVICE_ORDER
        ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID

        WHERE CUSTOMER_STATUS.C_ACTIVE = 2 OR CUSTOMER_STATUS.C_ACTIVE = 4 /*OR SERVICE_ORDER.ORDER_DATE < GETDATE()*/
        ORDER BY CUSTOMER.C_LNAME, CUSTOMER.C_FNAME;
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
@app.route ('/vehicles/new-vehicles', methods = ['POST', 'GET'])
## add new vehicle ##
def new_vehicle():
    message = ''
    if request.method == 'POST':
        v_vin = request.form.get ("v_vin")
        make = request.form.get ("make")
        model = request.form.get ("model")
        year = request.form.get ("year")
        license_plate = request.form.get ("plate")
        if v_vin and make and model and year and license_plate is not None:

             # new employee default
            #query = ""
            #vals = 
            #data = 
            #conn.commit()
            
            # new employee status
            #query = ""
            #vals = 
            #data = 
            #conn.commit()
            
            # new employee contact info
            
            #
            
            message = "New vehicle entered successfully!"
            #return render_template ('vehicles.html' , data = data, message = message)
        return render_template ('newvehicle.html')

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
    message = ''
    v_vin = request.form.get ("v_vin")      ##NEEDS DOUBLE CHECKING##
    if v_vin is not None:
        #query = 
        #vals = 
        #data = 
        #conn.commit()
        message = "Employee removed successfully!"
        #return render_template ('employees.html' , data = data , message = message)
    return render_template('deleteemployee.html')

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

    ORDER BY VEHICLE_STATUS.ACTIVE""")
    data = cursor.fetchall()
    conn.commit()
    return render_template('report_CustomerVehicleStatusReport.html', data = data)
################################### EMPLOYEES ##################################################
@app.route('/employees', methods = ['GET']) 
def employees():
    return render_template('employees.html')

@app.route ('/employees/new-employee', methods = ['POST', 'GET'])
def new_employee():
    message = ''
    if request.method == 'POST':
        lname = request.form.get ("lname")
        fname = request.form.get ("fname")
        address = request.form.get ("address")
        pnumber = request.form.get ("pnumber")
        jobfunc = request.form.get ("jobfunc")
        if lname and fname and address and pnumber and jobfunc is not None:
            
            # new employee default
            #query = ""
            #vals = 
            #data = 
            #conn.commit()
            
            # new employee status
            #query = ""
            #vals = 
            #data = 
            #conn.commit()
            
            # new employee contact info
            
            #
            
            message = "New employee entered successfully!"
            return render_template ('employees.html' , data = data, message = message)
        return render_template ('newemployee.html')
    
# modify existing employee by entering id
@app.route ('/employees/update-employee' , methods = ['POST' , 'GET'])
def update_employee():
    if request.method == 'POST':
        friendid = request.form.get ("fid")
        field =  request.form.get ("field")
        value = request.form.get ("value")
        if friendid and field and value is not None:
            #query = 
            #vals = 
            #data = 
            #conn.commit ()
            message = "Employee edited sucessfully!"
            #return render_template ('employees.html' data = data , message = message)
        return render_template ('updateemployee.html')
    
# remove employee from db by setting status to inactive
@app.route ('/employees/delete-emloyee' , methods =['POST' , 'GET'])
def delete_employee():
    message = ''
    friendid = request.form.get ("fid")
    if friendid is not None:
        #query = 
        #vals = 
        #data = 
        #conn.commit()
        message = "Employee removed successfully!"
        #return render_template ('employees.html' , data = data , message = message)
    return render_template('deleteemployee.html')

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
################################### SERVICES ##################################################
@app.route('/services', methods = ['GET']) 
def services():
    return render_template('services.html')

@app.route('/services/view-services', methods = ['GET'])
def view_services():
    cursor.execute ("SELECT * FROM CoogTechSolutions.dbo.SERVICE")
    data = cursor.fetchall()
    return render_template ('viewservices.html' , data = data)

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
################################### VIOLATIONS ##################################################
@app.route('/violations', methods = ['GET']) 
def violation():
    return render_template('violations.html')



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
