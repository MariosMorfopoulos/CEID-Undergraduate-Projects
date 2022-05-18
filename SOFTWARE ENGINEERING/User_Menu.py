from tkinter import *

window = Tk()
window.geometry("800x500+300+100")
window.minsize(800, 500)
window.maxsize(1800, 1500)
window.title(" RAZ Tech")

lbl=Label(window, text="User Menu", fg='red', font=("Helvetica", 16))
lbl.place(x=360, y=50, anchor="center")

def findjob():
    window.destroy()
    import Search_for_a_Job

def uploadProject():
    window.destroy()
    import UploadProject

def uploadResume():
    window.destroy()
    import UploadCV

def findProject():
    window.destroy()
    import find_project


btn=Button(window, text="Search for a Job", fg='blue',command=findjob)
btn.place(x=80, y=100)
btn=Button(window, text="Upload Resume", fg='blue',command=uploadResume)
btn.place(x=80, y=200)

btn=Button(window, text="Upload Project", fg='blue',command=uploadProject)
btn.place(x=400, y=100)
btn=Button(window, text="Find a Project", fg='blue',command=findProject)
btn.place(x=400, y=200)

window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()