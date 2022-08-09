# Monthly Finances
# By Derek Kwasniewski

import os
from tkinter import *
from tkinter import messagebox
import PySimpleGUI as GUI
import tkinter

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
                entriesList.append(list[0] + " " + list[1] + "\n")
# Else create file if payments.txt file exists
else:
    file = open("payments.txt", "w")
    file.close()

# Create GUI object using PySimpleGui Class
GUI.theme("DarkAmber")
layout = [
    [GUI.Listbox(key="-LISTBOX-", values=entriesList, size=(20, 10))],
    [GUI.Text("Name"), GUI.InputText(key="entryName", size=15)],
    [GUI.Text("Cost"), GUI.InputText(key="entryCost", size=16)],
    [GUI.Button("Ok"), GUI.Button("Cancel"), GUI.Button("Delete Element")]
]

# Create the window
window = GUI.Window("Window Title", layout, finalize=True)
listbox = window["-LISTBOX-"]
widget = listbox.widget

listbox.bind("<Button-1>", "", propagate=False)
window.refresh()
x0, y0, dx, dy = widget.bbox(GUI.tk.END)
y_limit = y0 + dy

def updateList(entryName, entryCost):
    entriesList.append(entryName + " " + entryCost + "\n")
    file = open("payments.txt", "a")
    file.write(entryName + " " + entryCost + "\n")
    window["-LISTBOX-"].update(values=entriesList)  # Lookup on pysimplegui.org the "find_element" function for the Window object (was updated to use a list lookup method)


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
        elif costText == "":
            messagebox.showerror("Python Error!", "Null Cost!")
        else:
            updateList(nameText, costText)

    elif event == "-LISTBOX-":
        y = listbox.user_bind_event.y
        if y  < y_limit:
            index = widget.nearest(y)
            listbox.update(set_to_index=index)
        selectedElementIndex = window["-LISTBOX-"].get_indexes() # Get listbox element index as a list
        print(selectedElementIndex)
        # try:
            # selectedElementIndex = selectedElementIndex[0] # Get the first index of list (The selected element index)
        # except IndexError:
            # continue
        # del entriesList[selectedElementIndex]
        # window["-LISTBOX-"].update(values=entriesList)

    # elif event == "Delete Element":




window.close()