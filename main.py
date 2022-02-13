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

################
#  All screen  #
################


def calc1():
    global name
    global name2
    calcs1 = tk.Toplevel()
    calcs1.title("Geography Calculator :: half life Calculator")
    calcs1.geometry("800x300")
    calcs1.resizable(0,0)
    calcs1.configure(background=config.menu_bg)
    tell_loc1 = tk.Label(calcs1,text="สารเริ่มต้น :  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button,width=15).place(x=125,y=50)
    tell_loc2 = tk.Label(calcs1,text="จำนวนวัน:  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button,width=15).place(x=125,y=100)
    name = tk.StringVar()
    name2 = tk.StringVar()
    loc1y = tk.Entry(calcs1,font=config.fonts_menu,width=15,textvariable=name).place(x=250,y=50)
    #loc1x = tk.Entry(calcs1,font=config.fonts_menu,width=15).place(x=365,y=50)
    loc2x = tk.Entry(calcs1,font=config.fonts_menu,width=15,textvariable=name2).place(x=250,y=100)
    #loc2y = tk.Entry(calcs1,font=config.fonts_menu,width=15).place(x=365,y=100)
    confirm_btn = tk.Button(calcs1,text="คำนวณ",bg=config.confirm_btn,command=result_screen,fg="#000",font=config.fonts_menu).place(x=660,y=70)
def agestone_cal():
    agestone_cal = tk.Tk()
    agestone_cal.title("Geography Calculator :: Geography stone age")
    agestone_cal.geometry("800x300")
    agestone_cal.resizable(0,0)
    agestone_cal.configure(background=config.menu_bg)
    tell_loc3 = tk.Label(agestone_cal,text="ค่าที่ 1 :  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button).place(x=125,y=50)
    tell_loc4 = tk.Label(agestone_cal,text="ค่าที่ 2:  ",font=config.fonts_menu,fg="#fff",bg=config.menu_button).place(x=125,y=100)
    loc3y = tk.Entry(agestone_cal,font=config.fonts_menu,width=15).place(x=200,y=50)
    #loc3x = tk.Entry(agestone_cal,font=config.fonts_menu,width=15).place(x=365,y=50)
    loc4x = tk.Entry(agestone_cal,font=config.fonts_menu,width=15).place(x=200,y=100)
    #loc4y = tk.Entry(agestone_cal,font=config.fonts_menu,width=15).place(x=365,y=100)

def result_screen():
    print(int(name.get()))
    print(int(name2.get()))
    a = float(name.get())
    b = float(name2.get())
    result1 = (a*(0.5))**(b/5730)
    print(result1)
    result_screen = tk.Tk()
    result_screen.title("result :: 101")
    result_screen.geometry("800x300")
    result_screen.configure(background=config.menu_bg)
    result2 = tk.Label(result_screen,text="%.3f"%result1,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
    
    
def credit():
    global namo_pic,yuan_pic,credits,close_credits
    namo_pic = ImageTk.PhotoImage(Image.open("assets/credit/namo.png")) # Import Photos
    yuan_pic = ImageTk.PhotoImage(Image.open("assets/credit/yuan.png"))
    credits = tk.Toplevel()
    credits.title("Credits :: คณะผู้จัดทำ")
    credits.geometry("850x550")
    credits.resizable(0,0)
    credits.configure(background="#332C30") # BG this dialogs
    picprimary=tk.Label(credits,image=namo_pic).pack(side=TOP,padx=5)
    


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

    obj_img_ngixx = tk.Label(credits,image=yuan_pic)#.pack() # Normal insert image


#####################
#   Root screen     #
#####################
pg_name = tk.Label(root,text="โปรแกรมคำนวณทางภูมิศาสตร์",font=(config.fonts_menu[0],45),fg="#ffffff",bg="#2D2926").pack(side=TOP,pady=25)
btn = tk.Button(root,text="คำนวณหาค่าครึ่งชีวิต",command=calc1,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
btn2 = tk.Button(root,text="คำนวณหาค่าอายุหิน",command=agestone_cal,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
btn3 = tk.Button(root,text="ผู้จัดทำ",command=credit,font=config.fonts_menu,fg="#ffffff",bg=config.menu_button,width=50).pack(pady=3)
vers = tk.Label(root,text=f"Version 1.0.0 {config.status()} ; Made from Python",font=(config.fonts_menu[0],18),fg="#ffffff",bg="#2D2926").pack(side=BOTTOM,pady=10)


root.mainloop()
