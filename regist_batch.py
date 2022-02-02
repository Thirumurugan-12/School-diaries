from distutils import command
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import os 
import pickle 
import mysql.connector  as sql
from tkinter import messagebox
from datetime import date
from datetime import time
from datetime import *
import requests
from bs4 import BeautifulSoup
import time
import user_inter
import csv 
import course_screen


def regist_batch():
    def click_clear_button():
        batch_name_entry.delete(0, END)
        batch_year_entry.delete(0, END)
        batch_intake_combo.current(0)

    def back():
        root.destroy()

    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])

    def validation():
        """this will validate if the batch code and name of entry fields are already in database table named
        batch or not if return True, error message is thrown displaying batch code/name already exists"""
        try:
            #obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            #db_connection.create(obj_batch_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            query = "select * from batch;"
            mycur.execute(query)
            data = mycur.fetchall()

            # print(data)
            name_list = []
            for values in data:
                name_data_list = values[1]
                name_list.append(name_data_list)
                # print(name_data_list)

        except BaseException as msg:
            print(msg)

        if batch_name_entry.get() == "" or batch_year_entry.get() == "":
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif batch_name_entry.get() in name_list:
            messagebox.showerror("Already Exists", f"{batch_name_entry.get()} Batch Already Exists")

        else:
            click_submit()

    def click_submit():
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            #obj_batch_database = Model_class.batch_registration.GetDatabase('use cms;')
            #db_connection.create(obj_batch_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            #obj_batch_database = Model_class.batch_registration.BatchRegistration(batch_name_entry.get(),
                                                                                    #batch_year_entry.get(),
                                                                                    #batch_intake_combo.get(),
                                                                                    #reg_date)

            query = f"insert into batch (batch_name,batch_year,batch_intake,reg_date) values ('{batch_name_entry.get()}','{batch_year_entry.get()}','{batch_intake_combo.get()}','{reg_date}');"
            mycur.execute(query)
            spec.commit()
            #values = (obj_batch_database.get_name(),obj_batch_database.get_year(),
                        #obj_batch_database.get_intake(),obj_batch_database.get_reg_date())
            # print(values)
            #db_connection.insert(query, values)
            # print(values)

            messagebox.showinfo("Success", f"Batch Registered Successfully\n Batch Name={batch_name_entry.get()},\n "
                                            f"Batch Year={batch_year_entry.get()}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def exit():
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            root.destroy()

    root = Toplevel()
    root.title('BATCH REGISTRATION FORM - COLLEGE MANAGEMENT SYSTEM')
    root.geometry('1067x600')
    root.config(bg="#f29844")
    root.resizable(False, False)


    # ======================Backend connection=============
    #db_connection = Backend.connection.DatabaseConnection()

    # creating frame for Register
    # img = img
    # dummylabel = Label(root, image=img)
    # dummylabel.place(x=30, y=30)

    reg_frame = Frame(root, bg="#ffffff", width=1000, height=560)
    reg_frame.place(x=30, y=30)



    heading = Label(reg_frame, text="Batch Registration Form", font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=200, y=0, width=600)



    batch_frame = LabelFrame(reg_frame, text="Batch Details", bg="white", fg="#4f4e4d", height=380,
                                    width=800, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
    batch_frame.config(highlightbackground="red")
    batch_frame.place(x=100, y=90)

    # ========================================================================
    # ===========================batch Name==================================
    # ========================================================================

    batch_name_label = Label(batch_frame, text="Batch Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    batch_name_label.place(x=160, y=65)

    batch_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
    batch_name_entry.place(x=400, y=212, width=345)  # trebuchet ms

    batch_name_line = Canvas(root, width=345, height=1.5, bg="#bdb9b1", highlightthickness=0)
    batch_name_line.place(x=400, y=234)

    # ========================================================================
    # ===========================batch YEAR ==================================
    # ========================================================================
    date = time.strftime("%Y")

    batch_year_label = Label(batch_frame, text="Batch Year ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    batch_year_label.place(x=160, y=115)

    batch_year_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
    batch_year_entry.place(x=390, y=262, width=355)  # trebuchet ms

    batch_year_line = Canvas(root, width=355, height=1.5, bg="#bdb9b1", highlightthickness=0)
    batch_year_line.place(x=390, y=284)
    batch_year_entry.insert(0, date)

    # ========================================================================
    # ===========================batch Intake==================================
    # ========================================================================
    root.option_add("*TCombobox*Listbox*Foreground", '#f29844')

    batch_intake_label = Label(batch_frame, text="Batch Intake ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    batch_intake_label.place(x=160, y=165)

    batch_intake_combo = ttk.Combobox(batch_frame, font=('yu gothic ui semibold', 12, 'bold'),
                                            state='readonly',
                                            width=35)
    batch_intake_combo['values'] = ("January", "February", "March", "April", "May", "June", "July", "August",
                                            "September", "October", "November", "December")
    batch_intake_combo.current(0)
    batch_intake_combo.place(x=270, y=167)
    # batch_intake_line.place(x=410, y=424)

    reg_date = time.strftime("%Y/%m/%d")


    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================
    submit_img = ImageTk.PhotoImage(file='Pics\\submit.png')
    submit = Button(batch_frame, image=submit_img,
                            font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                            , borderwidth=0, background="white", cursor="hand2",command=validation)
    submit.image = submit_img
    submit.place(x=90, y=267)

    clear_img = ImageTk.PhotoImage(file='Pics\\clear.png')
    clear_button = Button(batch_frame, image=clear_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2",
                                command=click_clear_button)
    clear_button.image = clear_img
    clear_button.place(x=250, y=270)

    back_img = ImageTk.PhotoImage(file='Pics\\back.png')
    back_button = Button(batch_frame, image=back_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2",command=back)
    back_button.image = back_img
    back_button.place(x=410, y=270)

    exit_img = ImageTk.PhotoImage(file='Pics\\exit.png')
    exit_button = Button(batch_frame, image=exit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2", command=exit)
    exit_button.image = exit_img
    exit_button.place(x=570, y=270)


    #root.mainloop()


if __name__ =="__main__":
    regist_batch()