import mysql.connector as sql


spec = sql.connect(host="localhost",user="root",password="root",port="3307")
mycur=spec.cursor(buffered=True)

mycur.execute("show databases;")
print(mycur.fetchall())
#spec.commit()
mycur.execute("use sms;")
mycur.execute("show tables;")
mycur.execute("Select count(*) from employees;")
a=mycur.fetchall()
for i in a:
    print(i)
mycur.close()
spec.close()
