import sqlite3

dbCon = sqlite3.connect('db/contactsDb')
cur = dbCon.cursor()
contRun = True

def programFlow(runBool):
    while(runBool):
        flowChoice = input("*[view] - View contacts \n*[new] - New contact \n*[q] - Quit \n").lower()
        if(flowChoice == "view"):
            getContacts()
        if(flowChoice == "new"):
            newContact()
        if(flowChoice == "q"):
            exit()
        else:
            print("Unknown command, refer to given list. \n")

def getContacts():
    for row in cur.execute("SELECT * FROM contacts"):
        print(row)

def newContact():
    name = input("Name: ")
    email = input("Email: ")
    phonenum = int(input("Phone number: "))

    cur.execute("INSERT INTO contacts VALUES(?, ?, ?);", (name, email, phonenum))
    dbCon.commit()

#newContact()
#getContacts()

programFlow(contRun)
