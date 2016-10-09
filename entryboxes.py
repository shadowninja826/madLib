# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:08:15 2016

@author: Soda.C.
"""



from tkinter import *
from tkinter import messagebox

def displayText():
    """ Display the Entry text value. """

    global entryWidget

    if entryWidget.get().strip() == "":
        messagebox.showerror("Soda's madlibs", "Enter a name")
    else:
        messagebox.showinfo("Soda's madlibs", "Full story should be here =" + entryWidget.get().strip())

if __name__ == "__main__":

    root = Tk()
    root.title("Soda's madlibs")
    root["padx"] = 40
    root["pady"] = 20   
    textFrame = Frame(root)
    entryLabel = Label(textFrame)
    entryLabel["text"] = "Enter a name:"
    entryLabel.pack(side=LEFT)
    entryWidget = Entry(textFrame)
    entryWidget["width"] = 50
    entryWidget.pack(side=LEFT)

    textFrame.pack()

    button = Button(root, text="Submit", command=displayText)
    button.pack()

    root.mainloop()