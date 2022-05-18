from tkinter import *

window = Tk()
window.geometry("800x500+300+100")
window.minsize(800, 500)
window.maxsize(1800, 1500)
window.title(" RAZ Tech")

lbl=Label(window, text="COMPANY MENU", fg='red', font=("Helvetica", 16))
lbl.place(x=360, y=50, anchor="center")



def password():
    window.destroy()
    import Change_Password_Company

def find_candidate():
    window.destroy()
    import Company_Find_Candidates

def seminar():
    window.destroy()
    import Company_Find_Seminars






btn=Button(window, text="Change Password of Company", fg='blue',command=password)
btn.place(x=80, y=100)

btn=Button(window, text="Company Seminar", fg='blue',command=seminar)
btn.place(x=80, y=200)

btn=Button(window, text="Find Candidates", fg='blue',command=find_candidate)
btn.place(x=400, y=100)






window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
