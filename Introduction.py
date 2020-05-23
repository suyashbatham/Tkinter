import tkinter
print(tkinter.TkVersion)
print(tkinter.TclVersion)
tkinter._test()

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindoes = tkinter.Tk()
mainWindoes.title("Hello Word")
mainWindoes.geometry("200x200+8+400")
mainWindoes.mainloop()



