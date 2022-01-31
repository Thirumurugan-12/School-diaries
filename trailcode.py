



def click_submit(self):
    """

    if there is any value in .txt file, it creates new database named 'cms'
    after then all the required database table are created.

    """

    try:
        le = os.path.getsize("database_data.txt")
        if le == 0:
            obj_connect_db = Model_class.connect_database.ConnectDatabase(host_entry.get(),
                                                                            port_entry.get(),
                                                                            username_entry.get(),
                                                                            password_entry.get())
            db_connection.d_connection(obj_connect_db.get_host(), obj_connect_db.get_port(),
                                            obj_connect_db.get_username(),
                                            obj_connect_db.get_password())
            messagebox.showinfo("Success", "Database Connection Successful")
            store_database()
        else:
            messagebox.showerror("Error", "Database may already connected")

        try:
            obj_create_database = Model_class.connect_database.CreateDatabase('create database cms;')
            db_connection.create(obj_create_database.get_database())
            messagebox.showinfo("Success", "Database \n cms\n created Successfully")
        except:
            obj_create_database = Model_class.connect_database.CreateDatabase('use cms;')
            db_connection.create(obj_create_database.get_database())
            messagebox.showerror("Error", "Database Creation Failed, \nDatabase May already exists!")
            return

        try:
            obj_create_database = Model_class.connect_database.CreateDatabase('use cms;')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table unverified(id int NOT NULL AUTO_INCREMENT, username varchar(256) NOT NULL,email '
                    'varchar(100) NOT NULL , password varchar(254) NOT NULL, PRIMARY KEY (id), UNIQUE KEY (username),'
                    'UNIQUE KEY (email))')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table admin(id int NOT NULL AUTO_INCREMENT, username varchar(256) NOT NULL,email '
                    'varchar(100) NOT NULL , password varchar(254) NOT NULL, PRIMARY KEY (id), UNIQUE KEY (username),'
                    'UNIQUE KEY (email))')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table batch(batch_id int NOT NULL AUTO_INCREMENT, batch_name varchar(50) NOT NULL,'
                    'batch_year varchar(10) NOT NULL, batch_intake varchar(20) NOT NULL,'
                    'PRIMARY KEY (batch_id), UNIQUE KEY (batch_name), reg_date date);')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table course(course_id int NOT NULL AUTO_INCREMENT, course_name varchar(50) NOT NULL,'
                    'course_duration varchar(10) NOT NULL, course_credit varchar(20) NOT NULL, reg_date date,'
                    'PRIMARY KEY (course_id), UNIQUE KEY (course_name));')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table section(section_id int NOT NULL AUTO_INCREMENT, section_code varchar(50) NOT NULL,'
                    'section_name varchar(50) NOT NULL, section_capacity int NOT NULL,'
                    'PRIMARY KEY (section_id), UNIQUE KEY (section_name), reg_date date);')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table department(department_id int NOT NULL AUTO_INCREMENT, department_code varchar(50) '
                    'NOT NULL,'
                    'department_name varchar(50) NOT NULL,'
                    'PRIMARY KEY (department_id), UNIQUE KEY (department_name), reg_date date);')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table students(student_id int NOT NULL AUTO_INCREMENT,'
                    'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                    'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                    'l_name varchar(50), dob varchar(20),gender varchar(10),'
                    'address varchar(30), contact_no int(13) NOT NULL,shift varchar(20) NOT NULL,'
                    'course_enrolled varchar(50) NOT NULL,batch varchar(50) NOT NULL,'
                    'section_enrolled varchar(20) NOT NULL, reg_date date, PRIMARY KEY (student_id),'
                    'FOREIGN KEY (course_enrolled) REFERENCES course (course_name),'
                    'FOREIGN KEY (batch) REFERENCES batch (batch_name),'
                    'CONSTRAINT UC_username UNIQUE (username,email));')
            db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase \
                ('create table employees(employee_id int NOT NULL AUTO_INCREMENT,'
                    'username varchar(254) NOT NULL, email varchar(50) NOT NULL,'
                    'password varchar(254) NOT NULL,f_name varchar(50) NOT NULL,'
                    'l_name varchar(50), dob varchar(20),gender varchar(10),'
                    'address varchar(30), contact_no int(13) NOT NULL,job_type varchar(20) NOT NULL,'
                    'registered_as varchar(50) NOT NULL,qualification varchar(50) NOT NULL,'
                    'department varchar(20) NOT NULL, reg_date date, PRIMARY KEY (employee_id),'
                    'FOREIGN KEY (department) REFERENCES department (department_name),'
                    'CONSTRAINT UC_username UNIQUE (username,email));')
            db_connection.create(obj_create_database.get_database())

            messagebox.showinfo("Success", "All Table are created successfully")

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "Database Table Creation Failed")
            return

        ask = messagebox.askokcancel("Setup Admin", "Please Setup First time Admin Login?\n "
                                                    "It will take just few seconds to get ready")
        if ask is True:
            win = Toplevel()
            Frontend.database_connected.DatabaseConnected(win)
            window.withdraw()
            win.deiconify()

    except BaseException as msg:

        messagebox.showerror("Error", f"Invalid Database Credentials\n {msg}")
        return
