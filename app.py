#This app allows users to chose certain apps that they can load up on a click of a button

import tkinter as tk #To help create the GUI
from tkinter import filedialog, Text #To chose the files, and display text
import os #Allows us to run the app we are adding to out app

root = tk.Tk() #The root is like the body, it holds the whole app
apps=[] #A list of all the apps that were appeneded

#------------------------
#Functions that control what happens when buttons are pressed
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()  #This deletes all of the prior info that was attached to the label, so we can get a new 

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables", ".app"),("all files","*.*"))) #This gets the file from the directory

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey") #This forloop goes through the app list and adds the text to the frame
        label.pack()


def runApps():
    for app in apps:
        os.system(app) #runs the apps

#------------------------


#------------------------
#Creating a canvas to make it bigger
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack() #To attach the canvas to the root

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #the relwidth and relheight is how big the frame is, the relx and rely is how far from the edges it is
#-------------------------

#--------------------------
#adding buttons
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="black", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="black", bg="#263D42", command=runApps)
runApps.pack()
#--------------------------


root.mainloop() #To get the root to run

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')