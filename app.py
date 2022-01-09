from tkinter import *
from tkinter import ttk

wordList = []

gui = Tk()
frm = ttk.Frame(gui, padding=10)

frm.grid()

ttk.Entry(frm).grid(column=1, row=1)

ttk.Label(frm, text="Welcome to Ordstjernesolver!").grid(column=0, row=0)

ttk.Label(frm, text="Enter ALL letters that the word is allowed to consist of including the special letter: ", anchor='w').grid(column=0, row=1)
ttk.Entry(frm).grid(column=1, row=1)

ttk.Label(frm, text="Enter the letter that all characters must consist of (the special letter): ", anchor='w').grid(column=0, row=2)
ttk.Entry(frm).grid(column=1, row=2)

ttk.Button(frm, text="Give me the words").grid(column=0, row=4)
ttk.Button(frm, text="Quit", command=gui.destroy).grid(column=0, row=5)

gui.mainloop()