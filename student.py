from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import sqlite3


root = Tk()
root.title("Student Management System")
#root.iconbitmap("C:/Users/HP/Downloads/Toma4025-Rumax-Camera.ico")  
root.geometry("400x400")

#Create Database
student = sqlite3.connect("Student_Info.db")

#create Table
'''
c = student.cursor()
c.execute("""create table info (
             first_name text,
             last_name text,
             address text,
             mob_no integer,
             parent_mob_no integer,
             fees_paid integer,
             blood_group text
         )""")
'''

def submit():
    student = sqlite3.connect("Student_Info.db")
    c = student.cursor()
    
    c.execute("INSERT INTO info VALUES(:first_name, :last_name, :address, :mob_no, :parent_mob_no, :fees_paid, :blood_group)",
              {
                  'first_name':first_name.get(),
                  'last_name' : last_name.get(),
                  'address' : address.get(),
                  'mob_no' : mob_no.get(),
                  'parent_mob_no' : parent_mob_no.get(),
                  'fees_paid' : fees_paid.get(),
                  'blood_group' : blood_group.get()
              }
             )
    student.commit()
    student.close()
    
    #clear the input
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    mob_no.delete(0,END)
    parent_mob_no.delete(0,END)
    fees_paid.delete(0,END)
    blood_group.delete(0,END)
    
def show():
    show_info = Toplevel()
    
    student = sqlite3.connect("Student_Info.db")
    
    c = student.cursor()
    
    c.execute("SELECT *,oid FROM info")
    infos = c.fetchall()
    print_record =""
    #print(infos)
    for record in infos:
        print_record += str(record) +"\n"
        
    show_label = Label(show_info,text=print_record,anchor=W)
    show_label.grid(row=13,column=1,columnspan=2,pady=(5,0)) 
    
    student.commit()
    student.close()
    
def update():
    edit = Toplevel()
    edit.title("Update Record")
    edit.geometry("400x400")
    
    student = sqlite3.connect("Student_Info.db")
    
    c = student.cursor()
    
    update_id = single_entry.get()
    c.execute("SELECT * FROM info WHERE oid = "+ update_id)
    
    infos = c.fetchall()
    
    global first_name_edit
    global last_name_edit
    global address_edit
    global mob_no_edit
    global parent_mob_no_edit
    global fees_paid_edit
    global blood_group_edit
    
    #create text box 
    first_name_edit = Entry(edit,width=30)
    first_name_edit.grid(row=0,column=1,padx=20,pady=(10,0))
    last_name_edit = Entry(edit,width=30)
    last_name_edit.grid(row=1,column=1)
    address_edit = Entry(edit,width=30)
    address_edit.grid(row=2,column=1)
    mob_no_edit = Entry(edit,width=30)
    mob_no_edit.grid(row=3,column=1)
    parent_mob_no_edit = Entry(edit,width=30)
    parent_mob_no_edit.grid(row=4,column=1)
    fees_paid_edit = Entry(edit,width=30)
    fees_paid_edit.grid(row=5,column=1)
    blood_group_edit = Entry(edit,width=30)
    blood_group_edit.grid(row=6,column=1)
    
    #create Text Box Labels 
    f_name_label = Label(edit,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label = Label(edit,text="Last Name")
    l_name_label.grid(row=1,column=0)
    address_name_label = Label(edit,text="Address")
    address_name_label.grid(row=2,column=0)
    mob_no_label = Label(edit,text="Mobile Number")
    mob_no_label.grid(row=3,column=0)
    parent_mob_no_edit_label = Label(edit,text="Parent Mobile Number")
    parent_mob_no_edit_label.grid(row=4,column=0)
    fees_paid_edit_label = Label(edit,text="Fees Paid")
    fees_paid_edit_label.grid(row=5,column=0)
    blood_group_edit_label = Label(edit,text="Blood Group")
    blood_group_edit_label.grid(row=6,column=0)
     
    for info in infos:
        first_name_edit.insert(0,info[0])
        last_name_edit.insert(0,info[1])
        address_edit.insert(0,info[2])
        mob_no_edit.insert(0,info[3])
        parent_mob_no_edit.insert(0,info[4])
        fees_paid_edit.insert(0,info[5])
        blood_group_edit.insert(0,info[6])
        
    save_b = Button(edit,text="Save Info",command=save_update)
    save_b.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=135)
    exit_b = Button(edit,text="Exit",command=edit.destroy)
    exit_b.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=135)
    
