from statistics import variance
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
textbox = Text(width=5, height=3)
textbox.focus()
textbox.insert(END, "Multi-line")
print(textbox.get("1.0", END))
textbox.pack()

def get_spinbox():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=get_spinbox)
spinbox.pack()

def get_scale(value):
    print(value)

scale = Scale(width=10, from_=0, to=100, command=get_scale)
scale.pack()

def checkbutton_clicked():
    print(check.get())

check=IntVar()
checkbutton = Checkbutton(text="Is it on?", variable=check, command=checkbutton_clicked)
checkbutton.pack()

def radiobutton_clicked():
    print(radio_state.get())

radio_state=IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radiobutton_clicked)
radiobutton2 = Radiobutton(text="Option1", value=2, variable=radio_state, command=radiobutton_clicked)
radiobutton1.pack()
radiobutton2.pack()

def get_listbox(value):
    print(listbox.get(listbox.curselection()))
fruits=["Apple", "Mango"]
listbox = Listbox(width=10, height=5)
for i in range(len(fruits)):
    listbox.insert(i, fruits[i])
listbox.bind("<<ListboxSelect>>", get_listbox)
listbox.pack()

window.mainloop()