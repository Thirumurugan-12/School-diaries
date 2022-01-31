from distutils import command
from struct import pack
from tkinter import *
from tkinter import ttk
from typing_extensions import _AnnotatedAlias
from PIL import Image,ImageTk 
import os 
import pickle
from cv2 import magnitude 
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
import regisf_stu

def stu_screen():
    def click_go_to_dashboard():
        """returns AdminDashboard class when clicked go to dashboard"""
        dashboard.dashboard()
        root.withdraw()

    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])

    def click_view_all():
        """it will show all the data contains on the student table of cms database, when clicked by default this method
        is called while initializing the class ManageStudent. Exception is handled to avoid run time error which may
        cause by user.
        """
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
            student_tree.delete(*student_tree.get_children())
            for values in data:
                data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
                                values[8],
                                values[9], values[10], values[11], values[12], values[13], values[14]]
                # print(data_list)
                student_tree.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def click_delete_student():
        """when clicked delete students, it will require to select the students and after selecting and
        performing the delete method, it will ask the admin either they are sure they want to delete that student
        or not if yes then student containing that id in student table is deleted."""
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

            tree_view_content = student_tree.focus()
            tree_view_items = student_tree.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            ask = messagebox.askyesno("Warning",
                                        f"Are you sure you want to delete Student having id {tree_view_values}")
            if ask is True:
                query = f"delete from students where student_id={tree_view_values};"
                mycur.execute(query)
                spec.commit()
                #db_connection.delete(query, (tree_view_values,))
                messagebox.showinfo("Success", f" student id {tree_view_values} deleted Successfully")

                click_view_all()
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                    "There is some error deleting the data\n Make sure you have Selected the data")


    def update_stu():
        def tree_event_handle():
            try:
                #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                #db_connection.create(obj_student_database.get_database())

                tree_view_content = student_tree.focus()
                tree_view_items = student_tree.item(tree_view_content)
                # print(tree_view_items)
                tree_view_values = tree_view_items['values']
                tree_view_id = tree_view_items['values'][0]
                # print(tree_view_id)
                get_id.clear()
                list_of_tree.clear()
                get_id.append(tree_view_id)
                for i in tree_view_values:
                    list_of_tree.append(i)
                    # ManageStudent.get_id.append(tree_view_id)
                # print(ManageStudent.list_of_tree)
                # print(tree_view_values)

                ask = messagebox.askyesno("Confirm",
                                        f"Do you want to Update Student having id {tree_view_id}")
                if ask is True:
                    #click_update_student()
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                    "There is some error updating the data\n Make sure you have Selected the data")
        
        tree_event_handle()
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


        def update():
            """updates the data of students from entry fields"""
            try:
                #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                #db_connection.create(obj_student_database.get_database())

                #get_id = ManageStudent.get_id
                data_id = get_id[0]
                # print(data_id)
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
                query = f"update students set email='{email_entry.get()}',f_name='{f_name_entry.get()}', l_name='{l_name_entry.get()}',dob='{dob_entry.get()}',gender='{gender_combo.get()}',address='{address_entry.get()}',contact_no='{contact_entry.get()}'," \
                        f"shift='{shift_combo.get()}', course_enrolled='{course_combo.get()}', batch='{batch_combo.get()}', section_enrolled='{section_combo.get()}' where student_id={data_id}"
                mycur.execute(query)
                #values = (obj_student_database.get_email(), obj_student_database.get_f_name(),
                        #obj_student_database.get_l_name(), obj_student_database.get_dob(),
                        #obj_student_database.get_gender(), obj_student_database.get_address(),
                        #obj_student_database.get_contact(), obj_student_database.get_shift(),
                        #obj_student_database.get_course_id(), obj_student_database.get_batch_id(),
                        #obj_student_database.get_section(), data_id)

                #db_connection.update(query, values)
                spec.commit()
                click_view_all()
                ask = messagebox.askyesnocancel("Success", f"Data having \n Email={email_entry.get()} \n Updated Successfully\n"
                                                        f"Do you want to Go Student Management Dashboard")
                if ask is True:
                    #win = Toplevel()
                    #Frontend.manage_student.ManageStudent(win)
                    #window.withdraw()
                    #win.deiconify()
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error", f"Error due to{msg}")



        

        root = Toplevel()
        root.title('COLLEGE MANAGEMENT SYSTEM')
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
                                , command=update)

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
                                    , borderwidth=0, background="white", cursor="hand2")
                                    #, command=click_back_button)
        back_button.image = back_img
        back_button.place(x=410, y=13)

        exit_img = ImageTk.PhotoImage \
            (file='Pics\\exit.png')
        exit_button = Button(options_frame, image=exit_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=exit)
        exit_button.image = exit_img
        exit_button.place(x=570, y=13)

        a = list_of_tree
        # print(a)
        try:
            email_entry.insert(0, a[3])
            f_name_entry.insert(0, a[1])
            l_name_entry.insert(0, a[2])
            dob_entry.delete(0, END)
            dob_entry.insert(0, a[4])
            gender_combo.set(a[5])
            address_entry.insert(0, a[6])
            contact_entry.insert(0, a[7])
            shift_combo.set(a[8])
            course_combo.set(a[9])
            batch_combo.set(a[10])
            section_combo.set(a[11])
        except IndexError as msg:
            print(msg)

    list_of_tree = []
    get_id = []

    root = Toplevel()
    root.geometry("1067x600")
    root.title("Student Management Dashboard - College Management System")
    #root.iconbitmap('images\\logo.ico')
    root.resizable(False, False)

    manage_student_frame_r = Image.open('Pics\\student_frame.png').resize((1067,600),Image.ANTIALIAS)
    manage_student_frame = ImageTk.PhotoImage(manage_student_frame_r)
    image_panel = Label(root, image=manage_student_frame)
    image_panel.image = manage_student_frame
    image_panel.pack(fill='both', expand='yes')

    #db_connection = Backend.connection.DatabaseConnection()

    txt = "Student Management Dashboard"
    heading = Label(root, text=txt, font=('yu gothic ui', 20, "bold"), bg="white",fg='black',bd=5,relief=FLAT)
    heading.place(x=420, y=23)

    # =======================================================================
    # ========================Left frame ====================================
    # =======================================================================

    left_view_frame = Frame(root, bg="white")
    left_view_frame.place(x=35, y=89, height=470, width=250)

    # =======================================================================
    # ========================Tree view frame================================
    # =======================================================================

    tree_view_frame = Frame(root, bg="white")
    tree_view_frame.place(x=301, y=90, height=473, width=730)

    # =======================================================================
    # ========================frame for personal credentials =================
    # =======================================================================

    personal_frame = LabelFrame(left_view_frame, text="Student Management Options", bg="white", fg="#4f4e4d",height=460,width=240, borderwidth=2.4,font=("yu gothic ui", 12, "bold"))
    personal_frame.config(highlightbackground="red")
    personal_frame.place(x=5, y=8)

    # ========================================================================
    # ============================Add student button===============================
    # ========================================================================

    add_student_r = Image.open('Pics\\add_student.png').resize((225,25),Image.ANTIALIAS)
    add_student = ImageTk.PhotoImage(add_student_r)
    add_student_button = Button(personal_frame, image=add_student, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=regisf_stu.regist_stu)
    add_student_button.image = add_student
    add_student_button.place(x=5, y=100)
    # add_student_button.place(x=36, y=295)

    # ========================================================================
    # ============================Update student button===============================
    # ========================================================================

    update_student_r = Image.open('Pics\\update_student.png').resize((225,25),Image.ANTIALIAS)
    update_student = ImageTk.PhotoImage(update_student_r)
    update_student_button = Button(personal_frame, image=update_student, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=update_stu)
    update_student_button.image = update_student
    update_student_button.place(x=5, y=165)
    # update_student_button.place(x=36, y=355)

    # ========================================================================
    # ============================Delete student button===============================
    # ========================================================================

    delete_student_r = Image.open('Pics\\delete_student.png').resize((225,25),Image.ANTIALIAS)
    delete_student = ImageTk.PhotoImage(delete_student_r)
    delete_student_button = Button(personal_frame, image=delete_student, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=click_delete_student)
    delete_student_button.image = delete_student
    delete_student_button.place(x=5, y=230)
    # delete_student_button.place(x=36, y=405)

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
    style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29844")

    scroll_x = Scrollbar(tree_view_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(tree_view_frame, orient=VERTICAL)
    student_tree = ttk.Treeview(tree_view_frame,
                                        columns=(
                                            "STUDENT ID", "FNAME", "LNAME", "EMAIL", "DOB", "GENDER", "ADDRESS",
                                            "CONTACT NO", "SHIFT", "COURSE ENROLLED", "BATCH", "SECTION",
                                            "REGISTRATION DATE"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=student_tree.xview)
    scroll_y.config(command=student_tree.yview)

    # ==========================TreeView Heading====================
    student_tree.heading("STUDENT ID", text="STUDENT ID")
    student_tree.heading("FNAME", text="FNAME")
    student_tree.heading("LNAME", text="LNAME")
    student_tree.heading("EMAIL", text="EMAIL")
    student_tree.heading("DOB", text="DOB")
    student_tree.heading("GENDER", text="GENDER")
    student_tree.heading("ADDRESS", text="ADDRESS")
    student_tree.heading("CONTACT NO", text="CONTACT NO")
    student_tree.heading("SHIFT", text="SHIFT")
    student_tree.heading("COURSE ENROLLED", text="COURSE ENROLLED")
    student_tree.heading("BATCH", text="BATCH")
    student_tree.heading("SECTION", text="SECTION")
    student_tree.heading("REGISTRATION DATE", text="REGISTRATION DATE")
    student_tree["show"] = "headings"

    # ==========================TreeView Column====================
    student_tree.column("STUDENT ID", width=150)
    student_tree.column("FNAME", width=170)
    student_tree.column("LNAME", width=170)
    student_tree.column("EMAIL", width=200)
    student_tree.column("ADDRESS", width=150)
    student_tree.column("GENDER", width=150)
    student_tree.column("CONTACT NO", width=150)
    student_tree.column("DOB", width=150)
    student_tree.column("SHIFT", width=150)
    student_tree.column("COURSE ENROLLED", width=150)
    student_tree.column("BATCH", width=100)
    student_tree.column("SECTION", width=100)
    student_tree.column("REGISTRATION DATE", width=150)
    student_tree.pack(fill=BOTH, expand=1)

    click_view_all()


    #root.mainloop()

if __name__ == "__main__":
    stu_screen()