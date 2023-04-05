from tkinter import *

window = Tk()
window.minsize(width=1200, height=800)
window.configure(padx=12, pady=8)

label = Label(text="Label")
label.grid(column=1, row=1)


def button_clicked():
    print("Hello, I am a button")


button = Button(text="Button", command=button_clicked)
button.grid(column=2, row=2)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=3, row=1)

entry=Entry()
entry.insert(END, "Input")
entry.grid(column=4, row=3)

window.mainloop()
