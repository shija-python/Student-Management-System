from tkinter import*
import stdDB_BackEnd
from tkinter import ttk
import tkinter.messagebox
import random
import datetime
import time
import tempfile, os

#FrontEnd

root = Tk()
root.title("STUDENT DATABASE MANAGEMENT SYSTEM")
root.geometry('1300x1300')
root.resizable(width=False , height=False)

StdID = StringVar()
Firstname = StringVar()
Surname = StringVar()
DoB = StringVar()
Age = StringVar()
Gender = StringVar()
Address= StringVar()
Mobile = StringVar()

#==================================FRAMES=======================================
MainFrame = Frame(root,width =1295, height =1295, bd=10, relief=RIDGE, bg="cadet blue")
MainFrame.grid()

TopFrame = Frame(root, width =1275, height =1295, bd = 8, relief=RIDGE)
TopFrame.place(x=10, y=10)
TitleFrame = Frame(root, width =1256, height =130, bd =10, relief=RIDGE)
TitleFrame.place(x=20, y=20)

TopFrame1 = Frame(root, width =1255, height =550, bd =10, relief=RIDGE, bg="cadet blue")
TopFrame1.place(x=20, y=150)

LeftFrame = Frame(TopFrame1, width =400, height =417, bd =10, relief=RIDGE)
LeftFrame.place(x=0, y=0)
RightFrame = Frame(TopFrame1, width =832, height =417, bd =10, relief=RIDGE)
RightFrame.place(x=403, y=0)


ButtonFrame = Frame(TopFrame1, width =1235, height =100, bd =10, relief=RIDGE)
ButtonFrame.place(x=0 , y=420)

#=======================================TITLE==============================================

Title = Label(TitleFrame, font=('arial', 53,'bold'), text="STUDENT MANAGEMENT SYSTEM", bd=10)
Title.place(x=25 ,y=10)

#====================================== FUNCTIONS ===================================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Student Management System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def iReset():
    txtStdID.delete(0, END)
    txtFirstname.delete(0, END)
    txtSurname.delete(0, END)
    txtDoB.delete(0, END)
    txtAge.delete(0, END)
    cboGender.set("")
    txtAddress.delete(0, END)
    txtMobile.delete(0, END)

def addData():
    if StdID.get() =="" or Firstname.get() =="" or Surname.get() =="":
        tkinter.messagebox.askyesno("Student Management System","Enter correct data please")

    else:
        stdDB_BackEnd.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())

        super(studentlist, self).delete()
        studentlist.insert(END.StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())

        DisplayData()

def DisplayData():
    result = stdDB_BackEnd.viewData()
    if len(result)!= 0:
        studentlist.delete(studentlist.get_children())
        for row in result:
            studentlist.insert('',END,values =row)



def StudentRec():
    global sd
    iReset()
    viewInfo = studentlist.focus()
    learnerData = studentlist.item(viewInfo)
    sd = learnerData['values']

    txtStdID.insert(END,sd[1])
    txtFirstname.insert(END,sd[2])
    txtSurname.insert(END,sd[3])
    txtDoB.insert(END,sd[4])
    txtAge.insert(END,sd[5])
    Gender.set(sd[6])
    txtAddress.insert(END,sd[7])
    txtMobile.insert(END,sd[8])

def DeleteData():
    if(len(StdID.get())!=0):
        stdDB_BackEnd.deleteRec(sd[0])
        iReset()
        DisplayData()
        tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")




#==================================LABELS & BUTTONS========================================
lblStdID = Label(LeftFrame, font=('arial', 12, 'bold'), text="Student ID", bd =7)
lblStdID.place(x=0 , y=0)
txtStdID = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=StdID)
txtStdID.place(x=120, y=0)

lblFirstname = Label(LeftFrame, font=('arial', 12, 'bold'), text="Firstname", bd =7)
lblFirstname.place(x=0 , y=45)
txtFirstname = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=Firstname)
txtFirstname.place(x=120, y=45)

lblSurname = Label(LeftFrame, font=('arial', 12, 'bold'), text="Surname", bd =7)
lblSurname.place(x=0 , y=90)
txtSurname = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=Surname)
txtSurname.place(x=120, y=90)

lblDoB = Label(LeftFrame, font=('arial', 12, 'bold'), text="Date of Birth", bd =7)
lblDoB .place(x=0 , y=135)
txtDoB = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=DoB)
txtDoB .place(x=120, y=135)

lblAge = Label(LeftFrame, font=('arial', 12, 'bold'), text="Age", bd =7)
lblAge.place(x=0 , y=180)
txtAge = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=Age)
txtAge.place(x=120, y=180)

Gender = Label(LeftFrame, text="Gender:",font=('arial',12,'bold'), bd=5)
Gender.place(x=0, y=225)
cboGender = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), width=26, state='readonly', textvariable=Gender)
cboGender['values']= ('', 'Male', 'Female')
cboGender.current(0)
cboGender.place(x=120, y=225)

lblAddress = Label(LeftFrame, font=('arial', 12, 'bold'), text="Address", bd =7)
lblAddress.place(x=0 , y=270)
txtAddress = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=Address)
txtAddress.place(x=120, y=270)

lblMobile = Label(LeftFrame, font=('arial', 12, 'bold'), text="Mobile", bd =7)
lblMobile.place(x=0 , y=315)
txtMobile = Entry(LeftFrame, font=('arial',12,'bold'), bd=5, width=26, textvariable=Mobile)
txtMobile.place(x=120, y=315)

#=======================================TREE VIEW====================================================
column = ('no','stdid','firstname','surname','dob','age','gender','address','mobile')

tree = ttk.Treeview(RightFrame, column=column, show='headings')

tree.heading('no', text='No')
tree.heading('stdid', text='Student ID')
tree.heading('firstname', text='Firstname')
tree.heading('surname', text='Surname')
tree.heading('dob', text='Date of Birth')
tree.heading('age', text='Age')
tree.heading('gender', text='Gender')
tree.heading('address', text='Address')
tree.heading('mobile', text='Mobile')


tree.column("no", width=10)
tree.column("stdid", width=10)
tree.column("firstname", width=10)
tree.column("surname", width=10)
tree.column("dob", width=10)
tree.column("age", width=10)
tree.column("gender", width=10)
tree.column("address", width=10)
tree.column("mobile", width=10)

tree.place(x=0,y=0, height=395, width=810)

#======================================= BUTTONS ================================================
btnAddNew = Button(ButtonFrame, bd=4, font=('arial',20, 'bold'), text="Add New", width=12,height=2, command=addData)
btnAddNew.place(x=10, y=0)

btnDisplay = Button(ButtonFrame, bd=4, font=('arial',20, 'bold'), text="Display", width=13,height=2, command=DisplayData)
btnDisplay.place(x=240, y=0)

btnDelete = Button(ButtonFrame, bd=4, font=('arial',20, 'bold'), text="Delete", width=13,height=2, command=DeleteData)
btnDelete.place(x=480, y=0)

btnReset = Button(ButtonFrame, bd=4, font=('arial',20, 'bold'), text="Reset", width=13,height=2, command=iReset)
btnReset.place(x=720, y=0)

btnExit = Button(ButtonFrame, bd=4, font=('arial',20, 'bold'), text="Exit", width=13,height=2, command=iExit)
btnExit.place(x=970, y=0)


root.mainloop();