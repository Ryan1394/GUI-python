from tkinter import * # type: ignore
from os import system
system("cls")

def check(Btn):
    global calculate
    calculate = calculate + Btn
    inpu_text.set(calculate)

def Check():
    global calculate
    result = eval(calculate)
    calculate = result
    inpu_text.set(calculate)
    calculate = ""

def clear():
    global calculate
    calculate = ""
    inpu_text.set(calculate)

def lastclear():
    global calculate
    ent.delete(len(ent.get())-1)
    calculate = ent.get()
    inpu_text.set(calculate)


calculate = ""

root = Tk()
root.geometry("260x335")
root.title("Calculator")
root.resizable(False,False)

inpu_text = StringVar()
ent = Entry(root,textvariable=inpu_text,font=("alias",14))
btn_0 = Button(root,text="0",bg="gray",width=8,height=3,command = lambda: check("0"))
btn_1 = Button(root,text="1",bg="gray",width=8,height=3,command = lambda: check("1"))
btn_2 = Button(root,text="2",bg="gray",width=8,height=3,command = lambda: check("2"))
btn_3 = Button(root,text="3",bg="gray",width=8,height=3,command = lambda: check("3"))
btn_4 = Button(root,text="4",bg="gray",width=8,height=3,command = lambda: check("4"))
btn_5 = Button(root,text="5",bg="gray",width=8,height=3,command = lambda: check("5"))
btn_6 = Button(root,text="6",bg="gray",width=8,height=3,command = lambda: check("6"))
btn_7 = Button(root,text="7",bg="gray",width=8,height=3,command = lambda: check("7"))
btn_8 = Button(root,text="8",bg="gray",width=8,height=3,command = lambda: check("8"))
btn_9 = Button(root,text="9",bg="gray",width=8,height=3,command = lambda: check("9"))
btn_dot = Button(root,text=".",bg="gray",width=8,height=3,command = lambda: check("."))
btn_sum = Button(root,text="+",bg="orange",width=8,height=3,command = lambda: check("+"))
btn_min = Button(root,text="-",bg="orange",width=8,height=3,command = lambda: check("-"))
btn_multi = Button(root,text="x",bg="orange",width=8,height=3,command = lambda: check("x"))
btn_div = Button(root,text="÷",bg="orange",width=8,height=3,command = lambda: check("÷"))
btn_clear = Button(root,text="C",bg="yellow",width=8,height=3,command=clear)
btn_lastclear = Button(root,text="⏪",bg="red",width=8,height=3,command=lastclear)
btn_eq = Button(root,text="=",bg="blue",width=8,height=3,command=Check)

ent.grid(row=0,column=0,columnspan=4,sticky=EW) #EW #NS
btn_1.grid(row=1,column=0,sticky=EW)
btn_2.grid(row=1,column=1,sticky=EW)
btn_3.grid(row=1,column=2,sticky=EW)
btn_4.grid(row=2,column=0,sticky=EW)
btn_5.grid(row=2,column=1,sticky=EW)
btn_6.grid(row=2,column=2,sticky=EW)
btn_7.grid(row=3,column=0,sticky=EW)
btn_8.grid(row=3,column=1,sticky=EW)
btn_9.grid(row=3,column=2,sticky=EW)
btn_dot.grid(row=4,column=0,sticky=EW)
btn_0.grid(row=4,column=1,sticky=EW)
btn_clear.grid(row=4,column=2,sticky=EW)
btn_eq.grid(row=5,column=0,sticky=EW,columnspan=2)
btn_lastclear.grid(row=5,column=2,sticky=EW,columnspan=2)
btn_sum.grid(row=1,column=3,sticky=EW)
btn_min.grid(row=2,column=3,sticky=EW)
btn_multi.grid(row=3,column=3,sticky=EW)
btn_div.grid(row=4,column=3,sticky=EW)

root.mainloop()