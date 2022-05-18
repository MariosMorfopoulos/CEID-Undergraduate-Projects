from tkinter import *
from tkinter.messagebox import showinfo,showerror

window = Tk()
window.geometry("800x500+300+100")
window.minsize(800, 500)
window.maxsize(1800, 1500)
window.title(" RAZ Tech")


#USE MYSQL Connection 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Morfopoulos.",
  database="POIROT"
)

mycursor = mydb.cursor()

#Εδω φτιαχνουμε τον πινακα για το Login_Company.py
sql_1 = "DROP TABLE Company;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Company( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, onoma VARCHAR(150),password VARCHAR(255))"
mycursor.execute(sql_2)



#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Company(id, onoma, password) VALUES (1, +'Company1',+'4567')"""

mySql_insert_query2 = """INSERT INTO Company (id, onoma, password) VALUES (2, +'Company2',+'1234')"""

mySql_insert_query3 = """INSERT INTO Company (id, onoma, password) VALUES (3,+'Company3',+'8900')"""

mySql_insert_query4 = """INSERT INTO Company (id, onoma, password) VALUES (4, +'Company4',+'4933')"""

mySql_insert_query5 = """INSERT INTO Company (id, onoma, password) VALUES (5, +'Company5',+'1290')"""



mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)
mycursor.execute(mySql_insert_query5)



mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Company Table")





#Με την συνάρτηση αυτη ελέγχουμε αν υπάρχει εταιρεια(company) στην βάση δεδομένων.
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    companyname = onoma.get()
    Pass = password.get()
    LoginToDatabase=False
    mycursor.execute("""SELECT * FROM company WHERE onoma =%s and password =%s""", (companyname,Pass))
    results = mycursor.fetchall()
    #print(results)
    for x in results:
        if companyname==x[1] and Pass==x[2]:
            LoginToDatabase=True
        if LoginToDatabase==True:
            showinfo(title = "success", message = "Name and password correct")
            import Company_Menu
        else:
            LoginToDatabase=False
            showerror(title = "warning", message = "incorrect name or password")
        
    mycursor.close()
    mydb.commit()
    mydb.close()



label1 = Label(window, text = " Login Company System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "Company Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

onoma = StringVar()
textBox1 = Entry(window, textvar = onoma, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Company Password:", font = ("arial", 16, "bold"))
label3.place(x = 80, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)


#display window
window.mainloop()
