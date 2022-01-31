from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 

root = Tk()
root.geometry("1000x600")
root.configure(background="black")
root.resizable(False, False) 
root.title("School Diaries")

#background image 
bg = ImageTk.PhotoImage(file="Pics\Sublime Light.jpg")
lbl_bg = Label(root,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

canvas = Canvas(root, bg="black", width=300, height=400,highlightthickness=0)
canvas.pack()
canvas.place(x=650,y=125)

photoimage = ImageTk.PhotoImage(file="Pics\grade1.png")
canvas.create_image(200, 200, image=photoimage)

img1=Image.open("Pics\icons8-user-64.png")
img1=img1.resize((100,100),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img1)
lg_ig=Label(image=photoimage1,borderwidth=0).place(x=650,y=100,width=100, height=100)

root.mainloop()
