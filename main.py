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
            print("Add new Table")
            cursor = connection.cursor()
            ############Paste sql code here#################
            create_table = """
                
            """
            ################################################
            cursor.execute(create_table)
        # remove table
        if command == 'd':
            print("Remove table")
            cursor = connection.cursor()
            ############Paste sql code here#################
            remove_table = """
                DROP TABLE [dbo].[SERVICE_ORDER_LINE]
            """
            ################################################
            cursor.execute(remove_table)

        # insert element in table
        if command == 'i':           
            print("Fill elements from excel file")
            #user_file = str(input("Enter filename(example.xlsx): "))
            #table_name = str(input("Enter table name(Customer): "))
            data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\Customer.xlsx")   
            df = pd.DataFrame(data)
            df = df.fillna(value=0)
            print(df)
            cursor = connection.cursor()
            for row in df.itertuples():
                cursor.execute('''
                            SET IDENTITY_INSERT [dbo].[Customer] OFF;
                            INSERT INTO CoogTechSolutions.dbo.Customer (ORDER_ID, SERVICE_ID, C_FNAME, C_LNAME, C_BUSINESS_NAME)
                            VALUES (?,?,?,?,?,?)
                            ''', row.ORDER_ID, row.SERVICE_ID, row.C_FNAME, row.C_LNAME, row.C_BUSINESS_NAME)
            connection.commit()
            
        # remove element in table
        if command == 'r':           
            print("Remove Element")
            
        # update element in table
        if command == 'u':           
            print("Update Element")
            
        # Print entire table    
        if command == 'o':
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
print(df)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.Customer OFF;
        INSERT INTO CoogTechSolutions.dbo.Customer (ORDER_ID, SERVICE_ID, C_FNAME, C_LNAME, C_BUSINESS_NAME)
        VALUES (?,?,?,?,?)
        ''', row.ORDER_ID, row.SERVICE_ID, row.C_FNAME, row.C_LNAME, row.C_BUSINESS_NAME)
connection.commit()

data = pd.read_excel(r"C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Records\FINSIHED_ORDER.xlsx")   
df = pd.DataFrame(data)
print(df)
cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute('''
        SET IDENTITY_INSERT CoogTechSolutions.dbo.FINSIHED_ORDER ON;
        INSERT INTO CoogTechSolutions.dbo.FINISHED_ORDER (ORDER_ID, DATE_START, DATE_END, Quality)
        VALUES (?,?,?)
        ''', row.DATE_START, row.DATE_END, row.Quality)
connection.commit()

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
