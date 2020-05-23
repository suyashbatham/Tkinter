try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindoes = tkinter.Tk()
mainWindoes.title("Hello Word")
mainWindoes.geometry("200x200+8+400")
label = tkinter.Label(mainWindoes,text="hello world")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindoes)
leftFrame.pack(side='left',anchor='n',fill=tkinter.Y,expand=False)
canvas = tkinter.Canvas(leftFrame,relief='raised',borderwidth=1)
# canvas.pack(side='left',fill=tkinter.Y,expand=True) # fill = tkinter.X
# canvas.pack(side='top',fill=tkinter.Y,expand=True)
canvas.pack(side='top')
button1 = tkinter.Button(mainWindoes,text="heloo")
button2 = tkinter.Button(mainWindoes,text="hii")
button3 = tkinter.Button(mainWindoes,text="Byy")
button1.pack(side='top',anchor='w')
button2.pack(side='top',anchor='n')
button3.pack(side='top',anchor='e')
mainWindoes.mainloop()
