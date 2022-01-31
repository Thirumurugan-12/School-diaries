import mysql.connector as sql 

def login():
    a=input("Enter the Username ")
    b=input("Enter the Password  ")
    c=input("Enter the Database ")

    spec=sql.connect(host="localhost",user=a,password=b,port=3307,database=c)
    if spec.is_connected():
        print("Database connected Sucessfully")
    spec.close()

def createaccount():
    spec=sql.connect(host="localhost",user="root",port=3307,database="cars")
    mycur=spec.cursor()
    a=input("Enter the Username ")
    b=input("Enter the Password  ")
    mycur.execute(f"create user '{a}'@'localhost' identified by '{b}'")
    spec.commit()
    print("Account Created successfully ")
    print("Your Account Details  ")
    print(f"Username : {a} ")
    print(f"Password: {b} ")
    mycur.close()
    spec.close()

while True:
    print("To login press 1 or To sign up press 2")
    d=int(input()) 
    if d==1:
        login()
    if d==2:
        createaccount()
    

