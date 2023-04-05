from tkinter import *

window = Tk()
window.minsize(width=1200, height=800)
window.title("My Window")

def button_clicked():
    my_label.configure(text=my_input.get())

my_label = Label(text="New Window")
my_label.pack()
my_input = Entry(width=20)
my_input.pack()
my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

window.mainloop()