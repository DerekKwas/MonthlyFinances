# Monthly Finances
# By Derek Kwasniewski

import os
from tkinter import *
from tkinter import messagebox, Tk
import PySimpleGUI as GUI

entriesList = []
selectedIndex = NONE

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
GUI.theme("SystemDefault") # See: "https://www.pysimplegui.org/en/latest/readme/#themes" for more themes
layout = [
    [GUI.Table(key="-TABLE-", headings=["Name", "Cost"], values=entriesList, enable_events=True)],
    [GUI.Text()],
    [GUI.Text("Name"), GUI.InputText(key="entryName", size=15)],
    [GUI.Text("Cost"), GUI.InputText(key="entryCost", size=16)],
    [GUI.Button("Add"), GUI.Button("Cancel"), GUI.Button("Delete Element")]
]

# Create the window
window = GUI.Window("Window Title", layout, finalize=True)
table = window["-TABLE-"]

def updateList(entryName, entryCost):
    entryCost = str(entryCost)
    entriesList.append(entryName + " " + entryCost + "\n")
    file = open("payments.txt", "a")
    file.write(entryName + " " + entryCost + "\n")
    window["-TABLE-"].update(values=entriesList)  # Lookup on pysimplegui.org the "find_element" function for the Window object (was updated to use a list lookup method)

def deleteEntry(index):
    del entriesList[index]
    window["-TABLE-"].update(values=entriesList)


# Event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in(GUI.WIN_CLOSED, "Cancel"): # if user closes the window or clicks cancel
        break

    elif event == "Add":
        nameText = values["entryName"]
        try:
            costText = int(values["entryCost"])
        except:
            messagebox.showerror("Python Error", "Cost must be an integer!")
            continue
        print(isinstance(costText, int))

        if nameText == "":
            messagebox.showerror("Python Error", "Entry must have a name!")
            continue
        elif costText == "":
            messagebox.showerror("Python Error!", "Entry must have a cost!")
            continue
        else:
            updateList(nameText, costText)

    elif event == "-TABLE-":
        try:
            selectedIndex = values["-TABLE-"][0]
            print(selectedIndex)
        except IndexError:
            print("No such index in values['-Values-']")
        # dataSelected = [entriesList[row] for row in values[event]]
        # print(dataSelected)

    elif event == "Delete Element":
        if isinstance(selectedIndex, int):
            del entriesList[selectedIndex]
            table.update(values=entriesList)
            selectedIndex = NONE

window.close()