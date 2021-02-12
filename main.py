import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Connection to MySql DB successful")
    except Error as e:
        print(f"The error '{e}' occured")

    return connection

# Run SQL scripts without return value
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")

# execute statements with return value(cursor)
def connect_cursor(sql_select_Query):
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print(tabulate(records, headers=['id', 'contactDetails', 'creationDate'], tablefmt='psql')) # print contacts in table format
    cursor.close() 

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

        while(command != 'a' and command != 'd' and command != 'u' and command != 'b' and command != 'c' and command != 'o' and command != 'q'): # pause menu when option is selected
            command = input('Choose an option:\n')

        # add new table
        if command == 'a':
            print("Add new contact")
            newID = input("Enter contact id: ")
            newDetails = str(input("Enter contact details: "))
            newDate = str(input("Enter contact date (MM/DD/YYYY): "))
            query = "INSERT INTO contacts (id, contactDetails, creationDate) VALUES (%s, '%s', STR_TO_DATE('%s','%%m/%%d/%%Y'))" % (newID, newDetails, newDate)
            execute_query(connection, query)

        # remove row from table
        if command == 'd':
            print("Remove contact")
            contact_id_to_delete = input("Enter contact id to delete: ")
            delete_statement = "DELETE FROM contacts WHERE id = %s" % (contact_id_to_delete)
            execute_query(connection, delete_statement)

        # update contact details
        if command == 'u':           
            print("Update contact details")
            contact_id_to_update = input("Enter contact id to update: ")
            new_details = str(input("Enter updated details: "))
            update_statement = "UPDATE contacts SET contactDetails = '%s' WHERE id = %s" % (new_details, contact_id_to_update)
            execute_query(connection, update_statement)
            
        # Print entire table    
        if command == 'o':
            sql_select_Query = "SELECT * FROM contacts"
            connect_cursor(sql_select_Query)
            
