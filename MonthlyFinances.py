# Monthly Finances
# By Derek Kwasniewski

import time
import os
from msilib.schema import ListBox
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
import PySimpleGUI as GUI

# def add_to_list():
    # if entryName.get() == '':
        # messagebox.showerror("Python Error", "Entry must have a name!")
    # if not entryPay.get().isnumeric():
        # messagebox.showerror("Python Error", "Entry payment must be a number!")
    # else:
        # listBox.insert(END, (entryName.get() + " " + entryPay.get()))
        # file = open("payments.txt", "a") # "a" is to append whereas "w" opens file for writing which clears the file 
        # file.write(entryName.get() + " " + entryPay.get() + "\n")
        # file.close()
        # entryName.delete(0, END)
        # entryPay.delete(0, END)


# def remove_from_list():
    # listBox.delete(listBox.curselection())

# ---------------------------------------------------------------------------------------------------------------------------------------------------

entriesList = []

if os.path.exists('payments.txt'):
    file = open("payments.txt", "r")
    fileString = file.readlines()
    file.close()
    if fileString != '':
        for line in fileString:
            if line == '':
                break
            else:
                list = line.split()
                entriesList.append(list[0] + " " + list[1])
# Else create file if payments.txt file exists
else:
    file = open("payments.txt", "w")
    file.close()

def updateDictNames():
    return

# Create GUI object using PySimpleGui Class
GUI.theme("DarkAmber")
layout = [
    [GUI.Listbox(values=entriesList, size=(35,22))],
    [GUI.Text("Enter Payment Name"), GUI.InputText(key="entryName"), GUI.InputText(key="entryCost")],
    [GUI.Button("Ok", ), GUI.Button("Cancel")]
]

# Create the window
window = GUI.Window("Window Title", layout)


# Event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in(GUI.WIN_CLOSED, "Cancel"): # if user closes the window or clicks cancel
        break
    elif event == "Ok":
        nameText = values["entryName"]
        costText = values["entryCost"]
        if nameText == "":
            messagebox.showerror("Python Error", "Null Name!")
        else:
            try:
                name = str(nameText)
            except:
                messagebox.showerror("Python Error", "Not a String!")
        if costText == "":
            messagebox.showerror("Python Error", "Null Cost!")

        else:
            try:
                cost = int(costText)
            except:
                messagebox.showerror("Python Error", "Not an Integer!")



window.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Create main window and set its name
#root = Tk()
#root.title("Finances List")

# Create the main frame with grid
#mainFrame = ttk.Frame(root, padding="3 3 12 12")
#mainFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))
#root.columnconfigure(0, weight = 1)
#root.rowconfigure(0, weight = 1)

#listBox = tkinter.Listbox(root)
#listBox.grid(column=1, columnspan=2, row=1, sticky=(W,E))
#if os.path.exists('payments.txt'):
    #file = open("payments.txt", "r")
    #fileString = file.readlines()
    #file.close()
    #if fileString != '':
        #for line in fileString:
            #if line == '':
                #break   
            #else:
                #list = line.split()
                #listBox.insert(END, (list[0] + " " + list[1] + "\n"))

# Else create file if payments.txt file exists
#else:
    #file = open("payments.txt", "w")
    #file.close()

#entryName = tkinter.Entry(root)
#entryName.grid(column=1, row=2, sticky=(W,E))

#entryPay = tkinter.Entry(root)
#entryPay.grid(column=2, row=2, sticky=(W,E))

#button = tkinter.Button(root, text="Add Entry", command = add_to_list)
#button.grid(column=1, row=3, sticky=(W,E))

#button2 = tkinter.Button(root, text="Remove Selected", command = remove_from_list)
#button2.grid(column=2, row=3, sticky=(W,E))

#root.mainloop() # Used to show that this is the end of Python execition and nothing after this will be executed