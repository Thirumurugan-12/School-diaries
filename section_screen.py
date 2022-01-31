from distutils import command
from tkinter import *
from tkinter import ttk
from turtle import up
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
import regist_section


def section_screen():
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
            """it will show all the data contains on the section table of cms database, when clicked by default this method
            is called while initializing the class ManageSection. Exception is handled to avoid run time error which may
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
                query = "select * from section;"
                mycur.execute(query)
                data = mycur.fetchall()
                # print(data)
                section_tree.delete(*section_tree.get_children())
                for values in data:
                    data_list = [values[0], values[1], values[2], values[3], values[4]]
                    # print(data_list)
                    section_tree.insert('', END, values=data_list)

            except BaseException as msg:
                print(msg)


    def click_delete_section():
            """when clicked delete sections, it will require to select the sections and after selecting and
            performing the delete method, it will ask the admin either they are sure they want to delete that section
            or not if yes then section containing that id in section table is deleted."""
            try:
                #obj_section_registration_database = Model_class.section_registration.GetDatabase('use cms;')
                #self.db_connection.create(obj_section_registration_database.get_database())
                a=load_data()
                host=a[0]
                username = a[2]
                password = a[3]
                port=a[1]
                
                spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
                mycur=spec.cursor()

                section_view_content = section_tree.focus()
                section_view_items = section_tree.item(section_view_content)
                section_view_values = section_view_items['values'][0]
                ask = messagebox.askyesno("Warning",
                                        f"Are you sure you want to delete Section having id {section_view_values}")
                if ask is True:
                    query = f"delete from section where section_id={section_view_values};"
                    mycur.execute(query)
                    spec.commit()
                    #self.db_connection.delete(query, (section_view_values,))
                    messagebox.showinfo("Success", f" Section id {section_view_values} deleted Successfully")

                    click_view_all()
                else:
                    print("not deleted")

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                    "There is some error deleting the data\n Make sure you have Selected the data")

    def up_sec():


        def tree_event_handle():
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

                tree_view_content = section_tree.focus()
                tree_view_items = section_tree.item(tree_view_content)
                # print(tree_view_items)
                tree_view_values = tree_view_items['values']
                tree_view_id = tree_view_items['values'][0]
                # print(tree_view_id)
                get_id.clear()
                list_of_tree.clear()
                get_id.append(tree_view_id)
                for i in tree_view_values:
                    list_of_tree.append(i)

                ask = messagebox.askyesno("Confirm",
                                        f"Do you want to Update Student having id {tree_view_id}")
                if ask is True:
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                    "There is some error updating the data\n Make sure you have Selected the data")
        #Frontend.section_registration.Clock(wind)
        
        tree_event_handle()
        a = list_of_tree
        # print(a)

        '''
        if count <= len(txt):
            count = 0
            text = ''
            heading.config(text=text)
        heading.place(x=150, y=0, width=800)'''

        def update():
            """updates the data of section from entry fields"""
            try:
                #obj_section_database = Model_class.section_registration.GetDatabase('use cms;')
                #db_connection.create(obj_section_database.get_database())

                #get_id = get_id
                data_id = get_id[0]
                # print(data_id)
                a=load_data()
                host=a[0]
                username = a[2]
                password = a[3]
                port=a[1]
                
                spec=sql.connect(host=host,user=username,password=password,port=port,database="sms")
                mycur=spec.cursor()
                #obj_section_database = Model_class.section_registration.SectionRegistration(section_code_entry.get(),
                                                                                            #section_name_entry.get(),
                                                                                            #section_capacity_entry.get(),
                                                                                            #reg_date)
                query = f"update section set section_code='{section_code_entry.get()}',section_name='{section_name_entry.get()}', section_capacity='{section_capacity_entry.get()}'" \
                        f" where section_id='{data_id}'"
                mycur.execute(query)
                spec.commit()
                

                #values = (obj_section_database.get_code(), obj_section_database.get_name(),
                            #obj_section_database.get_capacity(), data_id)

                #db_connection.update(query, values)

                ask = messagebox.askyesnocancel("Success", f"Data having \n Section Name={section_name_entry.get()} \n Updated Successfully\n"
                                                            f"Do you want to Go Section Dashboard")
                
                click_view_all()
                if ask is True:
                    pass
                    #win = Toplevel()
                    #Frontend.manage_section.ManageSection(win)
                    #window.withdraw()
                    #win.deiconify()

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error", f"Error due to{msg}")
        
        global section_code_entry,section_name_entry,section_capacity_entry
                                                                                            
        def click_clear_button():
                section_name_entry.delete(0, END)
                section_code_entry.delete(0, END)
                section_capacity_entry.delete(0,END)

        root = Toplevel()
        root.title('SECTION REGISTRATION FORM - COLLEGE MANAGEMENT SYSTEM')
        root.geometry('1067x600')
        root.config(bg="#f29844")

        # ======================Backend connection=============
        #db_connection = Backend.connection.DatabaseConnection()

        reg_frame = Frame(root, bg="#ffffff", width=1000, height=560)
        reg_frame.place(x=30, y=30)



        heading = Label(reg_frame, text="Section Registration Form", font=('yu gothic ui', 30, "bold"), bg="white",
                                fg='black',
                                bd=5,
                                relief=FLAT)
        heading.place(x=200, y=0, width=600)


        section_frame = LabelFrame(reg_frame, text="Section Details", bg="white", fg="#4f4e4d", height=380,
                                        width=800, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        section_frame.config(highlightbackground="red")
        section_frame.place(x=100, y=90)

        # ========================================================================
        # ============================Key Bindings====================================
        # ========================================================================

        #root.bind("<Return>", click_enter_submit)

        # # ========================================================================
        # # ============================Section ID label====================================
        # # ========================================================================

        # ========================================================================
        # ===========================Subject Code ==================================
        # ========================================================================

        section_code_label = Label(section_frame, text="Section Code ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        section_code_label.place(x=160, y=50)

        section_code_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))
        section_code_entry.place(x=405, y=197, width=340)  # trebuchet ms

        section_code_line = Canvas(root, width=340, height=1.5, bg="#bdb9b1", highlightthickness=0)
        section_code_line.place(x=405, y=219)

        # ========================================================================
        # ===========================Section Name==================================
        # ========================================================================

        section_name_label = Label(section_frame, text="Section Name ", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        section_name_label.place(x=160, y=100)

        section_name_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12))
        section_name_entry.place(x=410, y=247, width=335)  # trebuchet ms

        section_name_line = Canvas(root, width=335, height=1.5, bg="#bdb9b1", highlightthickness=0)
        section_name_line.place(x=410, y=269)

        # ========================================================================
        # ===========================Section capacity==================================
        # ========================================================================
        root.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        section_capacity_label = Label(section_frame, text="Section Capacity ", bg="white", fg="#4f4e4d",
                                            font=("yu gothic ui", 13, "bold"))
        section_capacity_label.place(x=160, y=150)

        section_capacity_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui semibold", 12))
        section_capacity_entry.place(x=430, y=297, width=315)  # trebuchet ms

        section_capacity_line = Canvas(root, width=315, height=1.5, bg="#bdb9b1", highlightthickness=0)
        section_capacity_line.place(x=430, y=319)

        reg_date = time.strftime("%Y/%m/%d")



        # ========================================================================
        # ============================Register options=====================================
        # ========================================================================
        submit_img = ImageTk.PhotoImage(file='Pics\\submit.png')
        submit = Button(section_frame, image=submit_img,
                                font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2",command=update)
        submit.image = submit_img
        submit.place(x=90, y=267)


        clear_img = ImageTk.PhotoImage(file='Pics\\clear.png')
        clear_button = Button(section_frame, image=clear_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2",
                                    command=click_clear_button)
        clear_button.image = clear_img
        clear_button.place(x=250, y=270)


        back_img = ImageTk.PhotoImage(file='Pics\\back.png')
        back_button = Button(section_frame, image=back_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        back_button.image = back_img
        back_button.place(x=410, y=270)


        exit_img = ImageTk.PhotoImage(file='Pics\\exit.png')
        exit_button = Button(section_frame, image=exit_img,
                                    font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=exit)
        exit_button.image = exit_img
        exit_button.place(x=570, y=270)

        try:
            section_code_entry.insert(0, a[1])
            section_name_entry.insert(0, a[2])
            section_capacity_entry.insert(0, a[3])
            submit.configure(command=update)
            txt = f" You are updating Section '{a[2]}'"
        except IndexError as msg:
            print(msg)

    list_of_tree = []
    get_id = []

    root = Toplevel()
    root.geometry("1067x600")
    root.title("Section Management Dashboard - College Management System")
    #root.iconbitmap('images\\logo.ico')
    root.resizable(False, False)

    manage_student_frame_r = Image.open('Pics\\student_frame.png').resize((1067,600),Image.ANTIALIAS)
    manage_student_frame = ImageTk.PhotoImage(manage_student_frame_r)
    image_panel = Label(root, image=manage_student_frame)
    image_panel.image = manage_student_frame
    image_panel.pack(fill='both', expand='yes')

    #b_connection = Backend.connection.DatabaseConnection()

    txt = "Section Management Dashboard"
    count = 0
    text = ''
    color = ["#4f4e4d", "#f29844", "#fa3939"]
    heading = Label(root, text=txt, font=('yu gothic ui', 20, "bold"), bg="white",
                            fg='black',
                            bd=5,
                            relief=FLAT)
    heading.place(x=420, y=26, width=640)
    #slider()
    #heading_color()

    # =======================================================================
    # ========================Defining Variables=============================
    # =======================================================================

    #search_by_var = StringVar()
    #sort_by_var = StringVar()
    #sort_in_var = StringVar()
    #sort_date_in_var = StringVar()

    # =======================================================================
    #left frame
    left_view_frame = Frame(root, bg="white")
    left_view_frame.place(x=35, y=89, height=470, width=250)


    #tree view frame
    tree_view_frame = Frame(root, bg="white")
    tree_view_frame.place(x=301, y=90, height=473, width=730)

    # =======================================================================
    # ========================frame for personal credentials =================
    # =======================================================================

    personal_frame = LabelFrame(left_view_frame, text="Section Management Options", bg="white", fg="#4f4e4d",height=460,width=240, borderwidth=2.4,font=("yu gothic ui", 12, "bold"))
    personal_frame.config(highlightbackground="red")
    personal_frame.place(x=5, y=8)

    # ========================================================================
    # ============================Add Subject button===============================
    # ========================================================================
    add_section_r = Image.open("Pics\\add_section.png").resize((225,25),Image.ANTIALIAS)
    add_section = ImageTk.PhotoImage(add_section_r)
    add_section_button = Button(personal_frame, image=add_section, relief=FLAT, borderwidth=0,activebackground="white", bg="white", cursor="hand2",command=regist_section.sec_reg)
    add_section_button.image = add_section
    add_section_button.place(x=5, y=100)
    # add_student_button.place(x=36, y=295)

    # ========================================================================
    # ============================Update subject button===============================
    # ========================================================================

    update_section_r = Image.open('Pics\\update_section.png').resize((225,25),Image.ANTIALIAS)
    update_section = ImageTk.PhotoImage(update_section_r)
    update_section_button = Button(personal_frame, image=update_section, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white", cursor="hand2",command=up_sec
                                        )
    update_section_button.image = update_section
    update_section_button.place(x=5, y=165)
    # update_student_button.place(x=36, y=355)

    # ========================================================================
    # ============================Delete section button===============================
    # ========================================================================

    delete_section_r = Image.open('Pics\\delete_section.png').resize((225,25),Image.ANTIALIAS)
    delete_section = ImageTk.PhotoImage(delete_section_r)
    delete_section_button = Button(personal_frame, image=delete_section, relief=FLAT, borderwidth=0,
                                        activebackground="white", bg="white", cursor="hand2",command=click_delete_section
                                        )
    delete_section_button.image = delete_section
    delete_section_button.place(x=5, y=230)
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

    scroll_x = Scrollbar(tree_view_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(tree_view_frame, orient=VERTICAL)
    section_tree = ttk.Treeview(tree_view_frame,
                                        columns=(
                                            "SECTION ID", "SECTION CODE", "SECTION NAME", "SECTION CAPACITY",
                                            "REGISTRATION DATE"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=section_tree.xview)
    scroll_y.config(command=section_tree.yview)

    # ==========================TreeView Heading====================
    section_tree.heading("SECTION ID", text="SECTION ID")
    section_tree.heading("SECTION CODE", text="SECTION CODE")
    section_tree.heading("SECTION NAME", text="SECTION NAME")
    section_tree.heading("SECTION CAPACITY", text="SECTION CAPACITY")
    section_tree.heading("REGISTRATION DATE", text="REGISTRATION DATE")
    section_tree["show"] = "headings"

    # ==========================TreeView Column====================
    section_tree.column("SECTION ID", width=50)
    section_tree.column("SECTION CODE", width=100)
    section_tree.column("SECTION NAME", width=150)
    section_tree.column("SECTION CAPACITY", width=100)
    section_tree.column("REGISTRATION DATE", width=100)
    section_tree.pack(fill=BOTH, expand=1)

    #section_tree.bind("<Delete>", click_delete_key)
    #section_tree.bind("<Button-3>", do_popup)
    #section_tree.bind("<Double-Button-1>", tree_double_click)
    #section_tree.bind("<Return>", tree_double_click)
    #search_start()
    #search_by.current(0)
    click_view_all()

    #root.mainloop()

if __name__ =="__main__":
    section_screen()