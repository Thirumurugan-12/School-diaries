from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import os 
import pickle 
import mysql.connector  as sql
from tkinter import messagebox

from login import login



        
class loginwindow:
    def __init__(self,root):
        self.root = Tk()
        self.root.geometry("1067x600")
        self.root.configure(background="black")  
        self.root.resizable(False, False) 
        self.root.title("School Diaries")

        #background
        #self.bg = ImageTk.PhotoImage(file="files\login.jpg")
        #self.lbl_bg = Label(self.root,image=self.bg)
        #self.lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #Labels
        #self.login_lbl = Label(self.root, text="Login", bg="white", fg="#4f4e4d",font=("San Francisco", 45))
        #self.login_lbl.place(x=757,y=120)

        self.username_label = Label(self.root, text="Username ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=675, y=190)
        self.username_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
        #username_entry.insert(0, "self.root")
        self.username_entry.place(x=695, y=215, width=190)

        self.password_label = Label(self.root, text="Password ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=675, y=280)
        self.password_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
        #password_entry.insert(0, "self.root")
        self.password_entry.place(x=692, y=305, width=190)

        self.login = ImageTk.PhotoImage(file='Pics\login.png')
        self.login_button = Button(self.root, image=self.login,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",borderwidth=0, background="white", cursor="hand2")
        self.login_button.place(x=770, y=390)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        spec=sql.connect(host=host,user=username,password=password,port=port)
        if spec.is_connected():
            messagebox.showinfo("Connected","Database connected Sucessfully")
        else:
            messagebox.showerror("Exists", "Failed")
        

        mycur=spec.cursor()
        mycur.execute()

#self.self.root.mainloop()
def window():
    root =Tk()
    loginwindow(root)
    root.mainloop()

if __name__=="__main__":
    window()

