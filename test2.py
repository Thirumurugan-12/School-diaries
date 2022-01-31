import csv

def load_data():
    f=open("Credentials.csv","r")
    s=csv.reader(f,delimiter="-")
    d=[]
    for i in s:
        d.append(i)
    a=d[::-1]
    return (a[0])
    #return lis[0]


load_data()