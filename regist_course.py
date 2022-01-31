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

def course_reg():
    def load_data():
        f=open("Credentials.csv","r")
        s=csv.reader(f,delimiter="-")
        d=[]
        for i in s:
            d.append(i)
        a=d[::-1]
        return (a[0])


    def click_submit():
        """initialize when click submit button, which will take data from entry box
        and insert those data into student table after successful validation of those data"""
        try:
            #obj_course_database = Model_class.course_registration.GetDatabase('use cms;')
            #self.db_connection.create(obj_course_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()
            #obj_course_database = Model_class.course_registration.CourseRegistration(self.course_name_entry.get(),
                                                                                        #self.course_duration_entry.get(),
                                                                                        #self.course_credit_entry.get(),
                                                                                        #self.reg_date)

            cn=course_name_entry.get()   
            cd=course_duration_entry.get()        
            cc=course_credit_entry.get()   

            query = f"insert into course (course_name,course_duration,course_credit,reg_date) values ('{cn}','{cd}','{cc}','{reg_date}');"
            mycur.execute(query)
            spec.commit()
            
            mycur.execute("select * from course;")
            value = mycur.fetchall()
            print(value)
            # print(values)
            #self.db_connection.insert(query, values)
            # print(values)
            messagebox.showinfo("Success", f"Data inserted Successfully\n Course name={course_name_entry.get()}")
            course_screen.click_view_all()
            
        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", f"There is some error Submitting Credentials")

    def validation():
        """this will validate if the course code and name of entry fields are already in database table named
        course or not if return True, error message is thrown displaying course code/name already exists"""
        name_list = []
        
        try:
            #obj_course_database = Model_class.course_registration.GetDatabase('use cms;')
            #self.db_connection.create(obj_course_database.get_database())
            a=load_data()
            host=a[0]
            username = a[2]
            password = a[3]
            port=a[1]
            
            spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
            mycur=spec.cursor()
            query = "select * from course;"
            mycur.execute(query)
            spec.commit()
            data = mycur.fetchall()
            
            # print(data)

            name_list = []
            for values in data:
                name_data_list = values[1]
                name_list.append(name_data_list)
        
        except BaseException as msg:
            print(msg)

        if course_name_entry.get() == "" or course_duration_entry.get() == "" or \
                course_credit_entry.get() == "" :
            messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")

        elif course_name_entry.get() in name_list:
            messagebox.showerror("Already Exists", f"{course_name_entry.get()} Course Already Exists")

        else:
            click_submit()



    root = Toplevel()
    root.title('COURSE REGISTRATION FORM - COLLEGE MANAGEMENT SYSTEM')
    root.geometry('1067x600')
    root.config(bg="#f29844")
    #root.iconbitmap('images\\logo.ico')
    root.resizable(False, False)
    #manage_student_frame = ImageTk.PhotoImage(file='Pics\\student_frame.png')


    # ======================Variables======================

    reg_frame = Frame(root, bg="#ffffff", width=1000, height=560)
    reg_frame.place(x=30, y=30)

    heading = Label(reg_frame, text="Course Registration Form", font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=200, y=0, width=600)


    course_frame = LabelFrame(reg_frame, text="Course Details", bg="white", fg="#4f4e4d", height=380,
                                    width=800, borderwidth=2.4,
                                    font=("yu gothic ui", 13, "bold"))
    course_frame.config(highlightbackground="red")
    course_frame.place(x=100, y=90)




    course_name_label = Label(course_frame, text="Course Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    course_name_label.place(x=160, y=65)

    course_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
    course_name_entry.place(x=410, y=212, width=335)  # trebuchet ms

    course_name_line = Canvas(root, width=335, height=1.5, bg="#bdb9b1", highlightthickness=0)
    course_name_line.place(x=410, y=234)

    # ========================================================================
    # ===========================Course Duration==================================
    # ========================================================================

    course_duration_label = Label(course_frame, text="Course Duration ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
    course_duration_label.place(x=160, y=115)

    course_duration_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))
    course_duration_entry.place(x=430, y=262, width=315)  # trebuchet ms

    course_duration_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
    course_duration_line.place(x=430, y=284)

    # ========================================================================
    # ===========================Course Credit==================================
    # ========================================================================

    course_credit_label = Label(course_frame, text="Course Credit ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
    course_credit_label.place(x=160, y=165)

    course_credit_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))
    course_credit_entry.place(x=410, y=312, width=335)  # trebuchet ms

    course_credit_line = Canvas(root, width=335, height=1.5, bg="#bdb9b1", highlightthickness=0)
    course_credit_line.place(x=410, y=334)

    reg_date = time.strftime("%Y/%m/%d")

    # ========================================================================
    # ============================Register options=====================================
    # ========================================================================
    submit_img = ImageTk.PhotoImage(file='Pics\submit.png')

    submit = Button(course_frame, image=submit_img,
                            font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                            , borderwidth=0, background="white", cursor="hand2",command=validation)
    submit.image = submit_img
    submit.place(x=90, y=267)

    clear_img = ImageTk.PhotoImage(file='Pics\\clear.png')
    clear_button = Button(course_frame, image=clear_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2"
                                )
    clear_button.image = clear_img
    clear_button.place(x=250, y=270)

    back_img = ImageTk.PhotoImage (file='Pics\\back.png')
    back_button = Button(course_frame, image=back_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    back_button.image = back_img
    back_button.place(x=410, y=270)

    exit_img = ImageTk.PhotoImage(file='Pics\\exit.png')
    exit_button = Button(course_frame, image=exit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2", command=exit)
    exit_button.image = exit_img
    exit_button.place(x=570, y=270)


    #root.mainloop()


if __name__=="__main__":
    course_reg()