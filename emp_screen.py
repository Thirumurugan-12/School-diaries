from distutils import command
from tkinter import *
from tkinter import ttk
from typing_extensions import _AnnotatedAlias
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
import dashboard
import csv
import regist_emp


def emp_screen():
    def click_delete_employee():
        """when clicked delete employees, it will require to select the employees and after selecting and
        performing the delete method, it will ask the admin either they are sure they want to delete that employee
        or not if yes then employee containing that id in employee table is deleted."""
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

            tree_view_content = employee_tree.focus()
            tree_view_items = employee_tree.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            ask = messagebox.askyesno("Warning",
                                        f"Are you sure you want to delete employee having id {tree_view_values}")
            if ask is True:
                query = f"delete from employees where employee_id={tree_view_values};"
                mycur.execute(query)
                spec.commit()
                #db_connection.delete(query, (tree_view_values,))
                messagebox.showinfo("Success", f" Employee id {tree_view_values} deleted Successfully")

                click_view_all()
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                    "There is some error deleting the data\n Make sure you have Selected the data")



    def update_emp():
        def tree_event_handle():
            try:
                #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                #db_connection.create(obj_student_database.get_database())

                tree_view_content = employee_tree.focus()
                tree_view_items = employee_tree.item(tree_view_content)
                # print(tree_view_items)
                tree_view_values = tree_view_items['values']
                tree_view_id = tree_view_items['values'][0]
                # print("tree",tree_view_id)
                get_id.clear()
                get_id.append(tree_view_id)
                list_of_tree.clear()
                # print("Appended", ManageEmployee.get_id)
                for i in tree_view_values:
                    list_of_tree.append(i)

                # print(ManageEmployee.list_of_tree)
                # print(tree_view_values)

                ask = messagebox.askyesno("Confirm",
                                        f"Do you want to Update employee having id {tree_view_id}")
                if ask is True:
                    #update()
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                    "There is some error updating the data\n Make sure you have Selected the data")
        
        tree_event_handle()
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

        def update():
            """updates the data of employees from entry fields"""
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

                #get_id = get_id
                data_id= get_id[0]
                # print(data_id)
                #obj_employee_database = Model_class.employee_registration.EmployeeRegistration(username_entry.get(),
                                                                                            #email_entry.get(),
                                                                                            #email_entry.get(),
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
                query = f"update employees set email='{email_entry.get()}',f_name='{f_name_entry.get()}', l_name={l_name_entry.get()},dob='{dob_entry.get()}',gender='{gender_combo.get()}',address='{address_entry.get()}',contact_no='{contact_entry.get()}'," \
                        f"job_type='{job_type_combo.get()}', registered_as='{register_as_combo.get()}', qualification='{qualification_entry.get()}', department='{department_combo.get()}' where employee_id={data_id}"
                mycur.execute(query)
                spec.commit()
                #values = (obj_employee_database.get_email(), obj_employee_database.get_f_name(),
                        #obj_employee_database.get_l_name(), obj_employee_database.get_dob(),
                        #obj_employee_database.get_gender(), obj_employee_database.get_address(),
                        #obj_employee_database.get_contact(), obj_employee_database.get_job(),
                        #obj_employee_database.get_reg_as(), obj_employee_database.get_qualification(),
                        #obj_employee_database.get_department(), data_id)

                #db_connection.update(query, values)

                ask=messagebox.askyesnocancel("Success", f"Data having \n Email={email_entry.get()} \n Updated Successfully\n"
                                                    f"Do you want to Go Employee Dashboard")

                click_view_all()
                if ask is True:
                    #win = Toplevel()
                    #Frontend.manage_employee.ManageEmployee(win)
                    #window.withdraw()
                    #win.deiconify()
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",f"Error due to{msg}")

        global username_entry,password_entry,email_entry,f_name_entry,l_name_entry,dob_entry,gender_combo,address_entry,contact_entry,job_type_combo,register_as_combo,qualification_entry,department_combo
                                                                                            

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
        info = Label(cred_frame,text="*You cant change Username and password leave the fields blank",bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        info.place(x=20,y=80)
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
                                , borderwidth=0, background="white", cursor="hand2",command=update)
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
                                    , borderwidth=0, background="white", cursor="hand2")
        back_button.image = back_img
        back_button.place(x=410, y=13)

        exit_img = ImageTk.PhotoImage(file='Pics\\exit.png')
        exit_button = Button(options_frame, image=exit_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=exit)
        exit_button.image = exit_img
        exit_button.place(x=570, y=13)

        a = list_of_tree
        print(a)
        try:
            #username_entry.insert(0,)
            email_entry.insert(0, a[3])
            f_name_entry.insert(0, a[1])
            l_name_entry.insert(0, a[2])
            dob_entry.delete(0, END)
            dob_entry.insert(0, a[4])
            gender_combo.set(a[5])
            address_entry.insert(0, a[6])
            contact_entry.insert(0, a[7])
            job_type_combo.set(a[8])
            register_as_combo.set(a[11])
            qualification_entry.insert(0,a[10])
            department_combo.set(a[9])
        except IndexError as msg:
            print(msg)


    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])

    def click_go_to_dashboard():
        """returns AdminDashboard class when clicked go to dashboard"""
        dashboard.dashboard()
        root.withdraw()

    def click_view_all():
        """it will show all the data contains on the employee table of cms database, when clicked by default this method
        is called while initializing the class ManageEmployee. Exception is handled to avoid run time error which may
        cause by user."""
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
            query = "select * from employees;"
            mycur.execute(query)
            data = mycur.fetchall()
            # print(data)
            employee_tree.delete(*employee_tree.get_children())
            for values in data:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                values[8],
                                values[9], values[10], values[13], values[12], values[11], values[14]]
                # print(data_list)
                employee_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    list_of_tree = []
    get_id = []

    root = Toplevel()
    root.geometry("1067x600")
    root.title("Manage Employee - College Management System")
    #root.iconbitmap('images\\logo.ico')
    root.resizable(False, False)


    manage_student_frame_r = Image.open('Pics\\student_frame.png').resize((1067,600),Image.ANTIALIAS)
    manage_student_frame = ImageTk.PhotoImage(manage_student_frame_r)
    image_panel = Label(root, image=manage_student_frame)
    image_panel.image = manage_student_frame
    image_panel.pack(fill='both', expand='yes')

    #db_connection = Backend.connection.DatabaseConnection()


    heading = Label(root, text="Employee Management Dashboard", font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=420, y=26, width=640)


    #left frame
    left_view_frame = Frame(root, bg="white")
    left_view_frame.place(x=35, y=89, height=470, width=250)


    #tree view frame
    tree_view_frame = Frame(root, bg="white")
    tree_view_frame.place(x=301, y=90, height=473, width=730)


    # =======================================================================
    # ========================frame for personal credentials =================
    # =======================================================================

    personal_frame = LabelFrame(left_view_frame, text="Employee Management Options", bg="white", fg="#4f4e4d",
                                height=460,
                                width=240, borderwidth=2.4,
                                font=("yu gothic ui", 13, "bold"))
    personal_frame.config(highlightbackground="red")
    personal_frame.place(x=5, y=8)

    # ========================================================================
    # ============================Add employee button===============================
    # ========================================================================

    #add_admin = ImageTk.PhotoImage(file='images\\add_admin.png')
    #add_admin_button = Button(personal_frame, image=add_admin, relief=FLAT, borderwidth=0,
                                        #activebackground="white", bg="white", cursor="hand2")
    #add_admin_button.place(x=8, y=60)

    # ========================================================================
    # ============================Add employee button===============================
    # ========================================================================

    add_employee_r = Image.open('Pics\\add_employee.png').resize((225,25),Image.ANTIALIAS)
    add_employee = ImageTk.PhotoImage(add_employee_r)
    add_employee_button = Button(personal_frame, image=add_employee, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white", cursor="hand2",command=regist_emp.regist_emp)
    add_employee_button.image = add_employee
    add_employee_button.place(x=8, y=100)
    # add_employee_button.place(x=36, y=295)

    # ========================================================================
    # ============================Update employee button===============================
    # ========================================================================

    update_employee_r = Image.open('Pics\\update_employee.png').resize((225,25),Image.ANTIALIAS)
    update_employee = ImageTk.PhotoImage(update_employee_r)
    update_employee_button = Button(personal_frame, image=update_employee, relief=FLAT, borderwidth=0,
                                            activebackground="white", bg="white", cursor="hand2",command= update_emp)
    update_employee_button.image = update_employee
    update_employee_button.place(x=8, y=165)
    # update_employee_button.place(x=36, y=355)

    # ========================================================================
    # ============================Delete employee button===============================
    # ========================================================================

    delete_employee_r = Image.open('Pics\\delete_employee.png').resize((225,25),Image.ANTIALIAS)
    delete_employee = ImageTk.PhotoImage(delete_employee_r)
    delete_employee_button = Button(personal_frame, image=delete_employee, relief=FLAT, borderwidth=0,
                                            activebackground="white", bg="white", cursor="hand2",command=click_delete_employee)
    delete_employee_button.image = delete_employee
    delete_employee_button.place(x=8, y=230)
    # delete_employee_button.place(x=36, y=405)


    # ========================================================================
    # ============================Goto Main dashboard button===============================
    # ========================================================================

    goto_dashboard_r = Image.open('Pics\\goto_dashboard.png').resize((225,25),Image.ANTIALIAS)
    goto_dashboard = ImageTk.PhotoImage (goto_dashboard_r)
    goto_dashboard_button = Button(personal_frame, image=goto_dashboard, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=click_go_to_dashboard)
    goto_dashboard_button.image = goto_dashboard
    goto_dashboard_button.place(x=5, y=295)

    # =======================================================================
    # ========================Starting Tree View=============================
    # =======================================================================

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")

    scroll_x = Scrollbar(tree_view_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(tree_view_frame, orient=VERTICAL)
    employee_tree = ttk.Treeview(tree_view_frame,
                                        columns=(
                                            "EMPLOYEE ID", "FNAME", "LNAME", "EMAIL", "DOB", "GENDER", "ADDRESS",
                                            "CONTACT NO", "JOB TYPE", "DEPARTMENT", "QUALIFICATION", "REGISTERED AS",
                                            "REGISTRATION DATE"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=employee_tree.xview)
    scroll_y.config(command=employee_tree.yview)

    # ==========================TreeView Heading====================
    employee_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
    employee_tree.heading("FNAME", text="FNAME")
    employee_tree.heading("LNAME", text="LNAME")
    employee_tree.heading("EMAIL", text="EMAIL")
    employee_tree.heading("DOB", text="DOB")
    employee_tree.heading("GENDER", text="GENDER")
    employee_tree.heading("ADDRESS", text="ADDRESS")
    employee_tree.heading("CONTACT NO", text="CONTACT NO")
    employee_tree.heading("JOB TYPE", text="JOB TYPE")
    employee_tree.heading("DEPARTMENT", text="DEPARTMENT")
    employee_tree.heading("QUALIFICATION", text="QUALIFICATION")
    employee_tree.heading("REGISTERED AS", text="REGISTERED AS")
    employee_tree.heading("REGISTRATION DATE", text="REGISTRATION DATE")
    employee_tree["show"] = "headings"

    # ==========================TreeView Column====================
    employee_tree.column("EMPLOYEE ID", width=150)
    employee_tree.column("FNAME", width=170)
    employee_tree.column("LNAME", width=170)
    employee_tree.column("EMAIL", width=200)
    employee_tree.column("ADDRESS", width=150)
    employee_tree.column("GENDER", width=150)
    employee_tree.column("CONTACT NO", width=150)
    employee_tree.column("DOB", width=150)
    employee_tree.column("JOB TYPE", width=150)
    employee_tree.column("DEPARTMENT", width=150)
    employee_tree.column("QUALIFICATION", width=150)
    employee_tree.column("REGISTERED AS", width=150)
    employee_tree.column("REGISTRATION DATE", width=150)
    employee_tree.pack(fill=BOTH, expand=1)
    # emp_tree.bind("<ButtonRelease-1>", getcredon_click)
    #employee_tree.bind("<Button-3>", do_popup)
    #employee_tree.bind("<Delete>", click_delete_key)
    #employee_tree.bind("<Return>", tree_double_click)
    #employee_tree.bind("<Double-Button-1>", tree_double_click)
    #search_start()
    #search_by.current(0)
    click_view_all()

    #root.mainloop()

if __name__ == "__main__":
    emp_screen()