# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:03:56 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
from tkinter import *

window = Tk()

def from_kg():
    
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274
    
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END) # Deletes the content of the Text box from start to END
    t1.insert(END, gram) # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

    
#create Kg label
e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)

#entry
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

#button
b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

#three text boxes
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# This makes sure to keep the main window open
window.mainloop()


