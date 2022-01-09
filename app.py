from tkinter import *
from tkinter import ttk
from ordstjerneSolver import ordstjerne_solver

wordList = []

def generate_list():
    all_letters = entry_all_letters.get()
    special_letter = entry_special_letter.get()
    
    if (all_letters == "" or special_letter == ""):
        result_string.set("Make sure that both fields are not empty!")
        return

    if(len(special_letter) > 1):
        result_string.set("The special character can only be one character!")
        return

    if(special_letter not in all_letters):
        result_string.set("Make sure that the special letter is a part of all the letters!")
        return

    all_letters = list(all_letters)

    result = str(ordstjerne_solver(all_letters, special_letter))

    if (result == []):
        result_string.set("No words found!")
        return
    
    result_string.set(result)
    return 

gui = Tk()
frm = ttk.Frame(gui, padding=10)

frm.grid()

# Will hold the result
result_string = StringVar()
label_result = ttk.Label(frm, textvariable=result_string)
label_result.grid(column=0, row=3)

ttk.Entry(frm).grid(column=1, row=1)

ttk.Label(frm, text="Welcome to Ordstjernesolver!").grid(column=0, row=0)

ttk.Label(frm, text="Enter ALL letters that the word is allowed to consist of including the special letter: ", anchor='w').grid(column=0, row=1)
entry_all_letters = ttk.Entry(frm)
entry_all_letters.grid(column=1, row=1)

ttk.Label(frm, text="Enter the letter that all characters must consist of (the special letter): ", anchor='w').grid(column=0, row=2)
entry_special_letter = ttk.Entry(frm)
entry_special_letter.grid(column=1, row=2)

ttk.Button(frm, text="Give me the words", command=generate_list).grid(column=0, row=4)
ttk.Button(frm, text="Quit", command=gui.destroy).grid(column=0, row=5)

gui.mainloop()