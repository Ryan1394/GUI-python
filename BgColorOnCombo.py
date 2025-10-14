from tkinter import * # type: ignore
from tkinter.ttk import Combobox
from os import system
from tkinter import messagebox
system("cls")

def ChangeColor(event):
    try:
        app.configure(bg=ComboWIDGET.get())
        messagebox.showwarning(title="Change Color",message=f"Color successfully changed to {ComboWIDGET.get()}")
    except:
        pass

LiSTofCOLORsCoMbObOx = [
    "Choose Color",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "cyan",
    "purple",
    "pink",
    "brown",
    "black"
]


app = Tk()
app.geometry("375x350")
app.resizable(False,False)
app.title(" Change Color With Combobox ")
app["bg"]= "white"

ComboWIDGET = Combobox(app,textvariable="",values=LiSTofCOLORsCoMbObOx) # type: ignore
ComboWIDGET.current(0)
ComboWIDGET.bind("<<ComboboxSelected>>",ChangeColor)
ComboWIDGET.grid(row=0,column=0,pady=5,padx=10,columnspan=5)

app.mainloop()