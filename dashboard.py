from cProfile import label
from distutils import command
from logging import root
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
import section_screen
import batch_screen
import department_screen
import emp_screen
import student_screen


def load_data():
    f=open("Credentials.csv","r")
    s=csv.reader(f,delimiter="-")
    d=[]
    for i in s:
        d.append(i)
    a=d[::-1]
    return (a[0])
    
def click_logout():
    root.destroy()

def dashboard():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def click_home():
        """set to default home tab where details like no. of students, employees, department shows """

        home_frame = Frame(root)
        home_frame.place(x=120, y=105, height=440, width=910)

        home_dashboard_fram_r=Image.open('files\home_new.png')
        home_dashboard_fram_r=home_dashboard_fram_r.resize((910,440),Image.ANTIALIAS)
        home_dashboard_frame = ImageTk.PhotoImage(home_dashboard_fram_r)
        home_panel = Label(home_frame, image=home_dashboard_frame, bg="white")
        home_panel.image= home_dashboard_frame
        home_panel.pack(fill='both', expand='yes')

        try:
            #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
            #self.db_connection.create(obj_student_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            print(a)
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()

            query = "SELECT COUNT(*) FROM students;"
            mycur.execute(query)
            data=mycur.fetchall()


            
            global no_students
            for value in data:
                no_students = value[0]

            total_students = Label(home_frame, text=f" TOTAL\n {no_students}\n STUDENTS",
                                   font=("yu gothic ui", 20, "bold"),
                                   background="white", fg='#e67c0b')
            total_students.place(x=180, y=65)

            query = "SELECT COUNT(*) FROM employees;"
            mycur.execute(query)
            data = mycur.fetchall()
            global no_employees
            for value in data:
                no_employees = value[0]

            total_employees = Label(home_frame, text=f" TOTAL\n {no_employees}\n EMPLOYEES",
                                    font=("yu gothic ui", 20, "bold"),
                                    background="white", fg='#e67c0b')
            total_employees.place(x=550, y=65)

            query = "SELECT COUNT(*) FROM department;"
            mycur.execute(query)
            data = mycur.fetchall()
            global no_department
            for value in data:
                no_department = value[0]

            total_department = Label(home_frame, text=f" TOTAL\n {no_department}\n DEPARTMENTS",
                                     font=("yu gothic ui", 20, "bold"),
                                     background="white", fg='#e67c0b')
            total_department.place(x=175, y=250)

        except BaseException as msg:
            print(msg)
    
    def click_manage():
            """ opens new frame from where one can go to manage students, employees, departments, course, section
            and batch"""

            manage_frame = Frame(root, bg="white")
            manage_frame.place(x=120, y=105, height=440, width=910)
            manage_dashboard_frame_r = Image.open('files\\manage_frame1.png')
            manage_dashboard_frame_r=manage_dashboard_frame_r.resize((910,440),Image.ANTIALIAS)
            manage_dashboard_frame = ImageTk.PhotoImage(manage_dashboard_frame_r)
            manage_panel = Label(manage_frame, image=manage_dashboard_frame, bg="white")
            manage_panel.image = manage_dashboard_frame
            manage_panel.pack(fill='both', expand='yes')
            
            student_r=Image.open('Pics\\student.png')
            student_r=student_r.resize((100,100),Image.ANTIALIAS)
            student = ImageTk.PhotoImage(student_r)
            student_button = Button(manage_frame, image=student, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=student_screen.stu_screen)
            student_button.image = student
            student_button.place(x=120, y=115)

            employee_r=Image.open('Pics\\employee.png')
            employee_r=employee_r.resize((100,100),Image.ANTIALIAS)
            employee = ImageTk.PhotoImage(employee_r)
            employee_button = Button(manage_frame, image=employee, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=emp_screen.emp_screen)
            employee_button.image =employee
            employee_button.place(x=395, y=115)

            department_r=Image.open('Pics\\department.png')
            department_r=department_r.resize((100,100),Image.ANTIALIAS)
            department = ImageTk.PhotoImage(department_r)
            department_button = Button(manage_frame, image=department, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=department_screen.depart_screen)
            department_button.image = department
            department_button.place(x=672, y=115)

            course_r=Image.open('Pics\\course.png')
            course_r=course_r.resize((100,100),Image.ANTIALIAS)
            course = ImageTk.PhotoImage(course_r)
            course_button = Button(manage_frame, image=course, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=course_screen.course_screen)
            course_button.image = course
            course_button.place(x=121, y=300)

            section_r=Image.open('Pics\\section.png')
            section_r=section_r.resize((100,100),Image.ANTIALIAS)
            section = ImageTk.PhotoImage(section_r)
            section_button = Button(manage_frame, image=section, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=section_screen.section_screen)
            section_button.image = section
            section_button.place(x=396, y=300)


            batch_r=Image.open('Pics\\batch.png')
            batch_r=batch_r.resize((100,100),Image.ANTIALIAS)
            batch = ImageTk.PhotoImage(batch_r)
            batch_button = Button(manage_frame, image=batch, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command= batch_screen.batch_screen)
            batch_button.image = batch
            batch_button.place(x=673, y=300)

    def click_view():
        """ Displays partial data into tree view of students, employees, departments, courses when clicked view tab
        on interface """
        view_frame = Frame(root, bg="white")
        view_frame.place(x=120, y=105, height=440, width=910)

        view_dashboard_frame_r=Image.open('Pics\\view_frame.png')
        view_dashboard_frame_r=view_dashboard_frame_r.resize((910,440),Image.ANTIALIAS)
        view_dashboard_frame = ImageTk.PhotoImage(view_dashboard_frame_r)
        view_panel = Label(view_frame, image=view_dashboard_frame, bg="white")
        view_panel.image=view_dashboard_frame
        view_panel.pack(fill='both', expand='yes')




        #department_view_label = Label(view_frame, text="View Department Information ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        #department_view_label.place(x=770, y=290)

        #course_view_label = Button(view_frame, text="View Course Information ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=studentinfo)
        #course_view_label.place(x=170, y=290)



        def studentinfo():
            # ========================================================================
            # ============================Displaying Student Information==============
            # ========================================================================
            def view_student_information():
            #"""fetched data of students from database and inserted required index to student tree view"""
                
                try:
                    #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                    #self.db_connection.create(obj_student_database.get_database())
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
                    #self.a = Label(self.window)
                    # print(data)
                    #self.view_student_tree.delete(*self.view_student_tree.get_children())
                    for values in data:
                        data_list = [values[0], values[4], values[11], values[9]]
                        # print(data_list)
                        view_student_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)

            #student_view_label = Label(view_frame, text="View Students Information ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
            #student_view_label.place(x=170, y=6)

            view_student_frame = Toplevel()#Frame(view_frame, bg="white")
            view_student_frame.geometry("800x500")
            #view_student_frame.place(x=10, y=40, height=250, width=575)

            style = ttk.Style()
            style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
            #style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="black")

            scroll_y = Scrollbar(view_student_frame, orient=VERTICAL)
            scroll_x = Scrollbar(view_student_frame, orient=HORIZONTAL)
            view_student_tree = ttk.Treeview(view_student_frame,columns=("STUDENT ID", "STUDENT NAME", "COURSE ENROLLED", "PHONE NO."),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,height=2)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=view_student_tree.xview)
            scroll_y.config(command=view_student_tree.yview)
            

            
            # ==========================TreeView Heading====================
            view_student_tree.heading("STUDENT ID", text="STUDENT ID")
            view_student_tree.heading("STUDENT NAME", text="STUDENT NAME")
            view_student_tree.heading("COURSE ENROLLED", text="COURSE ENROLLED")
            view_student_tree.heading("PHONE NO.", text="PHONE NO.")
            view_student_tree["show"] = "headings"

            # ==========================TreeView Column====================
            view_student_tree.column("STUDENT ID", width=50)
            view_student_tree.column("STUDENT NAME", width=150)
            view_student_tree.column("COURSE ENROLLED", width=100)
            view_student_tree.column("PHONE NO.", width=100)
            view_student_tree.pack(fill=BOTH, expand=1)

            view_student_information()
        #course_view_label = Button(view_frame, text="View Course Information ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=studentinfo)
        #course_view_label.place(x=170, y=290)

        def employee_info():
            # ========================================================================
            # =========================Displaying instructor Information==============
            # ========================================================================
            def view_employee_information():
            #"""fetched data of employees from database and inserted required index to employee tree view"""
                try:
                    #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                    #self.db_connection.create(obj_student_database.get_database())
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
                    #self.a = Label(self.window)
                    # print(data)
                    #self.view_student_tree.delete(*self.view_student_tree.get_children())
                    for values in data:
                        data_list = [values[0], values[4], values[13], values[11]]
                        # print(data_list)
                        view_employee_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)

            view_employee_frame = Toplevel()#(view_frame, bg="white")
            view_employee_frame.geometry("800x500")
            #view_employee_frame.place(x=595, y=40, height=250, width=575)
            #employee_view_label = Label(view_frame, text="View Employees Information ", bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
            #employee_view_label.place(x=600, y=5)

            scroll_y_e = Scrollbar(view_employee_frame, orient=VERTICAL)
            scroll_x_e = Scrollbar(view_employee_frame, orient=HORIZONTAL)
            view_employee_tree = ttk.Treeview(view_employee_frame,columns=("EMPLOYEE ID", "EMPLOYEE NAME", "DEPARTMENT", "EMPLOYEE TYPE"),xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
            scroll_x_e.pack(side=BOTTOM, fill=X)
            scroll_y_e.pack(side=RIGHT, fill=Y)
            scroll_x_e.config(command=view_employee_tree.xview)
            scroll_y_e.config(command=view_employee_tree.yview)

            # ==========================TreeView Heading====================
            view_employee_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
            view_employee_tree.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")
            view_employee_tree.heading("DEPARTMENT", text="DEPARTMENT")
            view_employee_tree.heading("EMPLOYEE TYPE", text="EMPLOYEE TYPE")
            view_employee_tree["show"] = "headings"

            # ==========================TreeView Column====================
            view_employee_tree.column("EMPLOYEE ID", width=50)
            view_employee_tree.column("EMPLOYEE NAME", width=150)
            view_employee_tree.column("DEPARTMENT", width=100)
            view_employee_tree.column("EMPLOYEE TYPE", width=100)
            view_employee_tree.pack(fill=BOTH, expand=1)

            view_employee_information()

        def course_info():
            # =======================================================================
            # ============================Displaying Course Information==============
            # ========================================================================
            def view_course_information():
                #"""fetched data of course from database and inserted required index to course tree view"""
                try:
                    #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                    #self.db_connection.create(obj_student_database.get_database())
                    a=load_data()
                    host=a[0]
                    username = a[2]
                    password = a[3]
                    port=a[1]
                    
                    spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
                    mycur=spec.cursor()
                    query = "select * from course;"
                    mycur.execute(query)
                    data = mycur.fetchall()

                    #data = self.db_connection.select(query)
                    # print(data)
                    # self.view_course_tree.delete(*self.view_course_tree.get_children())
                    for values in data:
                        data_list = [values[0], values[1], values[2], values[3]]
                        # print(data_list)
                        view_course_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)
            view_course_frame = Toplevel() #Frame(view_frame, bg="white")
            view_course_frame.geometry("800x500")
            #view_course_frame.place(x=10, y=320, height=250, width=575)

            scroll_y_e = Scrollbar(view_course_frame, orient=VERTICAL)
            scroll_x_e = Scrollbar(view_course_frame, orient=HORIZONTAL)
            view_course_tree = ttk.Treeview(view_course_frame,columns=("COURSE ID", "COURSE NAME", "COURSE DURATION", "COURSE CREDIT"),xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
            scroll_x_e.pack(side=BOTTOM, fill=X)
            scroll_y_e.pack(side=RIGHT, fill=Y)
            scroll_x_e.config(command=view_course_tree.xview)
            scroll_y_e.config(command=view_course_tree.yview)

            # ==========================TreeView Heading====================
            view_course_tree.heading("COURSE ID", text="COURSE ID")
            view_course_tree.heading("COURSE NAME", text="COURSE NAME")
            view_course_tree.heading("COURSE DURATION", text="COURSE DURATION")
            view_course_tree.heading("COURSE CREDIT", text="COURSE CREDIT")
            view_course_tree["show"] = "headings"

            # ==========================TreeView Column====================
            view_course_tree.column("COURSE ID", width=50)
            view_course_tree.column("COURSE NAME", width=150)
            view_course_tree.column("COURSE DURATION", width=100)
            view_course_tree.column("COURSE CREDIT", width=100)
            view_course_tree.pack(fill=BOTH, expand=1)

            view_course_information()

        def dep_info():
            # ========================================================================
            # =========================Displaying Department Information==============
            # ========================================================================
            def view_department_information():
            #"""fetched data of department from database and inserted required index to department tree view"""
                try:
                    #obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
                    #self.db_connection.create(obj_student_database.get_database())
                    a=load_data()
                    host=a[0]
                    username = a[2]
                    password = a[3]
                    port=a[1]
                    
                    spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
                    mycur=spec.cursor()
                    query = "select * from department;"
                    mycur.execute(query)
                    data = mycur.fetchall()

                    for values in data:
                        data_list = [values[0], values[2], values[1]]
                        # print(data_list)
                        view_department_tree.insert('', END, values=data_list)

                except BaseException as msg:
                    print(msg)

            view_department_frame = Toplevel()
            view_department_frame.geometry("800x500") #Frame(view_frame, bg="white")
            #iew_department_frame.place(x=595, y=320, height=250, width=575)

            scroll_y_e = Scrollbar(view_department_frame, orient=VERTICAL)
            scroll_x_e = Scrollbar(view_department_frame, orient=HORIZONTAL)
            view_department_tree = ttk.Treeview(view_department_frame,columns=("DEPARTMENT ID", "DEPARTMENT NAME", "DEPARTMENT CODE"),xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
            scroll_x_e.pack(side=BOTTOM, fill=X)
            scroll_y_e.pack(side=RIGHT, fill=Y)
            scroll_x_e.config(command=view_department_tree.xview)
            scroll_y_e.config(command=view_department_tree.yview)

            # ==========================TreeView Heading====================
            view_department_tree.heading("DEPARTMENT ID", text="DEPARTMENT ID")
            view_department_tree.heading("DEPARTMENT NAME", text="DEPARTMENT NAME")
            view_department_tree.heading("DEPARTMENT CODE", text="DEPARTMENT CODE")
            view_department_tree["show"] = "headings"

            # ==========================TreeView Column====================
            view_department_tree.column("DEPARTMENT ID", width=50)
            view_department_tree.column("DEPARTMENT NAME", width=150)
            view_department_tree.column("DEPARTMENT CODE", width=100)
            view_department_tree.pack(fill=BOTH, expand=1)

            view_department_information()



        student_view_label = Button(view_frame, text="View Students Information ",borderwidth=0,activebackground="white",relief=FLAT, bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=studentinfo)
        student_view_label.place(x=70, y=60)

        employee_view_label = Button(view_frame, text="View Employees Information ",borderwidth=0,activebackground="white",relief=FLAT, bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=employee_info)
        employee_view_label.place(x=70, y=140)

        department_view_label = Button(view_frame, text="View Department Information ",borderwidth=0,activebackground="white",relief=FLAT, bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=dep_info)
        department_view_label.place(x=70, y=220)

        course_view_label = Button(view_frame, text="View Course Information ",borderwidth=0,activebackground="white",relief=FLAT, bg="white", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),command=course_info)
        course_view_label.place(x=70, y=300)


        #view_student_information()
        #view_employee_information()
        #view_course_information()
        #view_department_information()'''
    
    


    def click_exit():
        """ Allows user to terminates the program when chosen yes"""
        root.deiconify()
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit\n Student Registration Form?")
        if ask is True:
            root.quit()

    def weather1():
        city="chennai Weather"
        city = city.replace(" ", "+")

        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        a=weather+"°C"+"  Chennai"
        concated_text = f" {info} \n {a} "  
        weather_l.configure(text=concated_text, font=("yu gothic ui", 13, "bold"), relief=FLAT, borderwidth=0, background="white", foreground="black")
        weather_l.after(180000, weather1)




    def time_running():
        """ displays the current date and time which is shown at top left corner of admin dashboard"""
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        
        dt=datetime.now()
        time1 = dt.strftime('%H:%M:%S') #time1 = datetime.strftime('%H:%M:%S')#
        date1 = date.today() #date = datetime.strftime('%Y/%m/%d')
        concated_text = f" {time1} \n {date1} " #concated_text = f"  {time} \n {date}"
        date_time.configure(text=concated_text, font=("yu gothic ui", 13, "bold"), relief=FLAT, borderwidth=0, background="white", foreground="black")
        date_time.after(100, time_running)


    
    root = Toplevel()
    root.geometry("1067x600")
    root.title("Dashboard")
    root.resizable(False, False) 
    #root.iconbitmap('images\\logo.ico')
    
    bg = ImageTk.PhotoImage(file="files\Dashboard1.jpg")
    lbl_bg = Label(root,image=bg)
    lbl_bg.image = bg
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    clock_image = ImageTk.PhotoImage(file="Pics/time.png")
    date_time_image = Label(root, image=clock_image, bg="white")
    date_time_image.image = clock_image
    date_time_image.place(x=32, y=50)

    date_time = Label(root)
    date_time.place(x=65, y=40)
    time_running()

    weather_image_r=Image.open("Pics/weather-news.png").resize((25,25),Image.ANTIALIAS)
    weather_image = ImageTk.PhotoImage(weather_image_r)
    weather_l_image = Label(root, image=weather_image, bg="white")
    weather_l_image.image = weather_image
    weather_l_image.place(x=160, y=50)

    weather_l=Label(root)
    weather_l.place(x=200,y=40)
    weather1()


    home_r=Image.open('Pics\\home.png')
    home_r=home_r.resize((50, 50), Image.ANTIALIAS)
    home = ImageTk.PhotoImage(home_r)
    home_button = Button(root, image=home,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2",command=click_home)
    home_button.image = home
    home_button.place(x=40, y=113)


    manage_r=Image.open('Pics\\manage.png')
    manage_r=manage_r.resize((50, 50), Image.ANTIALIAS)
    manage = ImageTk.PhotoImage(manage_r)
    manage_button = Button(root, image=manage,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2",command=click_manage)
    manage_button.image = manage
    manage_button.place(x=38, y=205)

    view_r=Image.open('Pics\\view.png')
    view_r=view_r.resize((50, 50), Image.ANTIALIAS)
    view = ImageTk.PhotoImage(view_r)
    view_button = Button(root, image=view,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2",command=click_view)
    view_button.image = view
    view_button.place(x=36, y=299)

    setting_r = Image.open('Pics\\setting.png')
    setting_r=setting_r.resize((50, 50), Image.ANTIALIAS)
    setting = ImageTk.PhotoImage(setting_r)
    setting_button = Button(root, image=setting,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
    setting_button.image = setting
    setting_button.place(x=38, y=395)

    exit_1_r=Image.open('Pics\\exit_button.png')
    exit_1_r=exit_1_r.resize((50, 50), Image.ANTIALIAS)
    exit_1 = ImageTk.PhotoImage(exit_1_r)
    exit_button = Button(root, image=exit_1,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2",command=click_exit)
    exit_button.image = exit_1
    exit_button.place(x=37, y=490)

    logout = ImageTk.PhotoImage(file='Pics\logout.png')
    logout_button = Button(root, image=logout,font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2",command=click_logout)
    logout_button.image = logout
    logout_button.place(x=940, y=56)



    #root.mainloop()


if __name__=="__main__":
    dashboard()
    