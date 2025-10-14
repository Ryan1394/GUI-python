from tkinter import * # type: ignore
from tkinter.ttk import Combobox
from datetime import datetime
from tkinter import messagebox
from os import system
system("clear")

def saveTask():
    todayDate = datetime.now()
    month = todayDate.month
    day = todayDate.day
    year = todayDate.year
    hr = todayDate.hour
    min = todayDate.minute
    sec = todayDate.second
    if sec < 9:
        sec = f"0{sec}"
    F = open(f"s6/{day}-{month}-{year}","w")
    DAY =combo_day.get()
    TITLE = entryTitle.get()
    DESC = ent_txt.get("1.0",END)
    HOUR = ent_start.get()
    MIN = ent_end.get()
    if TITLE == "":
        messagebox.showerror("title","Title can not be empty")
    elif day =="":
        messagebox.showerror("day error","day can not be empty")
    else:
        F.write(f"Day : {DAY}\n")
        F.write(f"Title : {TITLE}\n")
        F.write(f"Description : {DESC}\n")
        F.write(f"Time : {HOUR}:{MIN}\n")
        F.write(f"\nSaved at: {hr}:{min}:{sec}")
        messagebox.showinfo("sucsess","task saved sucsessfully")




todoListPage = Tk()
todoListPage.geometry("500x600")
todoListPage.title("Todo List")
todoListPage["bg"] = "cyan"

lbl_day = Label(todoListPage,text="what day *")
combo_day = Combobox(todoListPage,values=("Saturday","Sunday","Monday","Tuesday","Wednesday","Tursday","Friday"))
lbl_title = Label(todoListPage,text="Subject")
entryTitle = Entry(todoListPage)
lbl_desc = Label(todoListPage, text="Description")
ent_txt = Text(todoListPage,width=35,height=8)
lbl_time = Label(todoListPage,text="Start")
ent_start = Spinbox(todoListPage,from_=1,to=24)
ent_end = Spinbox(todoListPage,from_=0,to=60)

btn_save = Button(todoListPage,text="Save Your Task",command=saveTask)

lbl_day.place(x=25,y=50)
combo_day.place(x=120,y=50)
lbl_title.place(x=25,y=75)
entryTitle.place(x=120,y=75)
lbl_desc.place(x=25,y=100)
ent_txt.place(x=120,y=100)
lbl_time.place(x=25,y=245)
ent_start.place(x=75,y=245)
ent_end.place(x=250,y=245)

btn_save.place(x=200,y=315)

todoListPage.mainloop()