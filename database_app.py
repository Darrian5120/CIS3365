from tkinter import *
from PIL import ImageTk,Image
import pyodbc
import pandas as pd 

root = Tk()
root.title('Herrera Fabricating Inc.')
#root.iconbitmap('/path/to/ico/icon.ico')
root.geometry("800x800")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9PNG3JO;'
                      'Database=CoogTechSolutions;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

sql_query = pd.read_sql_query('SELECT * FROM TestDB.dbo.Person',conn)
print(sql_query)
print(type(sql_query))
#conn = pyodbc.connect('Driver={SQL Server};'
#                        'Server=CoT-CIS3365-05.cougarnet.uh.edu;'
#                        'Database=CoogTechSolutions;'
#                        'UID=;'
#                        'PWD=;'
#                        'Trusted_Connection=no;')
#cursor = conn.cursor()

root.mainloop()

