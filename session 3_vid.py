from tkinter import * 
from os import *
from time import sleep
system("cls")

################################################################################

def press(BTN):
    global temp

    if BTN == "Up":
        temp += 1
        temp_LbL.config(text=str(temp)+"℃")
    elif BTN =="Down":
        temp -= 1
        temp_LbL.config(text=str(temp)+"℃")
    
    if temp == 35:
        temp_LbL.config(text=str(temp)+"℃")
        print("Turning On The Cooler...")
        sleep(1)
        system("cls")
    elif temp == 20:
        temp_LbL.config(text=str(temp)+"℃")
        print("Turning Off The Cooler...")
        sleep(1)
        system("cls")


temp = 30

################################################################################

app = Tk()
app.title(" > > > ⚜ ʟαpʈøp cøõʟɛʀ ⚜ < < < ")
app.geometry("110x100")
app.resizable(False,False)
app["background"] = "pink"

# >> >>  >> >> >> >> >>> >> >>> > >> کدای اصلی :) << < <<< << <<< << << << <<  << << #

cooler_LbL = Label(app,
                   text= "Temperature :",
                   bg = "pink",
                   fg= "blue",
                   font=("alias",10))

temp_LbL = Label(app,
                   text= str(temp) + "℃",
                   bg = "pink",
                   fg= "blue",
                   font=("alias",10))

BTN_UP = Button(app,text="⬆",bg="blue",command= lambda: press("Up"))

BTN_DOWN = Button(app,text="⬇",bg="blue",command= lambda: press("Down"))

cooler_LbL.grid(row=1,column=0)
temp_LbL.grid(row=1,column=1)
BTN_UP.grid(row=0,column=0,columnspan=2,sticky=EW)
BTN_DOWN.grid(row=2,column=0,columnspan=2,sticky=EW)

# >> >>  >> >> >> >> >>> >> >>> > >> کدای اصلی :) << < <<< << <<< << << << <<  << << #

app.mainloop()