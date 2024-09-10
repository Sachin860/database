#graphical user  interface
from tkinter import *
from class_new.sql.python_with_sql_ex import insertstudent
root=Tk()
root.title('GUI FIRST')
root.geometry('400x400')
ID=IntVar()
Name=StringVar()
Mark1=IntVar()
Mark2=IntVar()
Mark3=IntVar()
ID.set('')
Mark1.set('')
Mark2.set('')
Mark3.set('')
Label(root,text='student_id').grid(row=0,column=0)
Entry(root,textvariable=ID).grid(row=0,column=1)
Label(root,text='Student_Name').grid(row=1,column=0)
Entry(root,textvariable=Name).grid(row=1,column=1)
Label(root,text="Mark_1").grid(row=2,column=0)
Entry(root,textvariable=Mark1).grid(row=2,column=1)
Label(root,text='Mark_2').grid(row=3,column=0)
Entry(root,textvariable=Mark2).grid(row=3,column=1)
Label(root,text='Mark_3').grid(row=4,column=0)
Entry(root,textvariable=Mark3).grid(row=4,column=1)
def savetodb():
    idv=ID.get()
    Namev=Name.get()
    Mark1v=Mark1.get()
    Mark2v=Mark2.get()
    Mark3v=Mark3.get()
    Total=Mark1v+Mark2v+Mark3v
    Avg=Total/3
    if Total >= 290:
        Grv = 'grade A'
    elif Total < 290 and Total >= 275:
        Grv = 'grade B'
    elif Total < 275 and Total >= 250:
        Grv = 'grade C'
    elif Total < 250 and Total >= 200:
        Grv = 'grade D'
    else:
        Grv = 'grade E'
    insertstudent(idv,Namev,Mark1v,Mark2v,Mark3v,Total,Avg,Grv)
    root.destroy()
Button(root,text='Save',command=savetodb).grid(row=5,column=1)
root.mainloop()


