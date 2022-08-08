# Monthly Finances
# By Derek Kwasniewski

from email import message
import os
from msilib.schema import ListBox
from tkinter import *
from tkinter import messagebox
import PySimpleGUI as GUI

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
    [GUI.Listbox(key="GUIList", values=entriesList, size=(0, 10), expand_x=True, )],
    [GUI.Text("Enter Payment Name"), GUI.InputText(key="entryName"), GUI.InputText(key="entryCost")],
    [GUI.Button("Ok", ), GUI.Button("Cancel")]
]


# Create the window
window = GUI.Window("Window Title", layout)

def updateList(entryName, entryCost):
    entriesList.append(entryName + " " + entryCost + "\n")
    file = open("payments.txt", "a")
    file.write(entryName + " " + entryCost + "\n")
    window["GUIList"].Update(values=entriesList)  # Lookup on pysimplegui.org the "find_element" function for the Window object (was updated to use a list lookup method)

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



window.close()