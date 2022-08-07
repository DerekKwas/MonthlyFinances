# Monthly Finances
# By Derek Kwasniewski

import os
from msilib.schema import ListBox
from tkinter import *
from tkinter import messagebox
import PySimpleGUI as GUI

entryDict = {1:2, 3:4, 5:6}
listboxMessages = []

def updateDictNames():
    return

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


# Else create file if payments.txt file exists
else:
    file = open("payments.txt", "w")
    file.close()

# Create GUI object using PySimpleGui Class
GUI.theme("DarkAmber")
layout = [
    [GUI.Listbox(values=listboxMessages, size=(35,22))],
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