from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog 
import time
from tkinter.messagebox import showinfo,showerror
import csv
import pyodbc
import psycopg2


root = Tk()
root.title('PythonGuides')
root.geometry('400x200')



#USE MYSQL Connection 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Morfopoulos.",
  database="POIROT"
)

mycursor = mydb.cursor()



#Δημιουργε τον πινακα για τα Project.
sql_3 = "CREATE TABLE IF NOT EXISTS ProjectTable(name VARCHAR(150) NOT NULL UNIQUE, document VARCHAR(255) NOT NULL)"
mycursor.execute(sql_3)


#def open_file():
root.filename = filedialog.askopenfilename(initialdir="/Users/Marios/Desktop", title="Select A File", filetypes=[("all files", "*.*")])
my_label = Label(root, text=root.filename).pack()
with open('/Users/Marios/Desktop/Project.txt',"r",errors='ignore') as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader:
            string = row
            print(string)
            def listToString(s): 
            #Αρχικοποιουμε ενα αδειο string
                str1 = "" 
                #Μετατροπει σε String 
                for ele in s: 
                    str1 += ele  
                    # return string  
                return str1 
            final_string = listToString(string)
            sql = "INSERT INTO ProjectTable (name,document) VALUES (%s, %s)"
            string = ("1o Project",final_string )
            mycursor.execute(sql, string)
            mycursor.fetchall()
            mydb.commit()
showinfo(title = "success", message = "Insert Your Project  Successfully")
mydb.close()
print("DONE")
    

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
