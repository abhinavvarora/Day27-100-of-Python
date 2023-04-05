from tkinter import *

window = Tk();
window.title("Mile to Kilometer conversion") 
window.minsize(width=1200, height=800)

entry = Entry(width=30)
entry.grid(column= 2, row=1)
entry.insert(END, "0")

text1 = Label(text="Miles")
text1.grid(column=3, row=1)

text2 = Label(text="is equal to")
text1.grid(column=1, row=2)

kilometer = Label(text="0")
kilometer.grid(column=2, row=2)

text3 = Label(text="Kilometers")
text3.grid(column=3, row=2)

def button_clicked():
    value = float(entry.get())
    kilometer.configure(text=f"{value*1.609}")

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=2, row=3)

window.mainloop()