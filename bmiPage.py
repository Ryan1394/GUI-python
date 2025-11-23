from tkinter import *
from tkinter import messagebox
from os import system
system("cls")

def check():
    ghad = float(ent_ghad.get())
    vazn = float(ent_vazn.get())
    vaznBtavan2 = vazn ** 2
    answer = ghad / vaznBtavan2
    BMi = answer * 10000
    if BMi < 18.5:
        messagebox.showinfo(title="BMi وضعیت",message=f"Bmi: {BMi} ، شما زیر 18.5 است \nو شما چاقی بسیار کمی دارید Bmi وضعیت")
    elif BMi >= 18.5 and BMi<=24.5:
        messagebox.showinfo(title="BMi وضعیت",message=f"است و خیلی خوب است {BMi} شما  Bmi وضعیت")
    elif BMi > 24.5 and BMi <= 29.5:
        messagebox.showinfo(title="BMi وضعیت",message=f"است که نشان میدهد کمی چاق هستید {BMi} Bmi وضعیت")
    elif BMi > 29.5 and BMi <= 35:
        messagebox.showinfo(title="BMi وضعیت",message=f"O: است و این نشان میدهد شما اضافه وزن دارید {BMi} شما Bmi وضعیت")
    else :
        messagebox.showwarning(title="BMi وضعیت",message="|: وضعیت چاقی ناسالم")


app = Tk()
app.geometry("425x425")
app["bg"] = "light blue"

lBl_vazn = Label(app,text="وزن خود را وارد کنید",font=("alias",15),bg="light blue")
lBl_vazn.place(x=1,y=15)

ent_vazn = Entry(app,font=("alias",15))
ent_vazn.place(x=165,y=15)

lBl_ghad = Label(app,text="قد خود را وارد کنید",font=("alias",15),bg="light blue")
lBl_ghad.place(x=1,y=75)

ent_ghad = Entry(app,font=("alias",15))
ent_ghad.place(x=165,y=75)

btn_bmi = Button(app,text="بررسی کردن",command=check)
btn_bmi.place(x=163,y=162)

app.mainloop()