def save_update():
    student  = sqlite3.connect("Student_Info.db")
    
    c = student.cursor()
    
    update_id = single_entry.get()
    
    c.execute("""UPDATE info SET
                first_name = :first,
                last_name = :last,
                address = :address,
                mob_no = :mob_no,
                parent_mob_no = :p_mob_no,
                fees_paid = :fees,
                blood_group = :bg
                
                WHERE oid = :oid""",
              {
                  'first':first_name_edit.get(),
                  'last' : last_name_edit.get(),
                  'address' : address_edit.get(),
                  'mob_no' : mob_no_edit.get(),
                  'p_mob_no' : parent_mob_no_edit.get(),
                  'fees' : fees_paid_edit.get(),
                  'bg' : blood_group_edit.get(),  
                  'oid': update_id
              })
    
    #commit Changes 
    student.commit()

    #close connection
    student.close()
    
    first_name_edit.delete(0,END)
    last_name_edit.delete(0,END)
    address_edit.delete(0,END)
    mob_no_edit.delete(0,END)
    parent_mob_no_edit.delete(0,END)
    fees_paid_edit.delete(0,END)
    blood_group_edit.delete(0,END) 
    
def delete():
    student = sqlite3.connect("Student_Info.db")
    
    c = student.cursor()
    
    c.execute("DELETE FROM info WHERE oid = "+ single_entry.get())
    
    single_entry.delete(0,END)
    student.commit()
    
    student.close()
    
#Create Entry
first_name = Entry(root,width=30)
first_name.grid(row=1,column=1,pady=(20,0),padx=(15,0))
last_name = Entry(root,width=30)
last_name.grid(row=2,column=1,padx=(15,0))
address = Entry(root,width=30)
address.grid(row=3,column=1,padx=(15,0))
mob_no = Entry(root,width=30)
mob_no.grid(row=4,column=1,padx=(15,0))
parent_mob_no = Entry(root,width=30)
parent_mob_no.grid(row=5,column=1,padx=(15,0))
fees_paid = Entry(root,width=30)
fees_paid.grid(row=6,column=1,padx=(15,0))
blood_group = Entry(root,width=30)
blood_group.grid(row=7,column=1,padx=(15,0))
single_entry = Entry(root,width=30)
single_entry.grid(row=10,column=1,padx=(15,0))


#create Entry Labels 
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=1,column=0,pady=(20,0),padx=(10,0))
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=2,column=0,padx=(10,0))
address_name_label = Label(root,text="Address")
address_name_label.grid(row=3,column=0,padx=(10,0))
mob_no_label = Label(root,text="Student Mob.No.")
mob_no_label.grid(row=4,column=0,padx=(10,0))
Parent_mob_no_label = Label(root,text="Parent Mob.No.")
Parent_mob_no_label.grid(row=5,column=0,padx=(10,0))
fees_paid_label = Label(root,text="Fees Paid")
fees_paid_label.grid(row=6,column=0,padx=(10,0))
blood_group_label = Label(root,text="Blood Group")
blood_group_label.grid(row=7,column=0,padx=(10,0))
single_entry_label = Label(root,text="Enter Roll No")
single_entry_label.grid(row=10,column=0,padx=(10,0))

#Create Buttons
add_student = Button(root,text="Add Student Info",command=submit)
add_student.grid(row=8,column=1,ipadx=64.5,pady=(10,0))

show_student = Button(root,text="Show Student Info",command=show)
show_student.grid(row=9,column=1,ipadx=62,pady=(5,10))

update_student = Button(root,text="Update Student Info",command=update)
update_student.grid(row=11,column=1,ipadx=57,pady=(10,0))

delete_student = Button(root,text="Delete Student Info",command=delete)
delete_student.grid(row=12,column=1,ipadx=59.5,pady=(5,0))

exit_student = Button(root,text="Exit",bg="red",command=root.destroy)
exit_student.grid(row=13,column=1,ipadx=59,pady=(5,0))


#commit changes 
student.commit()

#close connection
student.close()


root.mainloop()
