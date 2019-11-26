## Money change calculator by Michael Lian Gau
# This is one of the 30 days coding challenge.

import os
from tkinter import *

os.system("cls")

entries = []
def calChange():
    if (PayEntry.get() < costEntry.get()):
        noMoney = float(PayEntry.get()) - float(costEntry.get())
        print("Insuffiencient payment, need " +str(round(noMoney, 2)))
        changeLabel.config(text = "Insuffiencient payment, need " + str(round(-noMoney, 2)) + " more.")
    else:
        change = float(PayEntry.get()) - float(costEntry.get())
        print(str(round(change, 2)))
        changeLabel.config(text = "Change: " + str(round(change, 2)))
i = 0
def entry_next(event = None):
    global i
    if(i == 0):
        entries[1].focus_set()
        i = 1
    elif(i == 1):
        calChange()
        i = 0
        entries[0].focus_set()

mainWindow = Tk()
mainWindow.title("Change Calculator")
#
costLabel = Label(mainWindow, text="Item Cost: ")
costLabel.grid(row = 0, column = 0, sticky = W)
costEntry = Entry(mainWindow)
costEntry.grid(row = 0, column = 1)
entries.append(costEntry)
costEntry.focus()

mainWindow.bind("<Return>", entry_next)

PayLabel = Label(mainWindow, text="Customer pay: ")
PayLabel.grid(row = 1, column = 0,  sticky = W)
PayEntry = Entry(mainWindow)
PayEntry.grid(row = 1, column = 1)
entries.append(PayEntry)

ChangeBtn = Button(mainWindow, text="Calculate change", command = calChange)
ChangeBtn.grid(row = 2, column = 0, columnspan = 1)


changeLabel = Label(mainWindow, text="Change: ")
changeLabel.grid(row = 2, column = 1)
#
mainWindow.mainloop()
