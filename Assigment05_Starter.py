# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# QKuang,11.06.2019,Created started script
# QKuang,11.06.2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
import os

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

if os.path.exists(objFile):
    openFile = open(objFile, 'r')
    for row in openFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    openFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for Row in lstTable:
            print(Row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task here: ")
        strPriority = input("Enter the task's priority here: ")
        newdicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(newdicRow)
        print('Data was added!')
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Enter a task you want to remove here: ")
        for i in range(len(lstTable)):
            if lstTable[i]['Task'] == strTask:
                del lstTable[i]
                break
        print('Data was deleted!')
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        saveFile = open(objFile, 'w')
        for row in lstTable:
            saveFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        saveFile.close()
        print('Data was saved!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exit the program!')
        break  # and Exit the program
