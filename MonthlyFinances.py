# Monthly Finances
# By Derek Kwasniewski

from cgitb import text
import os
from tkinter import *
from tkinter import messagebox, Tk
import PySimpleGUI as GUI

entriesList = []
selectedIndex = NONE
entriesTotal = 0

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
    [GUI.Text("Monthly Payment:"), GUI.Text(key="-TOTAL-")],
    [GUI.Text("Name"), GUI.InputText(key="-ENTRYNAME-", size=15)],
    [GUI.Text("Cost"), GUI.InputText(key="-ENTRYCOST-", size=16)],
    [GUI.Button("Add"), GUI.Button("Cancel"), GUI.Button("Delete Element")]
]

# Create the window
window = GUI.Window("Window Title", layout, finalize=True)
table = window["-TABLE-"]
total = window["-TOTAL-"]
entryName = window["-ENTRYNAME-"]
entryCost = window["-ENTRYCOST-"]

def updateList(entryName, entryCost):
    entryCost = str(entryCost)
    entriesList.append(entryName + " " + entryCost + "\n")
    file = open("payments.txt", "a")
    file.write(entryName + " " + entryCost + "\n")
    table.update(values=entriesList)  # Lookup on pysimplegui.org the "find_element" function for the Window object (was updated to use a list lookup method)

def deleteEntry(index):
    del entriesList[index]
    table.update(values=entriesList)
    file = open("payments.txt", "w")
    for line in entriesList:
        file.write(line)
    file.close()

def updateTotal():
    global entriesList
    global entriesTotal
    entriesTotal = 0
    if len(entriesList) != 0:
        for line in entriesList:
            list = line.split()
            cost = int(list[1])
            entriesTotal += cost
        total.update(value=entriesTotal)

updateTotal()



# Event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in(GUI.WIN_CLOSED, "Cancel"): # if user closes the window or clicks cancel
        break

    elif event == "Add":
        nameText = values["-ENTRYNAME-"]
        try:
            costText = int(values["-ENTRYCOST-"])
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
            updateTotal()
            entryCost.update(value="")
            entryName.update(value="")

    elif event == "-TABLE-":
        if len(values["-TABLE-"]) > 0: 
            selectedIndex = values["-TABLE-"][0]
            print(selectedIndex)

    elif event == "Delete Element":
        if isinstance(selectedIndex, int):
            deleteEntry(selectedIndex)
            selectedIndex = NONE
            updateTotal()

window.close()