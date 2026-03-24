from tkinter import *
import database 

database.connect()

root = Tk()
root.title("Student Management System")
root.geometry("650x400")

name = StringVar()
roll = StringVar()
course = StringVar()
marks = StringVar()

def add_student():
    database.insert(name.get(), roll.get(), course.get(), marks.get())
    view_students()
    clear_fields()

def view_students():
    student_list.delete(0, END)
    for row in database.view():
        student_list.insert(END, row)

def delete_student():
    selected = student_list.get(ACTIVE)
    database.delete(selected[0])
    view_students()

def clear_fields():
    name.set("")
    roll.set("")
    course.set("")
    marks.set("")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Roll No").grid(row=1, column=0)
Label(root, text="Course").grid(row=2, column=0)
Label(root, text="Marks").grid(row=3, column=0)

Entry(root, textvariable=name).grid(row=0, column=1)
Entry(root, textvariable=roll).grid(row=1, column=1)
Entry(root, textvariable=course).grid(row=2, column=1)
Entry(root, textvariable=marks).grid(row=3, column=1)

Button(root, text="Add Student", command=add_student).grid(row=4, column=0)
Button(root, text="View Students", command=view_students).grid(row=4, column=1)
Button(root, text="Delete Student", command=delete_student).grid(row=4, column=2)

student_list = Listbox(root, width=90)
student_list.grid(row=5, column=0, columnspan=3)

root.mainloop()
