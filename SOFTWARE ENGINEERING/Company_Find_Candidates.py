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

#Εδω φτιαχνουμε τον πινακα για το Company_Find_Candidates.py
sql_1 = "DROP TABLE Candidates;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Candidates( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, onoma VARCHAR(150),idiotita VARCHAR(255),salary VARCHAR(255),empiria VARCHAR(255))"
mycursor.execute(sql_2)


#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (1, +'Candidate 1',+'Programmatistis',+'500$',+'Entry Level')"""

mySql_insert_query2 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (2, +'Candidate 2',+'Programmatistis',+'600$',+'Intermediate Level')"""

mySql_insert_query3 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (3, +'Candidate 3',+'Programmatistis',+'900$',+'Mid Level')"""

mySql_insert_query4 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (4, +'Candidate 4',+'Programmatistis',+'1200$',+'Senior Level')"""

mySql_insert_query5 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (5, +'Candidate 5',+'Mixanikos',+'500$',+'Entry Level')"""

mySql_insert_query6 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (6, +'Candidate 6',+'Mixanikos',+'600$',+'Intermediate Level')"""

mySql_insert_query7 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (7, +'Candidate 7',+'Mixanikos',+'900$',+'Mid Level')"""

mySql_insert_query8 = """INSERT INTO Candidates (id, onoma, idiotita,salary,empiria)
                       VALUES
                       (8, +'Candidate 8',+'Mixanikos',+'1200$',+'Senior Level')"""





mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)
mycursor.execute(mySql_insert_query5)
mycursor.execute(mySql_insert_query6)
mycursor.execute(mySql_insert_query7)
mycursor.execute(mySql_insert_query8)



mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Company Table")



def search():
	meros = perioxi.get()
	level = lvl.get()
	mycursor.execute("""SELECT onoma,salary FROM Candidates WHERE idiotita=%s and empiria=%s  """,(meros,level))
	records= mycursor.fetchall()
	print(records)
	#Εδω θα κανουμε loopa για να βγαλουμε τα στοιχεια του Query.
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(window, text=print_records,fg='Black', font=("Helvetica", 20))
	query_label.place(x=80, y=190)
	mydb.commit()
	mydb.close()




lbl=Label(window, text="Search For Candidates", fg='red', font=("Helvetica", 26))
lbl.place(x=360, y=50, anchor="center")

lbl=Label(window, text="Search The Region And Level you Prefer", fg='Black', font=("Helvetica", 30))
lbl.place(x=80, y=90)



perioxi = StringVar()
textBox1 = Entry(window, textvar = perioxi, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 185, y = 150)

lbl=Label(window, text="REGION HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=90, y=160, anchor="center")

lvl = StringVar()
textBox1 = Entry(window, textvar = lvl, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 550, y = 150)

lbl=Label(window, text="LEVEL HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=470, y=160, anchor="center")


     
btn=Button(window, text="Search", fg='blue',command = search)
btn.grid(row=13, column=1, columnspan=1, pady=10, padx=10, ipadx=137)
btn.place(x=80, y=330)


window.mainloop()