from tkinter import * # type: ignore
from tkinter.ttk import Progressbar
from os import system
from tkinter import messagebox
import random
system("cls")

def check():
    global score,DDDDDDdoodleyDU,cXrrXt_answ0r,SOAl,REAL_quetiXn_ORGINIAL,game_WiN,amalgarRiazi
    try:
        answZR = EnterANSWzR.get()
        answZR = int(answZR)
        if answZR != "":
            if answZR == cXrrXt_answ0r:
                print("Answer Correct")
                EnterANSWzR.delete("0",END)
                score += 5
                DDDDDDdoodleyDU +=10
                pBar["value"] = DDDDDDdoodleyDU
                messagebox.showinfo(title="نتیجه پاسخ",message="!پاسخ شما درست است! آفرین")
                NuM1 = random.randint(0,9)
                NuM2 = random.randint(0,9)
                amalgarRiazi = random.randint(1,4)
                if amalgarRiazi == 1:
                    amalgarRiazi = "+"
                    cXrrXt_answ0r = NuM1 + NuM2
                elif amalgarRiazi == 2:
                    amalgarRiazi = "-"
                    cXrrXt_answ0r = NuM1 - NuM2
                elif amalgarRiazi == 3:
                    amalgarRiazi = "x"
                    cXrrXt_answ0r = NuM1 * NuM2
                elif amalgarRiazi == 4:
                    amalgarRiazi = "/"
                    cXrrXt_answ0r = NuM1 / NuM2
                SOAl = f"{NuM1} {amalgarRiazi} {NuM2}"
                REAL_quetiXn_ORGINIAL["text"] = SOAl
                lbl_score["text"] = f"score: {score}"
                if score>=50:
                    game_WiN = Toplevel()
                    game_WiN.geometry("350x350")
                    game_WiN.resizable(False,False)
                    game_WiN["bg"] = "green"

                    lBlwiN = Label(game_WiN,text="!!!تو بردی",bg="green",font=("",random.randint(15,20)))
                    lBlwiN.pack(pady=5)

                    btn_Exit = Button(game_WiN,text="خروج",bg="red",fg="blue",command=exit_all_apps)
                    btn_Exit.pack(pady=5)
            else:
                print("Answer Incorrect")
                EnterANSWzR.delete("0",END)
                if score > 0:
                    score -= 5
                    DDDDDDdoodleyDU -=10
                    pBar["value"] = DDDDDDdoodleyDU
                else:
                    pass
                messagebox.showinfo(title="نتیجه پاسخ",message=f"{cXrrXt_answ0r} : پاسخ شما نادرست بود. پاسخ درست")
                NuM1 = random.randint(0,9)
                NuM2 = random.randint(0,9)
                amalgarRiazi = random.randint(1,4)
                if amalgarRiazi == 1:
                    amalgarRiazi = "+"
                    cXrrXt_answ0r = NuM1 + NuM2
                elif amalgarRiazi == 2:
                    amalgarRiazi = "-"
                    cXrrXt_answ0r = NuM1 - NuM2
                elif amalgarRiazi == 3:
                    amalgarRiazi = "x"
                    cXrrXt_answ0r = NuM1 * NuM2
                elif amalgarRiazi == 4:
                    amalgarRiazi = "/"
                    cXrrXt_answ0r = NuM1 / NuM2
                SOAl = f"{NuM1} {amalgarRiazi} {NuM2}"
                REAL_quetiXn_ORGINIAL["text"] = SOAl
                lbl_score["text"] = f"score: {score}"
    except ValueError as e:
        if EnterANSWzR.get() ==  float:
            if answZR == cXrrXt_answ0r: # type: ignore
                print("Answer Correct")
                EnterANSWzR.delete("0",END)
                score += 5
                DDDDDDdoodleyDU +=10
                pBar["value"] = DDDDDDdoodleyDU
                messagebox.showinfo(title="نتیجه پاسخ",message="!پاسخ شما درست است! آفرین")
                NuM1 = random.randint(0,9)
                NuM2 = random.randint(0,9)
                amalgarRiazi = random.randint(1,4)
                if amalgarRiazi == 1:
                    amalgarRiazi = "+"
                    cXrrXt_answ0r = NuM1 + NuM2
                elif amalgarRiazi == 2:
                    amalgarRiazi = "-"
                    cXrrXt_answ0r = NuM1 - NuM2
                elif amalgarRiazi == 3:
                    amalgarRiazi = "x"
                    cXrrXt_answ0r = NuM1 * NuM2
                elif amalgarRiazi == 4:
                    amalgarRiazi = "/"
                    cXrrXt_answ0r = NuM1 / NuM2
                SOAl = f"{NuM1} {amalgarRiazi} {NuM2}"
                REAL_quetiXn_ORGINIAL["text"] = SOAl
                lbl_score["text"] = f"score: {score}"
                if score>=50:
                    game_WiN = Toplevel()
                    game_WiN.geometry("350x350")
                    game_WiN["bg"] = "green"

                    lBlwiN = Label(game_WiN,text="!!!تو بردی",bg="green",font=("",random.randint(15,20)))
                    lBlwiN.pack(pady=5)

                    btn_Exit = Button(game_WiN,text="خروج",bg="red",fg="blue",command=exit_all_apps)
                    btn_Exit.pack(pady=5)
            else:
                print("Answer Incorrect")
                EnterANSWzR.delete("0",END)
                if score > 0:
                    score -= 5
                    DDDDDDdoodleyDU -=10
                    pBar["value"] = DDDDDDdoodleyDU
                else:
                    pass
                messagebox.showinfo(title="نتیجه پاسخ",message=f"{cXrrXt_answ0r} : پاسخ شما نادرست بود. پاسخ درست")
                NuM1 = random.randint(0,9)
                NuM2 = random.randint(0,9)
                amalgarRiazi = random.randint(1,4)
                if amalgarRiazi == 1:
                    amalgarRiazi = "+"
                    cXrrXt_answ0r = NuM1 + NuM2
                elif amalgarRiazi == 2:
                    amalgarRiazi = "-"
                    cXrrXt_answ0r = NuM1 - NuM2
                elif amalgarRiazi == 3:
                    amalgarRiazi = "x"
                    cXrrXt_answ0r = NuM1 * NuM2
                elif amalgarRiazi == 4:
                    amalgarRiazi = "/"
                    cXrrXt_answ0r = NuM1 / NuM2
                SOAl = f"{NuM1} {amalgarRiazi} {NuM2}"
                REAL_quetiXn_ORGINIAL["text"] = SOAl
                lbl_score["text"] = f"score: {score}"
        else:
            messagebox.showerror(title="خطا 505",message=f"{e}\n\nلطفا بخش کد ها را بررسی نموده و سپس برنامه را اجرا کنید")
    except Exception as e:
        messagebox.showerror(title="خطا 505",message=f"{e}\n\nلطفا بخش کد ها را بررسی نموده و سپس برنامه را اجرا کنید")

