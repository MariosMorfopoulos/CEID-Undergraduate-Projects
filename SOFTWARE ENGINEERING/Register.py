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
#Με την συνάρτηση αυτη προσθέτουμε εγγραφή στην βάση δεδομένων.
def register():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = password.get()
    mycursor.execute('INSERT INTO  xrhstes(username,password) VALUES (%s,%s)', (username,Pass))
    mydb.commit()
    showinfo(title = "success", message = "Insert User Successfully")
    mydb.close()


label1 = Label(window, text = " Register Form ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Register   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = register)
button1.place(x = 335, y = 340)

#display window
window.mainloop()
