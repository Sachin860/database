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
student_loc=StringVar(root)
sql_value=IntVar()
python=IntVar()
PowerBI=IntVar()
ID.set('')
Mark1.set('')
Mark2.set('')
Mark3.set('')
student_loc.set('select_state')
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
Label(root,text="state").grid(row=5,column=0)
Statelist=['tamilnadu','kerala','goa','mumbai']
OptionMenu(root,student_loc,*Statelist).grid(row=5,column=1)
Label(root,text="course_interseted").grid(row=6,column=0)
Checkbutton(root,variable=sql_value,text="sql",onvalue=1,offvalue=0).grid(row=6,column=1)
Checkbutton(root,variable=python,text="python",onvalue=1,offvalue=0).grid(row=6,column=2)
Checkbutton(root,variable=PowerBI,text="PowerBI",onvalue=1,offvalue=0).grid(row=6,column=3)

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
    loc=student_loc.get()
    ci=[]
    if sql_value.get()==1:
        ci.append('sql')
    if python.get()==1:
        ci.append('python')
    if PowerBI.get()==1:
        ci.append('PowerBI')
    cifinal="-".join(ci)
    insertstudent(idv,Namev,Mark1v,Mark2v,Mark3v,Total,Avg,Grv,loc,cifinal)
    root.destroy()
Button(root,text='Save',command=savetodb).grid(row=7,column=1)
root.mainloop()