def exit_all_apps():
    global game_WiN
    game.destroy()
    game_WiN.destroy()

NuM1 = random.randint(0,99)
NuM2 = random.randint(0,99)

amalgarRiazi = random.randint(1,4)

if amalgarRiazi == 1:
    amalgarRiazi = "+"
    cXrrXt_answ0r = NuM1 + NuM2
elif amalgarRiazi == 2:
    amalgarRiazi = "-"
    cXrrXt_answ0r = NuM1 - NuM2
elif amalgarRiazi == 3:
    amalgarRiazi = "x"
    cXrrXt_answ0r = NuM1 * NuM2
elif amalgarRiazi == 4:
    amalgarRiazi = "/"
    cXrrXt_answ0r = NuM1 / NuM2

SOAl = f"{NuM1} {amalgarRiazi} {NuM2}"
DDDDDDdoodleyDU = 0
score = 0
game = Tk()
game.resizable(False,False)
game.geometry("225x225")
game.title(" بازی و ریاضی ( نسخه پایتون ) ")

lbl_score = Label(game,text=f"Score : {score}",font=("",15))
lbl_score.pack(pady=5)

pBar = Progressbar(game,value=DDDDDDdoodleyDU)
pBar.pack()

questiXn = Label(game,text="Question : ")
questiXn.pack()

REAL_quetiXn_ORGINIAL = Label(game,text=SOAl)
REAL_quetiXn_ORGINIAL.pack()

answZr = Label(game,text="Your answer : ")
answZr.pack()

EnterANSWzR = Entry(game)
EnterANSWzR.pack()

BTN = Button(game,text="check",command=check)
BTN.pack()

game.mainloop()