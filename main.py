from email.mime import image    
import tkinter as tk
from tkinter import Canvas, Frame, messagebox
from tkinter import font
from tkinter.constants import *
import math
import time
from turtle import width
import config
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Geography Calculator")
root.geometry("800x500")
root.configure(background=config.menu_bg)
root.resizable(0,0)
icon_app = tk.PhotoImage(file = "assets/iconmain.png")
root.iconphoto(True,icon_app)

#  All screen  


def calc1():
    global name,name2,loc1y,loc2x
    root.destroy()
    calcs1 = tk.Tk()
    calcs1.title("Geography Calculator :: half life Calculator")
    calcs1.geometry("800x300")
    calcs1.resizable(0,0)
    calcs1.configure(background=config.menu_bg)
    tell_loc1 = tk.Label(calcs1,text="สารตั้งต้น(กรัม) :  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button,width=15).place(x=125,y=50)
    tell_loc2 = tk.Label(calcs1,text="จำนวนวัน:  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button,width=15).place(x=125,y=100)
    name = tk.StringVar()
    name2 = tk.StringVar()
    loc1y = tk.Entry(calcs1,font=config.fonts_menu,width=15,textvariable=name)
    loc2x = tk.Entry(calcs1,font=config.fonts_menu,width=15,textvariable=name2)
    loc1y.place(x=280,y=50)
    loc2x.place(x=280,y=100)
    confirm_btn = tk.Button(calcs1,text="คำนวณ",bg=config.confirm_btn,command=result_screen,fg="#000",font=config.fonts_menu).place(x=660,y=70)
def hvs():
    root.destroy()
    hvs = tk.Tk()
    hvs.title("Geography Calculator :: Geography stone age")
    hvs.geometry("800x300")
    hvs.resizable(0,0)
    hvs.configure(background=config.menu_bg)
    x1 = tk.StringVar()
    y1 = tk.StringVar()
    x2 = tk.StringVar()
    y2 = tk.StringVar()
    tell_loc3 = tk.Label(hvs,text="จุด 1 :  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button).place(x=125,y=50)
    tell_loc4 = tk.Label(hvs,text="จุด 2:  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button).place(x=125,y=100)
    loc3y = tk.Entry(hvs,font=config.fonts_menu,width=15,textvariable=x1).place(x=200,y=50)
    loc3x = tk.Entry(hvs,font=config.fonts_menu,width=15,textvariable=x2).place(x=365,y=50)
    loc4x = tk.Entry(hvs,font=config.fonts_menu,width=15,textvariable=y1).place(x=200,y=100)
    loc4y = tk.Entry(hvs,font=config.fonts_menu,width=15,textvariable=y2).place(x=365,y=100)
    confirm_btn = tk.Button(hvs,text="คำนวณ",bg=config.confirm_btn,command=lambda: haversine(int(x1.get()),int(y1.get()),int(x2.get()),int(y2.get())),fg="#000",font=config.fonts_menu).place(x=660,y=70)


def result_screen():
    if (name.get() == "") and (name2.get() == ""):
        messagebox.showerror("Error!","ไม่สามารถเว้นค่า")
    else:
        try:
            a = float(name.get())
            b = float(name2.get())
            result1 = (a*(0.5))**(b/5730)
            result4="%.3f"%result1
            result3 = messagebox.showinfo("halflifestone",result4+"gram")

        except ValueError:
            messagebox.showerror("Error!","กรอกค่าตัวเลขเท่านั้น!")

def info():
    global infomation,infos
    infos = tk.Toplevel()
    infos.title("stone classification")
    #infos.geometry("860x1030")
    infos.configure(background="#332C30")
    infomation = ImageTk.PhotoImage(Image.open("credit/info1.png"))
    picinfo=tk.Label(infos,image=infomation).pack()

####หน้า hvs####

def haversine(lat1, lon1, lat2, lon2):
    global rad,c
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    #return rad * c
    messagebox.showinfo("",f"{rad*c} kilometer")


####หน้า credit####
def credit():
    global namo_pic,yuan_pic,credits,close_credits
    namo_pic = ImageTk.PhotoImage(Image.open("credit/namo1.png")) # Import Photos
    yuan_pic = ImageTk.PhotoImage(Image.open("credit/yuan.png"))
    credits = tk.Toplevel()
    credits.title("Credits :: คณะผู้จัดทำ")
    credits.geometry("850x550")
    credits.resizable(0,0)
    credits.configure(background="#332C30") # BG this dialogs
    picprimary=tk.Label(credits,image=namo_pic).place(relx=0.1 , rely= 0.2 )
    picprimary=tk.Label(credits,image=yuan_pic).place(relx=0.7 , rely= 0.2 )

    

    


    title1 = tk.Label(credits,
        text="จัดทำโดย",
        font=config.fonts_menu,
        bg="red",
        fg="white"
    ).pack(side=TOP,pady=30)

    name_cre_st = tk.Label(
        credits,
        text=f"{config.credit_st[1]} เลขที่ {config.credit_st[0]}",
        font=config.fonts_menu,
        bg = "black",
        fg = "white"
    ).pack(side=TOP,pady=1)
    
    name_cre_nd = tk.Label(
        credits,
        text=f"{config.credit_nd[1]} เลขที่ {config.credit_nd[0]}",
        font=config.fonts_menu,       
        bg = "black",
        fg = "white"
    ).pack(side=TOP,pady=1)

    class_tell = tk.Label(
        credits,
        text=config.class_credit,
        font=config.fonts_menu,        
        bg = "red",
        fg = "white"
    ).pack(side=TOP,pady=10)

    title2 = tk.Label(
        credits,
        text="นำเสนอ",
        font=config.fonts_menu,
        bg="red",
        fg="white"
    ).place(anchor=CENTER,x=400,y=350)

    teach = tk.Label(
        credits,
        text=f"{config.teach_pre[0]}\n{config.teach_pre[1]}\n{config.teach_pre[2]}",
        font=config.fonts_menu,
        bg="black",
        fg="white"
    ).place(anchor=CENTER,x=400,y=365)

    obj_img_yuan = tk.Label(credits,image=yuan_pic)#.pack() # Normal insert image



#   Root screen     #

pg_name = tk.Label(root,text="โปรแกรมคำนวณทางภูมิศาสตร์",font=(config.fonts_menu[0],45),fg="#ffffff",bg="#C68866").pack(side=TOP,pady=25)
btn = tk.Button(root,text="คำนวณหาค่าครึ่งชีวิต",command=calc1,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
btn2 = tk.Button(root,text="คำนวณหาค่าระยะทางจุด2จุด",command=hvs,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
btn4 = tk.Button(root,text="เนื้อหา",command=info,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=4)
btn3 = tk.Button(root,text="ผู้จัดทำ",command=credit,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=5)
vers = tk.Label(root,text=f"Version 1.0 {config.status()} ; Made by namo",font=(config.fonts_menu[0],18),fg="#ffffff",bg="#2D2926").pack(side=BOTTOM,pady=10)


root.mainloop()
