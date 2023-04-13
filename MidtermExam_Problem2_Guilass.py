from tkinter import *

class MyName:
    def __init__(self, name):
        self.lbl5 = Label(name, text="My Full Name", font=("Verdana", 12, "bold"), fg="red")
        self.lbl5.place(x=200, y=15)

        self.lbl1 = Label(name, text="Enter Given Name:", fg="red")
        self.lbl1.place(x=100, y=60)
        self.lbl2 = Label(name, text="Enter Middle Name:", fg="red")
        self.lbl2.place(x=100, y=90)
        self.lbl3 = Label(name, text="Enter Last Name:", fg="red")
        self.lbl3.place(x=100, y=120)
        self.lbl4 = Label(name, text="My Full Name is:", fg="red")
        self.lbl4.place(x=100, y=170)

        self.txt1 = Entry(name, bd=1)
        self.txt1.place(x=250, y=60)
        self.txt2 = Entry(name, bd=1)
        self.txt2.place(x=250, y=90)
        self.txt3 = Entry(name, bd=1)
        self.txt3.place(x=250, y=120)
        self.txt4 = Entry(name, bd=1, fg="red")
        self.txt4.place(x=250, y=170, width= 200)

        self.btnGivenName = Button(name, text="Show Full Name", bg="white", command=self.fullname)
        self.btnGivenName.place(x=300, y=220, anchor="center")
        self.btnClearAll = Button(name, text="Clear All", bg="white", command=self.clear_all)
        self.btnClearAll.place(x=300, y=255, anchor="center")

    def fullname(self):
        GivenName = self.txt1.get()
        MiddleName = self.txt2.get()
        LastName = self.txt3.get()
        result = f"{LastName}, {GivenName} {MiddleName}"
        self.txt4.delete(0, END)
        self.txt4.insert(END, result)

    def clear_all(self):
        self.txt1.delete(0, END)
        self.txt2.delete(0, END)
        self.txt3.delete(0, END)
        self.txt4.delete(0, END)

window = Tk()
MyWin = MyName(window) # changed to myName
window.geometry("600x400")
window.title("Midterm Exam Problem 2")
window.mainloop()