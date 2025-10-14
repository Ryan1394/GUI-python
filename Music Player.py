from tkinter import * # type: ignore
from tkinter import filedialog # type: ignore
from os import * # type: ignore
import pygame
system("cls")

def destroy__():
    MaowZik_DDD.destroy()

def LoAD():
    try:
        global PLaYER
        res = filedialog.askopenfilename()
        PLaYER = pygame.mixer
        PLaYER.init()
        PLaYER.music.load(res)
        PLaYER.music.set_volume(0.7)
    except:
        pass

def PLaY():
    try:
        PLaYER.music.play()
    except:
        pass


def PaUSE():
    try:
        PLaYER.music.pause()
    except:
        pass

def ReSUMe():
    try:
        PLaYER.music.unpause()
    except:
        pass

def SToP():
    try:
        PLaYER.music.stop()
    except:
        pass

MaowZik_DDD = Tk()
MaowZik_DDD.resizable(False,False)
MaowZik_DDD.config(bg="Pink")
MaowZik_DDD.geometry("750x200")
MaowZik_DDD.title(" 🎶 🎵 🎛 🎧 🎼  MUSiC PLAYER  🎼 🎧 🎛 🎵 🎶 ")

PLaY_btn    =   Button(MaowZik_DDD,text="Play Music",     width=10,height=3,font=("alias",10),bg="orange",command=PLaY).grid(row=0,column=0,   padx=5,        pady=20)
PaUSE_btn    =  Button(MaowZik_DDD,text="Pause Music",    width=10,height=3,font=("alias",10),bg="orange",command=PaUSE).grid(row=0,column=1,   padx=5,       pady=20)
ReSUMe_btn    = Button(MaowZik_DDD,text="Resume Music",   width=10,height=3,font=("alias",10),bg="orange",command=ReSUMe).grid(row=0,column=2,   padx=5,      pady=20)
SToP_btn    =   Button(MaowZik_DDD,text="Stop Music",     width=10,height=3,font=("alias",10),bg="orange",command=SToP).grid(row=0,column=3,   padx=5,        pady=20)
EXiT_btn    =   Button(MaowZik_DDD,text="Exit",           width=10,height=3,font=("alias",10),   bg="red",command=destroy__).grid(row=0,column=5,   padx=5,   pady=20)
LoAD_btn    =   Button(MaowZik_DDD,text="Load Music",     width=10,height=1,font=("alias",10),bg="orange",pady=20,command=LoAD).grid(row=0,column=4 ,padx=5,  pady=20)

MaowZik_DDD.mainloop()