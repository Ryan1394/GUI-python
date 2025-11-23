from tkinter import *
app = Tk()
app.geometry("450x300")
app.title(" BMi CALCULATOR ")
app["bg"] = "cyan"

def check():
    WEiGHT = weight_ENT.get()
    HEiGHT = height_ENT.get()
    WEiGHT = float(WEiGHT)
    HEiGHT = float(HEiGHT)
    HEiGHT2 = HEiGHT * HEiGHT
    answer = WEiGHT / HEiGHT2
    Bmi = answer * 10000
    answr_lBl["text"] = Bmi


weight_lBl = Label(app,text="وزن خود را وارد کنید",font=("Arial",14),bg="cyan")
weight_lBl.place(x=2,y=15)

weight_ENT = Entry(app,font=("arial",10))
weight_ENT.place(x=165,y=15)

height_lBl = Label(app,text="قد خود را وارد کنید",font=("Arial",14),bg="cyan")
height_lBl.place(x=2,y=45)

height_ENT = Entry(app,font=("arial",10))
height_ENT.place(x=165,y=45)

BTN = Button(app,text="حساب کن",font=("alias",15),bg="orange",command=check)
BTN.place(x=160,y=80)

answr_lBl = Label(app,text="",font=("alias",15),bg="cyan")
answr_lBl.place(x=160,y=125)

app.mainloop()