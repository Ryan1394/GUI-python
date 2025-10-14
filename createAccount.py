from tkinter import * # type: ignore
from tkinter.ttk import Combobox
from tkinter import messagebox
from os import system
from sys import exit
system("cls")

def Check():
    if (ent_name,ent_lastname,ent_age,ent_gender,ent_username,ent_password) != "":
        cf = open(f"s5/{ent_username.get()}'s account.txt","w")
        cf.write(f"Name : {ent_name.get()}\n")
        cf.write(f"LastName : {ent_lastname.get()}\n")
        cf.write(f"Age : {ent_age.get()}\n")
        cf.write(f"Gender : {ent_gender.get()}\n")
        cf.write(f"Username : {ent_username.get()}\n")
        cf.write(f"password : {ent_password.get()}\n")
        cf.write(f"phone number : {ent_phoneNumber.get()}\n")
        cf.write(f"Email/Gmail : {ent_EMAiL.get()}\n")
        cf.close()

        messagebox.showwarning(title="Data saved",message=f"{ent_name.get()}'s data has been saved sucsessfully in a \"txt\" file!")
        exit()

acc = Tk()
acc.title(" Register Page v.2.0.0 ")
acc.geometry("350x275")
acc["bg"] = "cyan"


l_name = Label(acc,text="name : ",bg="cyan",font=("",12),pady=2)
l_lastname = Label(acc,text="lastname : ",bg="cyan",font=("",12),pady=2)
l_age = Label(acc,text="age : ",bg="cyan",font=("",12),pady=2)
l_gender = Label(acc,text="gender : ",bg="cyan",font=("",12),pady=2)
l_username = Label(acc,text="username : ",bg="cyan",font=("",12),pady=2)
l_password = Label(acc,text="password : ",bg="cyan",font=("",12),pady=2)
l_phoneNumber = Label(acc,text="Phone Number : ",bg="cyan",font=("",12),pady=2)
l_EMAiL = Label(acc,text="Email/Gmail : ",bg="cyan",font=("",12),pady=2)

ent_name = Entry(acc,font=("",10))
ent_lastname = Entry(acc,font=("",10))
ent_age = Spinbox(acc,from_=5,to=50,font=("",12))
ent_gender = Combobox(acc,values=("Female","Male","Not saying"),font=("",12))
ent_username = Entry(acc,font=("",10))
ent_password = Entry(acc,font=("",10))
ent_phoneNumber = Entry(acc,font=("",10))
ent_EMAiL = Entry(acc,font=("",10))

SAVE = Button(acc,text="Check",width=10,height=2,bg="Blue",fg="white",command=Check)

# - - -- - -- - -- - - -- GRID  - - -- - -- - -- - - -- #

l_name.grid(row=0,column=0)
l_lastname.grid(row=1,column=0)
l_age.grid(row=2,column=0)
l_gender.grid(row=3,column=0)
l_username.grid(row=4,column=0)
l_password.grid(row=5,column=0)
l_phoneNumber.grid(row=6,column=0)
l_EMAiL.grid(row=7,column=0)

ent_name.grid(row=0,column=1)
ent_lastname.grid(row=1,column=1)
ent_age.grid(row=2,column=1)
ent_gender.grid(row=3,column=1)
ent_username.grid(row=4,column=1)
ent_password.grid(row=5,column=1)
ent_phoneNumber.grid(row=6,column=1)
ent_EMAiL.grid(row=7,column=1)

SAVE.grid(row=9,column=1,pady=1)

# - - -- - -- - -- - - -- GRID  - - -- - -- - -- - - -- #

acc.mainloop()