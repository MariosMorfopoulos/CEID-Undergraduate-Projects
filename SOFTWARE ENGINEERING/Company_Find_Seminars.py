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
sql_1 = "DROP TABLE Company_Seminars;"
mycursor.execute(sql_1)
sql_2 = "CREATE TABLE IF NOT EXISTS Company_Seminars( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, onoma VARCHAR(150),region VARCHAR(255), category VARCHAR(255), salary VARCHAR(255))"
mycursor.execute(sql_2)


#Εδω κανουμε τις εγγραφες για τον πινακα
mySql_insert_query1 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES 
                        (1, +'COMPANY 1',+'Software',+'Easy',+'120$')"""

mySql_insert_query2 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (2, +'COMPANY 1',+'Software',+'Easy',+'150$')"""

mySql_insert_query3 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (3, +'COMPANY 1',+'Software',+'Easy',+'180$')"""

mySql_insert_query4 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (4, +'COMPANY 1',+'Software',+'Easy',+'145$')"""

mySql_insert_query5 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (5, +'COMPANY 2',+'Software',+'Easy',+'167$')"""

mySql_insert_query6 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (6, +'COMPANY 2',+'Software',+'Easy',+'178$')"""

mySql_insert_query7 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (7, +'COMPANY 2  ',+'Software',+'Medium',+'220$')"""

mySql_insert_query8 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (8, +'COMPANY 2',+'Software',+'Medium',+'345$')"""

mySql_insert_query9 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (9, +'COMPANY 3',+'Software',+'Medium',+'368$')"""

mySql_insert_query10 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (10, +'COMPANY 3',+'Software',+'Medium',+'475$')"""

mySql_insert_query11 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (11, +'COMPANY 3',+'Software',+'Medium',+'250%')"""

mySql_insert_query12 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (12, +'COMPANY 3',+'Software',+'Medium',+'730$')"""

mySql_insert_query13 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (13, +'COMPANY 4',+'Hardware',+'Medium',+'390$')"""

mySql_insert_query14 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (14, +'COMPANY 4',+'Hardware',+'Medium',+'600$')"""

mySql_insert_query15 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (15, +'COMPANY 4',+'Hardware',+'Medium',+'700$')"""

mySql_insert_query16 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (16, +'COMPANY 4',+'Hardware',+'Expert',+'550$')"""

mySql_insert_query17 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (17, +'COMPANY 5',+'Hardware',+'Expert',+'450$')"""

mySql_insert_query18 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (18, +'COMPANY 5',+'Hardware',+'Expert',+'300$')"""

mySql_insert_query19 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (19, +'COMPANY 5',+'Hardware',+'Expert',+'300$')"""

mySql_insert_query20 = """INSERT INTO Company_Seminars(id, onoma, region,category,salary)
                        VALUES
                        (20, +'COMPANY 5',+'Hardware',+'Expert',+'300$')"""






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
mycursor.execute(mySql_insert_query19)
mycursor.execute(mySql_insert_query20)


mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Company Seminars Table")






def search():
  comp = etaireia.get()
  lefta = salary.get()
  mycursor.execute("""SELECT region,category FROM Company_Seminars WHERE onoma=%s and salary=%s  """,(comp,lefta))
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






lbl=Label(window, text="Search For A Company Seminar", fg='red', font=("Helvetica", 26))
lbl.place(x=360, y=50, anchor="center")

lbl=Label(window, text="Search The Company And Salary you Prefer", fg='Black', font=("Helvetica", 30))
lbl.place(x=80, y=90)



etaireia = StringVar()
textBox1 = Entry(window, textvar = etaireia, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 185, y = 150)

lbl=Label(window, text="COMPANY HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=90, y=160, anchor="center")

salary = StringVar()
textBox1 = Entry(window, textvar = salary, width = 10, font = ("arial", 16, "bold"))
textBox1.place(x = 550, y = 150)

lbl=Label(window, text="SALARY HERE:", fg='Black', font=("Helvetica", 16))
lbl.place(x=440, y=160, anchor="center")


     
btn=Button(window, text="Search", fg='blue',command = search)
btn.grid(row=13, column=1, columnspan=1, pady=10, padx=10, ipadx=137)
btn.place(x=80, y=330)


window.mainloop()


