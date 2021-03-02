import datetime
from datetime import date
import pyodbc
import pandas as pd
from pandas import ExcelFile
from tabulate import tabulate

#Menu to create
def menu():
    menu = ('\nMENU\n'
        'a - Add new table\n'
        'd - Remove table\n'
        'i - Import EXCEL\n'
        'r - Remove element\n'
        'u - Update attribute\n'
        'o - Output table\n'
        'q - Quit\n')

    command = ''

    while(command != 'q'): # menu continues to run until user quits
        print(menu, end='\n')
        command = input('Choose an option:\n')

        while(command != 'a' and command != 'd' and command != 'i' and command != 'r' and command != 'u' and command != 'o' and command != 'q'): # pause menu when option is selected
            command = input('Choose an option:\n')

        # add new table
        if command == 'a':
            None
       

def insert_func(data, sql_string):
    None         
                     
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9PNG3JO;'
                      'Database=CoogTechSolutions;'
                      'Trusted_Connection=yes;')

###################################################################################################################

data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\CUSTOMER.xlsx")   
df = pd.DataFrame(data)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.Customer OFF;
        INSERT INTO CoogTechSolutions.dbo.Customer (ORDER_ID, SERVICE_ID, C_FNAME, C_LNAME, C_BUSINESS_NAME)
        VALUES (?,?,?,?,?)
        ''', row.ORDER_ID, row.SERVICE_ID, row.C_FNAME, row.C_LNAME, row.C_BUSINESS_NAME)
connection.commit()
cursor = connection.cursor()
sql_query = pd.read_sql_query('SELECT * FROM Customer',connection)
print(sql_query)
print(type(sql_query))

#
data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\FINSIHED_ORDER.xlsx")   
df = pd.DataFrame(data)
print(df)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.FINSIHED_ORDER ON;
        INSERT INTO CoogTechSolutions.dbo.FINISHED_ORDER (ORDER_ID, DATE_START, DATE_END, Quality)
        VALUES (?,?,?,?)
        ''', row.ORDER_ID, row.DATE_START, row.DATE_END, row.Quality)
connection.commit()
cursor = connection.cursor()
sql_query = pd.read_sql_query('SELECT * FROM FINSIHED_ORDER',connection)
print(sql_query)
print(type(sql_query))


#
data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\PAYMENT.xlsx")   
df = pd.DataFrame(data)
#df = df.fillna(value=0)
print(df)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.PAYMENT ON;
        INSERT INTO CoogTechSolutions.dbo.PAYMENT (C_ID, AMT_PAID)
        VALUES (?,?)
        ''', row.C_ID, row.AMT_PAID)


#
data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\SERVICE_ORDER_LINE.xlsx")   
df = pd.DataFrame(data)
#df = df.fillna(value=0)
print(df)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.SERVICE_ORDER_LINE ON;
        INSERT INTO CoogTechSolutions.dbo.SERVICE_ORDER_LINE (ORDER_ID, SERVICE_DATE, ITEM_QTY, ITEM_COST, LABOR_HOURS)
        VALUES (?,?,?,?,?)
        ''', row.ORDER_ID, row.SERVICE_DATE, row.ITEM_QTY, row.ITEM_COST, row.LABOR_HOURS)
###################################################################################################################    
connection.commit()


#menu()
