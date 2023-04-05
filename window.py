import tkinter
from turtle import position

window = tkinter.Tk()

window.title("My First Application")
window.minsize(height=500, width=300)
my_label = tkinter.Label(text="My first label")
my_label.pack(anchor="center", expand=True)

window.mainloop()
