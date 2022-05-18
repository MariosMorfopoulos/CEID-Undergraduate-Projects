from tkinter import *
import socket

window = Tk()
window.geometry("800x550+300+100")
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
sql_1 = "DROP TABLE Projects;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Projects( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, title VARCHAR(150),region VARCHAR(255), category VARCHAR(255), coauthors VARCHAR(255))"
mycursor.execute(sql_2)

#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES 
                        (1, +'WEB DEVELOPMENT HTML JAVASCRIPT NODEJS EXPRESS MONGO',+'Software',+'Easy',+'Freelancer1')"""

mySql_insert_query2 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (2, +'ML LINEAR REGRESSION K MEANS ALGORITHM',+'Software',+'Easy',+'Freelancer2')"""

mySql_insert_query3 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (3, +'DATABASES MYSQL',+'Software',+'Easy',+'Freelancer3')"""

mySql_insert_query4 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (4, +'OPERATION SYSTEMS C',+'Software',+'Easy',+'Freelancer4')"""

mySql_insert_query5 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (5, +'OBJECT ORIENTED WITH C++ ',+'Software',+'Easy',+'Freelancer5')"""

mySql_insert_query6 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (6, +'OBJECT ORIENTED WITH JAVA',+'Software',+'Easy',+'Freelancer6')"""

mySql_insert_query7 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (7, +'ANDROID WITH KOTLIN ',+'Software',+'Medium',+'Freelancer7')"""

mySql_insert_query8 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (8, +'DATABASES POSTGRE SQL',+'Software',+'Medium',+'Freelancer8')"""

mySql_insert_query9 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (9, +'PARALLEL THREADS WITH C++',+'Software',+'Medium',+'Freelancer9')"""

mySql_insert_query10 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (10, +'WEB DEVELOPEMENT WITH ANGULAR PHP AND MYSQL',+'Software',+'Medium',+'Freelancer10')"""

mySql_insert_query11 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (11, +'NETWORKS WITH C',+'Software',+'Medium',+'Freelancer11')"""

mySql_insert_query12 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (12, +'OBJECT ORIENTED WITH C++',+'Software',+'Medium',+'Freelancer12')"""

mySql_insert_query13 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (13, +'VLSI',+'Hardware',+'Medium',+'Freelancer13')"""

mySql_insert_query14 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (14, +'DIGITAL COMMUNICATIONS WITH MATLAB',+'Hardware',+'Medium',+'Freelancer14')"""

mySql_insert_query15 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (15, +'MICROELECTRONICS WITH C',+'Hardware',+'Medium',+'Freelancer15')"""

mySql_insert_query16 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (16, +'IMAGE PROCESSING WITH MATLAB',+'Hardware',+'Expert',+'Freelancer16')"""

mySql_insert_query17 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (17, +'ROBOTICS WITH C',+'Hardware',+'Expert',+'Freelancer17')"""

mySql_insert_query18 = """INSERT INTO Projects(id, title, region,category,coauthors)
                        VALUES
                        (18, +'ARDUINO WITH C',+'Hardware',+'Expert',+'Freelancer18')"""


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
print(mycursor.rowcount, "Record inserted successfully into Projects Table")


def search():
  eidos = region.get()
  katigoria = category.get()
  mycursor.execute("""SELECT title,coauthors FROM Projects WHERE region=%s and category=%s  """,(eidos,katigoria))
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



lbl=Label(window, text="Search For Project", fg='red', font=("Helvetica", 26))
lbl.place(x=360, y=50, anchor="center")

lbl=Label(window, text="Search The Region And Category you Prefer", fg='Black', font=("Helvetica", 30))
lbl.place(x=80, y=90)



region = StringVar()
textBox1 = Entry(window, textvar = region, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 185, y = 150)

lbl=Label(window, text="   CATEGORY HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=80, y=170, anchor="center")

category = StringVar()
textBox1 = Entry(window, textvar = category, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 550, y = 150)

lbl=Label(window, text="REGION HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=440, y=160, anchor="center")


     
btn=Button(window, text="Search", fg='blue',command = search)
btn.grid(row=13, column=1, columnspan=1, pady=10, padx=10, ipadx=137)
btn.place(x=80, y=330)


window.mainloop()







