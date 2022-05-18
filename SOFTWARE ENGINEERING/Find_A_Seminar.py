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



#Εδω φτιαχνουμε τον πινακα για το Find_Project.py
sql_1 = "DROP TABLE Seminars;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Seminars( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, onoma VARCHAR(150),region VARCHAR(255), category VARCHAR(255), salary VARCHAR(255))"
mycursor.execute(sql_2)

#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES 
                        (1, +'SEMINARIO WEB DEVELOPMENT HTML CSS',+'Software',+'Easy',+'120$')"""

mySql_insert_query2 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (2, +'SEMINARIO MACHINE LEARNING',+'Software',+'Easy',+'150$')"""

mySql_insert_query3 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (3, +'SEMINARIO JAVA',+'Software',+'Easy',+'180$')"""

mySql_insert_query4 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (4, +'SEMINARIO C++',+'Software',+'Easy',+'145$')"""

mySql_insert_query5 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (5, +'SEMINARIO C',+'Software',+'Easy',+'167$')"""

mySql_insert_query6 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (6, +'SEMINARIO OBJECT ORIENTED WITH JAVA',+'Software',+'Easy',+'178$')"""

mySql_insert_query7 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (7, +'SEMINARIO WEB DEVELOPMENT PHP  ',+'Software',+'Medium',+'220$')"""

mySql_insert_query8 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (8, +'SEMINARIO ANDROID KOTLIN',+'Software',+'Medium',+'345$')"""

mySql_insert_query9 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (9, +'SEMINARIO WEB DEVELOPMENT NODEJS',+'Software',+'Medium',+'368$')"""

mySql_insert_query10 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (10, +'SEMINARIO WEB DEVELOPEMENT  WITH ANGULAR PHP AND MYSQL',+'Software',+'Medium',+'475$')"""

mySql_insert_query11 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (11, +'SEMINARIO EISAGWGHS NETWORKS',+'Software',+'Medium',+'250%')"""

mySql_insert_query12 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (12, +'SEMINARIO TYPESCRIPT',+'Software',+'Medium',+'730$')"""

mySql_insert_query13 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (13, +'SEMINARIO EISAGWGHS STA VLSI',+'Hardware',+'Medium',+'390$')"""

mySql_insert_query14 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (14, +'SEMINARIO EISAGWGHS DIGITAL COMMUNICATIONS WITH MATLAB',+'Hardware',+'Medium',+'600$')"""

mySql_insert_query15 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (15, +'SEMINARIO EISAGWGHS MICROELECTRONICS WITH C',+'Hardware',+'Medium',+'700$')"""

mySql_insert_query16 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (16, +'SEMINARIO EISAGWGHS IMAGE PROCESSING WITH MATLAB',+'Hardware',+'Expert',+'550$')"""

mySql_insert_query17 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (17, +'SEMINARIO EISAGWGHS ROBOTICS WITH C',+'Hardware',+'Expert',+'450$')"""

mySql_insert_query18 = """INSERT INTO Seminars(id, onoma, region,category,salary)
                        VALUES
                        (18, +'SEMINARIO EISAGWGHS ARDUINO WITH C',+'Hardware',+'Expert',+'300$')"""


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
print(mycursor.rowcount, "Record inserted successfully into Seminars Table")






def search():
  eidos = perioxi.get()
  katigoria = category.get()
  mycursor.execute("""SELECT onoma,salary FROM Seminars WHERE region=%s and category=%s  """,(eidos,katigoria))
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






lbl=Label(window, text="Search For A Seminar", fg='red', font=("Helvetica", 26))
lbl.place(x=360, y=50, anchor="center")

lbl=Label(window, text="Search The Region And Category you Prefer", fg='Black', font=("Helvetica", 30))
lbl.place(x=80, y=90)



perioxi = StringVar()
textBox1 = Entry(window, textvar = perioxi, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 185, y = 150)

lbl=Label(window, text="REGION HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=90, y=160, anchor="center")

category = StringVar()
textBox1 = Entry(window, textvar = category, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 550, y = 150)

lbl=Label(window, text="CATEGORY HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=440, y=160, anchor="center")


     
btn=Button(window, text="Search", fg='blue',command = search)
btn.grid(row=13, column=1, columnspan=1, pady=10, padx=10, ipadx=137)
btn.place(x=80, y=330)


window.mainloop()