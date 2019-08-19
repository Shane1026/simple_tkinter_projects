from tkinter import *

window = Tk()

def kilos_to_pounds():
    pounds=float(e1_value.get())*2.20462
    t1.insert(END, pounds)

b1 = Button(window, text="Convert", command=kilos_to_pounds)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
