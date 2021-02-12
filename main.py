import datetime
from datetime import date
import pyodbc
import pandas as pd
from tabulate import tabulate

#Menu to create
def menu():
    menu = ('\nMENU\n'
        'a - Add new table\n'
        'd - Remove table\n'
        'i - Insert element\n'
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
            print("Insert Element")
            
         # remove element in table
        if command == 'i':           
            print("Remove Element")
            
        # update element in table
        if command == 'i':           
            print("Update Element")
            
        # Print entire table    
        if command == 'o':
            None
            
                     
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

menu()
