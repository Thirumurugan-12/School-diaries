from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import os 
import pickle 
import mysql.connector  as sql
from tkinter import messagebox
import csv 

def signup():
    '''
    def store_database():

        """
        takes user input for host connection and store them into .txt file
        by pickling it into binary form
        """

        dictcred = {}

        #le = os.path.getsize("database_data.txt")

        host = host_entry.get()
        port = port_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # only if user input is not empty
        if host == "" or port == "" or username == "":
            messagebox.showinfo("Empty", "Please fill up all details")

        else:
            listcred1 = [host, port, username, password]
            di = {1: listcred1}

            if le == 0:
                f = open("database_data.txt", "wb")
                dictcred.update(di)
                pickle.dump(dictcred, f)
                messagebox.showinfo("Success!", "Your data have been saved successfully")
                f.close()

            else:
                messagebox.showerror("Exists", "Database is already connected")'''


    def createaccount():
        username = username_entry.get()
        password = password_entry.get()
        port = port_entry.get()

        spec=sql.connect(host="localhost",user="root",port="3307")
        mycur1=spec.cursor()

        try :
            '''
            username = username_entry.get()
            password = password_entry.get()
            port = port_entry.get()

            spec=sql.connect(host="localhost",user=username,port=port)
            mycur=spec.cursor()
            '''
            mycur1.execute("Flush privileges")
            mycur1.execute(f"create user '{username}'@'localhost' identified by '{password}'")
            spec.commit()
            messagebox.showinfo("Success","Account Created successfully ")
            messagebox.showwarning("Note it",f"Your Account Details Username : {username} Password: {password} ")
            #mycur1.execute("Flush privileges")
            
            

        except:
            messagebox.showerror("Error","fill the details carefully")
        
        
        spec2 = sql.connect(host="localhost",user=username_entry.get(),password=password_entry.get(),port=int(port_entry.get()))
        mycur=spec2.cursor(buffered=True)


        #database creation 
        try:
            #spec2 = sql.connect(host="localhost",user=username,password=password,port=port)
            #mycur=spec2.cursor()
            #mycur.execute("Flush privileges")
            mycur.execute('create database sms;')
            messagebox.showinfo("Success", "Database \n cms\n created Successfully")
        except:
            mycur.execute('use sms;')
            messagebox.showerror("Error", "Database Creation Failed, \nDatabase May already exists!")

        try:
            mycur.execute('use sms;')
            mycur.execute('create table batch(batch_id int NOT NULL AUTO_INCREMENT, batch_name varchar(50) NOT NULL,batch_year varchar(10) NOT NULL, batch_intake varchar(20) NOT NULL,PRIMARY KEY (batch_id), UNIQUE KEY (batch_name), reg_date date);')
            

            mycur.execute('create table course(course_id int NOT NULL AUTO_INCREMENT, course_name varchar(50) NOT NULL,course_duration varchar(10) NOT NULL, course_credit varchar(20) NOT NULL, reg_date date,PRIMARY KEY (course_id), UNIQUE KEY (course_name));')
            

            mycur.execute('create table section(section_id int NOT NULL AUTO_INCREMENT, section_code varchar(50) NOT NULL,section_name varchar(50) NOT NULL, section_capacity int NOT NULL,PRIMARY KEY (section_id), UNIQUE KEY (section_name), reg_date date);')
            

            mycur.execute ('create table department(department_id int NOT NULL AUTO_INCREMENT, department_code varchar(50) NOT NULL,department_name varchar(50) NOT NULL,PRIMARY KEY (department_id), UNIQUE KEY (department_name), reg_date date);')
            

            mycur.execute('create table students(student_id int NOT NULL AUTO_INCREMENT,'
                    'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                    'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                    'l_name varchar(50), dob varchar(20),gender varchar(10),'
                    'address varchar(30), contact_no int(13) NOT NULL,shift varchar(20) NOT NULL,'
                    'course_enrolled varchar(50) NOT NULL,batch varchar(50) NOT NULL,'
                    'section_enrolled varchar(20) NOT NULL, reg_date date, PRIMARY KEY (student_id),'
                    'FOREIGN KEY (course_enrolled) REFERENCES course (course_name),'
                    'FOREIGN KEY (batch) REFERENCES batch (batch_name),'
                    'CONSTRAINT UC_username UNIQUE (username,email));')
            

            mycur.execute('create table employees(employee_id int NOT NULL AUTO_INCREMENT,'
                    'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                    'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                    'l_name varchar(50), dob varchar(20),gender varchar(10),'
                    'address varchar(30), contact_no int(13) NOT NULL,job_type varchar(20) NOT NULL,'
                    'registered_as varchar(50) NOT NULL,qualification varchar(50) NOT NULL,'
                    'department varchar(20) NOT NULL, reg_date date, PRIMARY KEY (employee_id),'
                    'FOREIGN KEY (department) REFERENCES department (department_name),'
                    'CONSTRAINT UC_username UNIQUE (username,email));')
            
            spec2.commit()
            messagebox.showinfo("Success", "All Table are created successfully")
            
    

        except BaseException as msg:
            #f=open("log.txt","w")
            #f.write(msg)
            #f.close()
            messagebox.showerror("Error", f"Database Table Creation Failed {msg}")
        #except BaseException:
            #messagebox.showerror("Error","fill the details carefully")

    root = Tk()
    root.geometry("1067x600")
    root.configure(background="black")
    root.resizable(False, False) 
    root.title("School Diaries")

    #background
    bg = ImageTk.PhotoImage(file="files\\Sublime Light 12_new.jpg")
    lbl_bg = Label(root,image=bg)
    lbl_bg.image = bg
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    #user_ic=ImageTk.PhotoImage(file=r"Pics\user.png")
    #u_lbl=Label(root,image=user_ic,bg="white")
    #u_lbl.image = user_ic
    #u_lbl.place(x=805,y=53)

    #Labels
    register = Label(root, text="Sign Up", bg="white", fg="#4f4e4d",font=("San Francisco", 45))
    register.place(x=750,y=75)
    
    
    port_label = Label(root, text="Port ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 12, "bold"))
    port_label.place(x=675, y=172)
    port_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
    #host_entry.insert(0, "localhost")
    port_entry.place(x=692, y=198, width=145)
    
    username_label = Label(root, text="Username ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
    username_label.place(x=675, y=260)
    username_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
    #username_entry.insert(0, "root")
    username_entry.place(x=692, y=287, width=190)

    password_label = Label(root, text="Password ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
    password_label.place(x=675, y=350)
    password_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 12))
    #password_entry.insert(0, "root")
    password_entry.place(x=692, y=375, width=190)

    f_name_label = Label(root, text="First Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    f_name_label.place(x=10, y=10)

    f_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    f_name_entry.place(x=235, y=277, width=260)  # trebuchet ms

    f_name_line = Canvas(root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
    f_name_line.place(x=235, y=299)

    submit = ImageTk.PhotoImage(file='Pics\submit.png')
    submit_button = Button(root, image=submit,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",borderwidth=0, background="white", cursor="hand2",command=createaccount)
    submit_button.image = submit
    submit_button.place(x=655, y=440)

    login = ImageTk.PhotoImage(file='Pics\login.png')
    login_button = Button(root, image=login,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white",borderwidth=0, background="white", cursor="hand2")
    login_button.image = login 
    login_button.place(x=785, y=442)

    root.mainloop()

if __name__=='__main__':
    signup()