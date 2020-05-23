# from tkinter import *
# top = Tk()
# top.mainloop()


                     # pack method
# from tkinter import *
# top = Tk()
# redbutton = Button(top,text="Red",fg="red")
# redbutton.pack(side=LEFT)
# blackbutton = Button(top,text="Black",fg="black")
# blackbutton.pack(side=RIGHT)
# orangebutton = Button(top,text="Orange",fg="orange")
# orangebutton.pack(side=TOP)
# greenbutton = Button(top,text="Green",fg="green")
# greenbutton.pack(side=BOTTOM)
# top.mainloop()

                  # Grid Method
# from tkinter import *
# top = Tk()
# name = Label(top,text="Name").grid(row=0,column=0)
# e1 = Entry(top).grid(row=0,column=1)
# password = Label(top,text="Password").grid(row=1,column=0)
# e2 = Entry(top).grid(row=1,column=1)
# submit = Button(top,text="Submit").grid(row=4,column=0)
# top.mainloop()

                 # Place Method
# from tkinter import *
# top = Tk()
# top.geometry("200x200")
# name = Label(top,text="Name").place(x=30,y=50)
# email = Label(top,text="Email").place(x=30,y=90)
# password = Label(top,text="Password").place(x=30,y=130)
# submit = Button(top,text="Submit").place(x=30,y=160)
# e1 = Entry(top).place(x=80,y=50)
# e2 = Entry(top).place(x=80,y=90)
# e3 = Entry(top).place(x=95,y=130)
# top.mainloop()