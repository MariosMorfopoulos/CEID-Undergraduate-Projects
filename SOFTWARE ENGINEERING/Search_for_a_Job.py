from tkinter import *
import socket

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

#Εδω φτιαχνουμε τον πινακα για το Search_for_Job.py
sql_1 = "DROP TABLE Jobs;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Jobs( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, onoma VARCHAR(150),perioxi VARCHAR(255),salary VARCHAR(255),eidos VARCHAR(255))"
mycursor.execute(sql_2)

#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (1, +'Web Developer Engineer Congity',+'Kifisia',+'900$',+'Software')"""

mySql_insert_query2 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (2, +'Machine Learning Engineer Deloitte',+'Kifisia',+'750$',+'Software')"""

mySql_insert_query3 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (3, +'DevOps Engineer OPAP',+'Marousi',+'800$',+'Software')"""

mySql_insert_query4 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (4, +'Android Engineer Microsoft',+'Marousi',+'850$',+'Software')"""

mySql_insert_query5 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (5, +'Software Engineer Vodafone',+'Marousi',+'1000$',+'Software')"""

mySql_insert_query6 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (6, +'Software Engineer Cosmote',+'Kifisia',+'670$',+'Software')"""

mySql_insert_query7 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (7, +'SQL Engineer Cognity',+'Kifisia',+'600$',+'Software')"""

mySql_insert_query8 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (8, +'System Architecture Manager',+'Marousi',+'1800$',+'Software')"""

mySql_insert_query9 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (9, +'Senior Front End Developer',+'Marousi',+'1100$',+'Software')"""

mySql_insert_query10 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (10, +'Full Stack Web Developer Apple',+'Marousi',+'1500$',+'Software')"""

mySql_insert_query11 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (11, +'Ruby Engineer ',+'Kifisia',+'970$',+'Software')"""

mySql_insert_query12 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (12, +'C++ Engineer',+'Kifisia',+'1000$',+'Software')"""

mySql_insert_query13 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (13, +'VLSI Engineer',+'Kifissia',+'1000$',+'Hardware')"""

mySql_insert_query14 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (14, +'System Architecture Networks',+'Kifisia',+'1000$',+'Hardware')"""

mySql_insert_query15 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (15, +'MicroElectronics Engineer',+'Kifisia',+'1000$',+'Hardware')"""

mySql_insert_query16 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (16, +'Image Processing Engineer',+'Kifisia',+'1000$',+'Hardware')"""

mySql_insert_query17 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (17, +'Robotics Expert',+'Kifisia',+'1000$',+'Hardware')"""

mySql_insert_query18 = """INSERT INTO Jobs (id, onoma, perioxi,salary,eidos)
                       VALUES
                       (18, +'Arduino Senior Manager',+'Kifisia',+'1000$',+'Hardware')"""

mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)
mycursor.execute(mySql_insert_query5)
mycursor.execute(mySql_insert_query6)
mycursor.execute(mySql_insert_query7)
mycursor.execute(mySql_insert_query8)
mycursor.execute(mySql_insert_query9)
mycursor.execute(mySql_insert_query10)
mycursor.execute(mySql_insert_query11)
mycursor.execute(mySql_insert_query12)
mycursor.execute(mySql_insert_query13)
mycursor.execute(mySql_insert_query14)
mycursor.execute(mySql_insert_query15)
mycursor.execute(mySql_insert_query16)
mycursor.execute(mySql_insert_query17)
mycursor.execute(mySql_insert_query18)



mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Jobs Table")
#SOS πρεπει να μπει η SQL σε # λογο του mycursor bug για να τρεξει ο απο κατω κωδικας.


def search():
	meros = perioxi.get()
	job = douleia.get()
	mycursor.execute("""SELECT onoma,salary FROM Jobs WHERE perioxi=%s and eidos=%s  """,(meros,job))
	records= mycursor.fetchall()
	#sql = "SELECT onoma,salary FROM Jobs WHERE perioxi=%s and eidos=%s"
  #mycursor.execute(sql,([(meros,job)]))
  #mycursor.fetchall()
	print(records)
	#Εδω θα κανουμε loopa για να βγαλουμε τα στοιχεια του Query.
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(window, text=print_records,fg='Black', font=("Helvetica", 20))
	query_label.place(x=80, y=190)
	mydb.commit()
	mydb.close()



lbl=Label(window, text="Search For A Job", fg='red', font=("Helvetica", 26))
lbl.place(x=360, y=50, anchor="center")

lbl=Label(window, text="Search The Region And Job you prefer", fg='Black', font=("Helvetica", 30))
lbl.place(x=80, y=90)



perioxi = StringVar()
textBox1 = Entry(window, textvar = perioxi, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 185, y = 150)

lbl=Label(window, text="REGION HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=90, y=160, anchor="center")

douleia = StringVar()
textBox1 = Entry(window, textvar = douleia, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 550, y = 150)

lbl=Label(window, text="JOB HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=490, y=160, anchor="center")


     
btn=Button(window, text="Search", fg='blue',command = search)
btn.grid(row=13, column=1, columnspan=1, pady=10, padx=10, ipadx=137)
btn.place(x=80, y=330)


window.mainloop()