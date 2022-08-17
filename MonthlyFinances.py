# Monthly Finances
# By Derek Kwasniewski

from email import message
import os
from tkinter import *
from tkinter import messagebox, Tk
import PySimpleGUI as GUI

entriesList = []
selectedIndex = NONE
entriesTotal = 0
paymentFreq = ["Daily", "Weekly", "Bi-Weekly", "Monthly", "Bi-Monthly", "Half-Year"]
selectedFreq = "Monthly"
avgDaysInMonth = 30

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
                entriesList.append(f"{list[0]} {list[1]} {list[2]}\n")
# Else create file if payments.txt file exists
else:
    file = open("payments.txt", "w")
    file.close()

# Create GUI object using PySimpleGui Class
GUI.theme("SystemDefault") # See: "https://www.pysimplegui.org/en/latest/readme/#themes" for more themes
layout = [
    [GUI.Table(key="-TABLE-", headings=["Name", "Monthly Cost", "Frequency"], values=entriesList, auto_size_columns=False, col_widths=[10, 10, 12], justification="center", vertical_scroll_only=False, enable_events=True)],
    [GUI.Text("Monthly Payment: $"), GUI.Text(key="-TOTAL-")],
    [GUI.Text("Name"), GUI.InputText(key="-ENTRYNAME-", size=[31,1])],
    [GUI.Text("Cost"), GUI.InputText(key="-ENTRYCOST-", size=[32,1])],
    [GUI.Combo(values=paymentFreq, default_value="Monthly", key="-DROPDOWN-", size=36, enable_events=True)],
    [GUI.Button("Add"), GUI.Button("Delete Element"), GUI.Button("Cancel")]
]

# Create the window
window = GUI.Window("Window Title", layout, finalize=True)
table = window["-TABLE-"]
total = window["-TOTAL-"]
entryName = window["-ENTRYNAME-"]
entryCost = window["-ENTRYCOST-"]

def updateList(entryName, monthlyCost, entryCost):
    # monthlyCost = str(monthlyCost)
    entriesList.append(f"{entryName} ${monthlyCost} ${entryCost}/{selectedFreq}\n")
    file = open("payments.txt", "a")
    file.write(f"{entryName} ${monthlyCost} ${entryCost}/{selectedFreq}\n")
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
            costStr = list[1]
            costStr = costStr.replace("$", "")
            cost = int(costStr)
            entriesTotal += cost
        total.update(value=entriesTotal)
    else:
        total.update(value=0)

def calcMonthlyPayment(Freq, payment):
    monthlyCost = NONE
    if Freq == "Monthly":
        monthlyCost = payment
    elif Freq == "Daily":
        monthlyCost = avgDaysInMonth * payment
    elif Freq == "Weekly":
        monthlyCost = 4 * payment
    elif Freq == "Bi-Weekly":
        monthlyCost = 2 * payment
    elif Freq == "Bi-Monthly":
        monthlyCost = int(.5 * payment)
    elif Freq == "Half-Year":
        monthlyCost = int(payment/6)
    return monthlyCost

updateTotal()



# Event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # If user closes the window or clicks cancel
    if event in(GUI.WIN_CLOSED, "Cancel"): 
        break

    elif event == "Add":
        nameText = values["-ENTRYNAME-"]
        if nameText == "":
            messagebox.showerror("Python Error", "Entry must have a name!")
            continue
        if " " in nameText:
            nameText = nameText.replace(" ", "")
            messagebox.showwarning("Python Message", "No spaces in name, spaces will be removed!")

        costText = values["-ENTRYCOST-"]
        if costText == "":
            messagebox.showerror("Python Error", "Entry must have a cost!")
            continue
        try:
            costText = int(costText)
        except:
            messagebox.showerror("Python Error", "Cost must be an integer!")
            continue
        # print(isinstance(costText, int))
        if isinstance(costText, int):
            costMonthly = calcMonthlyPayment(selectedFreq, costText)
            updateList(nameText, costMonthly, costText)
            updateTotal()
            entryCost.update(value="")
            entryName.update(value="")

    elif event == "-TABLE-":
        if len(values["-TABLE-"]) > 0: 
            selectedIndex = values["-TABLE-"][0]
            # print(selectedIndex)

    elif event == "Delete Element":
        if isinstance(selectedIndex, int):
            deleteEntry(selectedIndex)
            selectedIndex = NONE
            updateTotal()

    elif event == "-DROPDOWN-":
        selectedFreq = values["-DROPDOWN-"]

window.close()