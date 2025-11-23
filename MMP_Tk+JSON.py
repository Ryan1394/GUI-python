from tkinter import * # type: ignore
import requests
import json
import os
os.system("cls")

def save(DATA):
    if DATA == "ALL":
        with open("s5/ArzAllData.json","w") as ARZfile:
            EtelaateArz = Data
            json.dump(EtelaateArz,ARZfile,indent=4)
            ARZfile.close()
    if DATA == "FourData":
        with open("s5/Arz4Data.json","w") as ARZfile:
            EtelaateArz = {
                "status":200,
                "result":{
                    "usd":DLR_PRiCE,
                    "eur":EUR_PRiCE,
                    "gbp":PND_PRiCE,
                    "cad":CAD_PRiCE
                }
            }
            json.dump(EtelaateArz,ARZfile,indent=4)
            ARZfile.close()

token = "993228:688a82b1bd11a"

URL = "https://api.one-api.ir/currency/v1/navasan/currency"

Header = {
    "one-api-token":token
}

cur = {
    "Dollar":"usd",
    "Euro":"eur",
    "Dollar Canada":"cad",
    "Pond":"gbp"
}

response = requests.get(url=URL,headers=Header)

Data = response.json()

DLR_PRiCE = Data["result"]["usd"]["value"]
EUR_PRiCE = Data["result"]["eur"]["value"]
PND_PRiCE = Data["result"]["gbp"]["value"]
CAD_PRiCE = Data["result"]["cad"]["value"]

####################################################

root = Tk()
root.geometry("450x450")
root.title("قیمت ارز ها به تومان")
root["bg"] = "#54abc2"

lBl_ShowWhatIsThisAppAbout = Label(root,text="قیمت ارز ها به تومان",bg="#54abc2",fg="Black",font=("",25))
lBl_ShowWhatIsThisAppAbout.pack(pady=13)

lBl_Dollar = Label(root,text=f"قیمت دلار : {DLR_PRiCE} تومان",bg="#54abc2",fg="Black",font=("",20))
lBl_Dollar.pack(pady=5)

lBl_Euro = Label(root,text=f"قیمت یورو : {EUR_PRiCE} تومان",bg="#54abc2",fg="Black",font=("",20))
lBl_Euro.pack(pady=5)

lBl_Pond = Label(root,text=f"قیمت پوند : {PND_PRiCE} تومان",bg="#54abc2",fg="Black",font=("",20))
lBl_Pond.pack(pady=5)

lBl_DollarCND = Label(root,text=f"قیمت دلار کانادا : {CAD_PRiCE} تومان",bg="#54abc2",fg="Black",font=("",20))
lBl_DollarCND.pack(pady=5)

BtnSave__ALL__Data = Button(root,text="ذخیره اطلاعات همه ارز ها",bg="Green",fg="Black",font=("",19),command= lambda : save("ALL"))
BtnSave__ALL__Data.pack(pady=5)

BtnSave__ALL__Data = Button(root,text="ذخیره اطلاعات دلار ، یورو ، پوند و دلار کانادا",bg="Green",fg="Black",font=("",19),command= lambda : save("FourData"))
BtnSave__ALL__Data.pack(pady=5)

root.mainloop()