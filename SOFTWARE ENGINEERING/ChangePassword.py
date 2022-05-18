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
#sql_2 = "CREATE TABLE IF NOT EXISTS xrhstes( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(150) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL)"
#mycursor.execute(sql_2)

#Με την συνάρτηση αυτη αλλάζουμε τα στοιχεια χρηστη(user/company) στην βάση δεδομένων.
def update():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = username1.get()
    Pass = password.get()
    mycursor.execute("""UPDATE xrhstes  SET  password=%s WHERE username=%s""", (Pass,username))
    results = mycursor.fetchall()
    mydb.commit()
    showinfo(title = "success", message = "Update Succesfully")
    mydb.close()


label1 = Label(window, text = " Change Password  Form ", fg = "black", font = ("new times roman", 20, "bold"))
label1.place(x = 200, y = 15)

label21 = Label(window, text = "Enter  New Username :", font = ("arial", 10, "bold"))
label21.place(x = 110, y = 160)

username1 = StringVar()
textBox1 = Entry(window, textvar = username1, width = 30, font = ("arial", 10, "bold"))
textBox1.place(x = 290, y = 150)

label2 = Label(window, text = "Enter old Password :", font = ("arial", 10, "bold"))
label2.place(x = 110, y = 180)

# userpasswordOld = StringVar()
# textBox1 = Entry(window, textvar = userpasswordOld, width = 30, font = ("arial", 10, "bold"))
# textBox1.place(x = 290, y = 180)

label3 = Label(window, text = "Enter new Password :", font = ("arial", 10, "bold"))
label3.place(x = 110, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

# label4 = Label(window, text = "Enter new Password again:", font = ("arial", 10, "bold"))
# label4.place(x = 110, y = 350)

# password1 = StringVar()
# textBox3 = Entry(window, textvar = password1, width = 30, font = ("arial", 16, "bold"))
# textBox3.place(x = 390, y = 350)

button1 = Button(window, text = "Update", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = update)
button1.place(x = 335, y = 440)

#display window
window.mainloop()
