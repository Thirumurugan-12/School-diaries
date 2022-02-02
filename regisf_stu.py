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


def regist_stu():
    def validation():
        """this will validate if the username and email of entry fields are already in database table named student or
        not if return True, error message is thrown displaying email/username already exists"""
        try:
            #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            #db_connection.create(obj_student_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            query = "select * from students;"
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

        elif email_entry.get() in email_list:
            messagebox.showerror("Already Exists", f"{email_entry.get()} Email ID Already Exists")

        elif password_entry.get() != c_password_entry.get():
            messagebox.showerror("Not Matched", "Password Does not Matched")

        else:
            click_submit()

    def click_submit():
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            #db_connection.create(obj_student_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            #obj_student_database = Model_class.student_registration.StudentRegistration(username_entry.get(),
                                                                                        #email_entry.get(),
                                                                                        #password_entry.get(),
                                                                                        #f_name_entry.get(),
                                                                                        #l_name_entry.get(),
                                                                                        #dob_entry.get(),
                                                                                        #gender_combo.get(),
                                                                                        #address_entry.get(),
                                                                                        #contact_entry.get(),
                                                                                        #shift_combo.get(),
                                                                                        #course_combo.get(),
                                                                                        #batch_combo.get(),
                                                                                        #section_combo.get(),
                                                                                        #reg_date)
            query = f"insert into students (username,email,password,f_name,l_name,dob,gender,address," \
                    f"contact_no,shift,course_enrolled,batch,section_enrolled,reg_date) values ('{username_entry.get()}','{email_entry.get()}','{password_entry.get()}','{f_name_entry.get()}','{l_name_entry.get()}','{dob_entry.get()}'," \
                    f"'{gender_combo.get()}','{address_entry.get()}','{contact_entry.get()}','{shift_combo.get()}','{course_combo.get()}','{batch_combo.get()}','{section_combo.get()}','{reg_date}');"
            #values = (obj_student_database.get_username(), obj_student_database.get_email(),
                        #obj_student_database.get_password(), obj_student_database.get_f_name(),
                        #obj_student_database.get_l_name(), obj_student_database.get_dob(),
                        #obj_student_database.get_gender(), obj_student_database.get_address(),
                        #obj_student_database.get_contact(), obj_student_database.get_shift(),
                        #obj_student_database.get_course_id(), obj_student_database.get_batch_id(),
                        #obj_student_database.get_section(), obj_student_database.get_reg_date())
            # print(values)
            mycur.execute(query)
            spec.commit()
            # print(values)
            messagebox.showinfo("Success", f"Data inserted Successfully\n Name={username_entry.get()},\n "
                                            f"registration={reg_date}")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There is some error Submitting Credentials ")

    def click_clear_button():
        """this will clear entire field to default when click on clear button"""
        username_entry.delete(0, END)
        f_name_entry.delete(0, END)
        l_name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        c_password_entry.delete(0, END)
        dob_entry.delete(0, END)
        gender_combo.current(0)
        address_entry.delete(0, END)
        contact_entry.delete(0, END)
        shift_combo.current(0)
        batch_combo.current(0)
        course_combo.current(0)
        batch_combo.current(0)
        section_combo.current(0)

    def back():
        root.destroy()

    def exit():
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if (ask == True):
            root.destroy()

    root = Toplevel()
    root.title('SCHOOL MANAGEMENT SYSTEM')
    root.geometry('1067x600')
    root.config(bg="#f29844")
    #root.iconbitmap('images\\logo.ico')
    root.resizable(False, False)
    #manage_student_frame = ImageTk.PhotoImage(file='Pics\\student_frame.png')

    # ======================Variables======================

    reg_frame = Frame(root, bg="#ffffff", width=1000, height=560)
    reg_frame.place(x=30, y=30)

    heading = Label(reg_frame, text="Student Registration Form", font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=200, y=0, width=600)


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
    username_line.place(x=230, y=140)

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
    email_line.place(x=555, y=140)

    # ========================================================================
    # ============================Password====================================
    # ========================================================================

    password_label = Label(cred_frame, text="Password ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    password_label.place(x=10, y=50)

    password_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12), show="*")
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
                                    font=("yu gothic ui semibold", 12), show="*")
    c_password_entry.place(x=650, y=157, width=255)  # trebuchet ms

    c_password_line = Canvas(root, width=255, height=1.5, bg="#bdb9b1", highlightthickness=0)
    c_password_line.place(x=650, y=180)


    # =======================================================================
    # ========================frame for personal credentials ================
    # =======================================================================

    personal_frame = LabelFrame(reg_frame, text="Personal Details", bg="white", fg="#4f4e4d", height=265,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
    personal_frame.config(highlightbackground="red")
    personal_frame.place(x=100, y=200)



    # ========================================================================
    # ============================First name==================================
    # ========================================================================
    f_name_label = Label(personal_frame, text="First Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    f_name_label.place(x=10, y=10)

    f_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    f_name_entry.place(x=235, y=267, width=260)  # trebuchet ms

    f_name_line = Canvas(root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
    f_name_line.place(x=235, y=290)

    # ========================================================================
    # ============================Last name===================================
    # ========================================================================

    l_name_label = Label(personal_frame, text="Last Name ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    l_name_label.place(x=370, y=10)

    l_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    l_name_entry.place(x=595, y=267, width=315)  # trebuchet ms

    l_name_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
    l_name_line.place(x=595, y=290)

    # ========================================================================
    # ============================DOB=========================================
    # ========================================================================

    dob_label = Label(personal_frame, text="DOB ", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
    dob_label.place(x=10, y=50)

    dob_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                            font=("yu gothic ui semibold", 12))
    dob_entry.insert(0, "mm/dd/yyyy")
    dob_entry.place(x=190, y=307, width=305)  # trebuchet ms
    #dob_entry.bind("<1>", pick_date)

    dob_line = Canvas(root, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
    dob_line.place(x=190, y=329)

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

    gender_list = ['Male', 'Female', 'Rather not say']
    gender_combo['values'] = gender_list
    # gender_combo.current(0)
    gender_combo.place(x=570, y=307)

    # gender_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
    # gender_line.place(x=595, y=369)

    # ========================================================================
    # ============================Address====================================
    # ========================================================================

    address_label = Label(personal_frame, text="Address ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    address_label.place(x=10, y=90)

    address_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    address_entry.place(x=215, y=347, width=280)  # trebuchet ms

    address_line = Canvas(root, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
    address_line.place(x=215, y=370)

    # ========================================================================
    # ============================Contact no====================================
    # ========================================================================

    contact_label = Label(personal_frame, text="Contact No. ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    contact_label.place(x=370, y=90)

    contact_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                font=("yu gothic ui semibold", 12))
    contact_entry.place(x=605, y=347, width=305)  # trebuchet ms

    contact_line = Canvas(root, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
    contact_line.place(x=605, y=370)

    # ========================================================================
    # ============================Shift No====================================
    # ========================================================================

    shift_label = Label(personal_frame, text="Shift ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    shift_label.place(x=10, y=130)

    shift_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                    width=28)
    shift_list = ["Morning", "Day", "Evening"]
    shift_combo['values'] = shift_list
    shift_combo.current(0)
    shift_combo.place(x=213, y=387)

    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])

    try:
        #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
        #db_connection.create(obj_student_database.get_database())
        a=load_data()
        host=a[0]
        username = a[2]
        password = a[3]
        port=a[1]
        
        
        spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
        mycur=spec.cursor()

        query = "select * from section"
        mycur.execute(query)
        #data=mycur.fetchall()
        query = "select * from section"
        section_tuple = mycur.fetchall()
        # print(section_tuple)
        section_list = []
        for i in section_tuple:
            section_name = i[2]
            section_list.append(section_name)
            # print(section_name)
            # print(section_list)

    except BaseException as msg:
        print(msg)

    try:
        #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
        #db_connection.create(obj_student_database.get_database())
        a=load_data()
        host=a[0]
        username = a[2]
        password = a[3]
        port=a[1]
        
        
        spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
        mycur=spec.cursor()

        query = "select * from course"
        mycur.execute(query)
        course_tuple = mycur.fetchall()

        # print(course_tuple)
        course_list = []
        for i in course_tuple:
            course_name = i[1]
            course_list.append(course_name)
            # print(course_name)
            # print(course_list)

    except BaseException as msg:
        print(msg)

    try:
        #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
        #db_connection.create(obj_student_database.get_database())
        a=load_data()
        host=a[0]
        username = a[2]
        password = a[3]
        port=a[1]
        
        
        spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
        mycur=spec.cursor()

        query = "select * from batch"
        mycur.execute(query)
        batch_tuple = mycur.fetchall()
        # print(batch_tuple)
        batch_list = []
        for i in batch_tuple:
            batch_name = i[1]
            batch_list.append(batch_name)
            # print(batch_name)
            # print(batch_list)

    except BaseException as msg:
        print(msg)









    # ========================================================================
    # ============================Course enrolled=============================
    # ========================================================================

    course_label = Label(personal_frame, text="Course Enrolled ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    course_label.place(x=370, y=130)

    course_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=28)

    course_combo['values'] = course_list
    try:
        course_combo.current(0)
    except:
        messagebox.showerror("Error","You must add course first")
    course_combo.place(x=635, y=387)

    # ========================================================================
    # ============================Batch=======================================
    # ========================================================================

    batch_label = Label(personal_frame, text="Batch ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    batch_label.place(x=10, y=170)

    batch_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                    width=28)

    batch_combo['values'] = batch_list
    try:
        batch_combo.current(0)
    except:
        messagebox.showerror("Error", "You must add batch first")
    batch_combo.place(x=213, y=427)

    # ========================================================================
    # ============================Section=====================================
    # ========================================================================

    section_label = Label(personal_frame, text="Section ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    section_label.place(x=370, y=170)

    section_combo = ttk.Combobox(root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                        width=28)

    section_combo['values'] = section_list
    try:
        section_combo.current(0)
    except:
        messagebox.showerror("Error", "You must add section first")
    section_combo.place(x=635, y=427)

    reg_date = time.strftime("%Y/%m/%d")

    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================

    options_frame = LabelFrame(reg_frame, text="Register Options", bg="white", fg="#4f4e4d", height=83,
                                    width=800, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
    options_frame.config(highlightbackground="red")
    options_frame.place(x=100, y=470)

    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================
    submit_img = ImageTk.PhotoImage \
        (file='Pics\\submit.png')

    submit = Button(options_frame, image=submit_img,
                            font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                            , borderwidth=0, background="white", cursor="hand2"
                            , command=validation)

    submit.image = submit_img                      
    submit.place(x=90, y=10)

    clear_img = ImageTk.PhotoImage \
        (file='Pics\\clear.png')
    clear_button = Button(options_frame, image=clear_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2"
                                ,command=click_clear_button)
    clear_button.image = clear_img
    clear_button.place(x=250, y=13)

    back_img = ImageTk.PhotoImage \
        (file='Pics\\back.png')
    back_button = Button(options_frame, image=back_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2"
                                , command=back)
    back_button.image = back_img
    back_button.place(x=410, y=13)

    exit_img = ImageTk.PhotoImage \
        (file='Pics\\exit.png')
    exit_button = Button(options_frame, image=exit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2", command=exit)
    exit_button.image = exit_img
    exit_button.place(x=570, y=13)


    #root.mainloop()

if __name__ =="__main__":
    regist_stu()