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



def regist_emp():
    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])


    def reg_as():
        """ to validate and register employee as different roles"""
        global department_combo 
        try:
            #obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
            #db_connection.create(obj_employee_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            query = "select * from department"
            mycur.execute(query)

            department_tuple = mycur.fetchall()
            # print(department_tuple)
            department_list = []
            for i in department_tuple:
                department_name = i[2]
                department_list.append(department_name)
                # print(department_name)
                # print(department_list)

        except BaseException as msg:
            print(msg)
        # ========================================================================
        # ============================Department=============================
        # ========================================================================
        department_label = Label(personal_frame, text="Department ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        department_label.place(x=370, y=170)  # (x=370, y=130) (x=370, y=170)

        department_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                                width=31)

        department_combo['values'] = department_list
        try:
            department_combo.current(0)
        except:
            messagebox.showerror("Error", "You must add Department first")
        department_combo.place(x=605, y=437)


    def validation():
            """this will validate if the username and email of entry fields are already in database table named employee or
            not if return True, error message is thrown displaying email/username already exists"""
            try:
                #obj_student_database = Model_class.employee_registration.GetDatabase('use cms;')
                #db_connection.create(obj_student_database.get_database())
                a=load_data()
                host=a[0]
                username = a[2]
                password = a[3]
                port=a[1]
                
                spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
                mycur=spec.cursor()

                query = "select * from employees;"
                mycur.execute(query)
                data = mycur.fetchall()
                # print(data)
                username_list = []
                email_list = []
                for values in data:
                    # print(values)
                    user_data_list = values[1]
                    username_list.append(user_data_list)
                    email_data_list = values[2]
                    email_list.append(email_data_list)
                    # print(final_list)
                    # print(data_list)
            except BaseException as msg:
                print(msg)

            if username_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "" \
                    or f_name_entry.get() == "" or l_name_entry.get() == "" or dob_entry.get() == "" \
                    or address_entry.get() == "" or contact_entry.get() == "":
                messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

            elif username_entry.get() in username_list:
                messagebox.showerror("Already Exists", f"{username_entry.get()} username Already Exists")

            elif "@" not in email_entry.get():
                messagebox.showerror("Invalid Email", f"{email_entry.get()} Email ID Invalid")

            elif email_entry.get() in email_list:
                messagebox.showerror("Already Exists", f"{email_entry.get()} Email ID Already Exists")

            elif password_entry.get() != c_password_entry.get():
                messagebox.showerror("Not Matched", "Password Does not Matched")

            else:
                click_submit()
    def back():
        root.destroy()

    def click_submit():
        """initialize when click submit button, which will take data from entry box
        and insert those data into employee table after successful validation of those data"""
        try:
            #obj_employee_database = Model_class.employee_registration.GetDatabase('use cms;')
            #db_connection.create(obj_employee_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            #obj_employee_database = Model_class.employee_registration.EmployeeRegistration(username_entry.get(),
                                                                                            #email_entry.get(),
                                                                                            #password_entry.get(),
                                                                                            #f_name_entry.get(),
                                                                                            #l_name_entry.get(),
                                                                                            #dob_entry.get(),
                                                                                            #gender_combo.get(),
                                                                                            #address_entry.get(),
                                                                                            #contact_entry.get(),
                                                                                            #job_type_combo.get(),
                                                                                            #register_as_combo.get(),
                                                                                            #qualification_entry.get(),
                                                                                            #department_combo.get(),
                                                                                            #reg_date)
            query = f"insert into employees (username,email,password,f_name,l_name,dob,gender,address," \
                    f"contact_no,job_type,registered_as,qualification,department,reg_date) values ('{username_entry.get()}','{email_entry.get()}','{password_entry.get()}','{f_name_entry.get()}','{l_name_entry.get()}','{dob_entry.get()}'," \
                    f"'{gender_combo.get()}','{address_entry.get()}','{contact_entry.get()}','{job_type_combo.get()}','{register_as_combo.get()}','{qualification_entry.get()}','{department_combo.get()}','{reg_date}');"

                
            #values = (obj_employee_database.get_username(), obj_employee_database.get_email(),
                        #obj_employee_database.get_password(), obj_employee_database.get_f_name(),
                        #obj_employee_database.get_l_name(), obj_employee_database.get_dob(),
                        #obj_employee_database.get_gender(), obj_employee_database.get_address(),
                        #obj_employee_database.get_contact(), obj_employee_database.get_job(),
                        #obj_employee_database.get_reg_as(), obj_employee_database.get_qualification(),
                        #obj_employee_database.get_department(), obj_employee_database.get_reg_date())
            # print(values)
            #db_connection.insert(query, values)
            # print(values)
            mycur.execute(query)
            spec.commit()
            messagebox.showinfo("Success", f"Data inserted Successfully\n Employee name={f_name_entry.get()},\n "
                                            f"JOB={job_type_combo.get()}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def exit():
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n College Management System?")
        if ask is True:
            root.destroy()


    root = Toplevel()
    root.title('EMPLOYEE MANAGEMENT SYSTEM - COLLEGE MANAGEMENT SYSTEM')
    root.geometry('1067x600')
    root.config(bg="#f29844")

    # ======================Backend connection=============
    #db_connection = Backend.connection.DatabaseConnection()

    reg_frame = Frame(root, bg="#ffffff", width=1000, height=560)
    reg_frame.place(x=30, y=30)


    heading = Label(reg_frame, text="Employee Registration Form", font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=200, y=0, width=600)
    #slider()
    #heading_color()

    cred_frame = LabelFrame(reg_frame, text="Account Details", bg="white", fg="#4f4e4d", height=140,
                                    width=800, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
    cred_frame.config(highlightbackground="red")
    cred_frame.place(x=100, y=50)

    # ========================================================================
    # ============================Username====================================
    # ========================================================================

    username_label = Label(cred_frame, text="Username ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    username_label.place(x=10, y=10)

    username_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    username_entry.place(x=230, y=117, width=260)  # trebuchet ms

    username_line = Canvas(root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=230, y=139)

    # ========================================================================
    # ============================Email=======================================
    # ========================================================================

    email_label = Label(cred_frame, text="Email ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    email_label.place(x=370, y=10)

    email_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    email_entry.place(x=555, y=117, width=350)  # trebuchet ms

    email_line = Canvas(root, width=350, height=1.5, bg="#bdb9b1", highlightthickness=0)
    email_line.place(x=555, y=139)

    # ========================================================================
    # ============================Password====================================
    # ========================================================================

    password_label = Label(cred_frame, text="Password ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    password_label.place(x=10, y=50)

    password_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12),show = "*")
    password_entry.place(x=230, y=157, width=260)  # trebuchet ms

    password_line = Canvas(root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=230, y=180)

    # ========================================================================
    # ============================Confirm password============================
    # ========================================================================

    c_password_label = Label(cred_frame, text="Confirm Password ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    c_password_label.place(x=370, y=50)

    c_password_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show = "*")
    c_password_entry.place(x=650, y=157, width=255)  # trebuchet ms

    c_password_line = Canvas(root, width=255, height=1.5, bg="#bdb9b1", highlightthickness=0)
    c_password_line.place(x=650, y=180)

    # =======================================================================
    # ========================frame for personal credentails=================
    # =======================================================================

    personal_frame = LabelFrame(reg_frame, text="Personal Details", bg="white", fg="#4f4e4d", height=265,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
    personal_frame.config(highlightbackground="red")
    personal_frame.place(x=100, y=210)


    # ========================================================================
    # ============================First name==================================
    # ========================================================================
    f_name_label = Label(personal_frame, text="First Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    f_name_label.place(x=10, y=10)

    f_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    f_name_entry.place(x=235, y=277, width=260)  # trebuchet ms

    f_name_line = Canvas(root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
    f_name_line.place(x=235, y=299)

    # ========================================================================
    # ============================Last name===================================
    # ========================================================================

    l_name_label = Label(personal_frame, text="Last Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    l_name_label.place(x=370, y=10)

    l_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    l_name_entry.place(x=595, y=277, width=315)  # trebuchet ms

    l_name_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
    l_name_line.place(x=595, y=299)

    # ========================================================================
    # ============================DOB=========================================
    # ========================================================================

    dob_label = Label(personal_frame, text="DOB ", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
    dob_label.place(x=10, y=50)

    dob_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                            font=("yu gothic ui semibold", 12))
    dob_entry.insert(0, "mm/dd/yyyy")
    dob_entry.place(x=190, y=317, width=305)  # trebuchet ms
    #dob_entry.bind("<1>", pick_date)

    dob_line = Canvas(root, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
    dob_line.place(x=190, y=339)

    # ========================================================================
    # ===========================Gender=======================================
    # ========================================================================
    style = ttk.Style()

    # style.map('TCombobox', selectbackground=[('readonly', 'grey')])
    root.option_add("*TCombobox*Listbox*Foreground", '#f29844')

    gender_label = Label(personal_frame, text="Gender ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    gender_label.place(x=370, y=50)

    gender_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=35)
    gender_combo['values'] = ('Male', 'Female', 'Rather not say')
    gender_combo.current(0)
    gender_combo.place(x=570, y=317)

    # gender_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
    # gender_line.place(x=595, y=369)
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # ========================================================================
    # ============================Address====================================
    # ========================================================================

    address_label = Label(personal_frame, text="Address ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    address_label.place(x=10, y=90)

    address_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    address_entry.place(x=215, y=357, width=280)  # trebuchet ms

    address_line = Canvas(root, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
    address_line.place(x=215, y=379)

    # ========================================================================
    # ============================Contact no====================================
    # ========================================================================

    contact_label = Label(personal_frame, text="Contact No. ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    contact_label.place(x=370, y=90)

    contact_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    contact_entry.place(x=605, y=357, width=305)  # trebuchet ms

    contact_line = Canvas(root, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
    contact_line.place(x=605, y=379)

    # ========================================================================
    # ============================Job Type====================================
    # ========================================================================

    job_type_label = Label(personal_frame, text="Job Type ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    job_type_label.place(x=10, y=130)

    job_type_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=27)
    job_type_list = ["Part time", "Full time"]
    job_type_combo['values'] = job_type_list
    job_type_combo.current(0)
    job_type_combo.place(x=223, y=397)

    # ========================================================================
    # ============================Register as=====================================
    # ========================================================================

    register_as_label = Label(personal_frame, text="Register as ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    register_as_label.place(x=370, y=130)

    register_as_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=31)

    register_as_list = ["Department Head", "Instructor", "Employee"]
    register_as_combo['values'] = register_as_list
    register_as_combo.current(2)
    register_as_combo.place(x=605, y=397)
    #register_as_combo.bind('<<ComboboxSelected>>', reg_as_event_handle)

    # ========================================================================
    # ============================Qualification===============================
    # ========================================================================

    qualification_label = Label(personal_frame, text="Qualification ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
    qualification_label.place(x=10, y=170)

    qualification_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))
    qualification_entry.place(x=250, y=437, width=240)  # trebuchet ms

    qualification_line = Canvas(root, width=240, height=1.5, bg="#bdb9b1", highlightthickness=0)
    qualification_line.place(x=250, y=460)

    reg_date = time.strftime("%Y/%m/%d")

    reg_as()

    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================

    options_frame = LabelFrame(reg_frame, text="Register Options", bg="white", fg="#4f4e4d", height=80,
                                    width=800, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
    options_frame.config(highlightbackground="red")
    options_frame.place(x=100, y=475)

    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================

    submit_img = ImageTk.PhotoImage(file='Pics\\submit.png')
    submit = Button(options_frame, image=submit_img,
                            font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                            , borderwidth=0, background="white", cursor="hand2",command=validation)
    submit.image = submit_img
    submit.place(x=90, y=10)

    clear_img = ImageTk.PhotoImage(file='Pics\\clear.png')
    clear_button = Button(options_frame, image=clear_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    clear_button.image = clear_img
    clear_button.place(x=250, y=13)

    back_img = ImageTk.PhotoImage(file='Pics\\back.png')
    back_button = Button(options_frame, image=back_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2",command=back)
    back_button.image = back_img
    back_button.place(x=410, y=13)

    exit_img = ImageTk.PhotoImage(file='Pics\\exit.png')
    exit_button = Button(options_frame, image=exit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2", command=exit)
    exit_button.image = exit_img
    exit_button.place(x=570, y=13)

    #root.mainloop()


if __name__ == "__main__":
    regist_emp()