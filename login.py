from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import os 
import pickle 
import mysql.connector  as sql
from tkinter import messagebox
import user_inter
import dashboard

def loginscreen():
    def login_l():

        try:
            host = user_inter.login1.host_entry.get()
            port = user_inter.login1.port_entry.get()
            username = username_entry.get()
            password = password_entry.get()


            spec=sql.connect(host=host,user=username,password=password,port=port)
            if spec.is_connected():
                messagebox.showinfo("Connected","Database connected Sucessfully")
                dashboard.dashboard()
            #else:
               # messagebox.showerror("Exists", "Failed")
            

            mycur=spec.cursor()
            mycur.execute()
        except BaseException:
            messagebox.showerror("User","User doesnt exist")

            

    root = Toplevel()
    root.geometry("1067x600")
    root.configure(background="black")  
    root.resizable(False, False) 
    root.title("School Diaries")

    #background
    bg = ImageTk.PhotoImage(file="files\login.jpg")
    lbl_bg_l = Label(root,image=bg)
    lbl_bg_l.image = bg
    lbl_bg_l.place(x=0,y=0,relwidth=1,relheight=1)


    #Labels
    login_lbl = Label(root, text="Login", bg="white", fg="#4f4e4d",font=("San Francisco", 45))
    login_lbl.place(x=757,y=120)

    username_label = Label(root, text="Username ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
    username_label.place(x=675, y=190)
    username_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
    #username_entry.insert(0, "root")
    username_entry.place(x=695, y=215, width=190)

    password_label = Label(root, text="Password ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
    password_label.place(x=675, y=280)
    password_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
    #password_entry.insert(0, "root")
    password_entry.place(x=692, y=305, width=190)

    login_pi = ImageTk.PhotoImage(file='Pics\login.jpg')
    login_button_lg = Button(root, image=login_pi,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",borderwidth=0, background="white", cursor="hand2",command=login_l)
    login_button_lg.image = login_pi
    login_button_lg.place(x=770, y=390)

    #root.mainloop()


if __name__=="__main__":
    loginscreen()


