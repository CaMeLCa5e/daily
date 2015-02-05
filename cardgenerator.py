#! usr/bin/python

import tkinter
import random

cardNames =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def pickCard():
	cardLabel.configure(text.random.choice(cardNames))

#make gui window 
root = tkinter.Tk()
#set title 
root.title("Random card generator")
#set size
root.geometry("200x100")

nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()

#add button 
pickButton = tkinter.Button(text="Pick!", command=pickCard)
pickButton.pack()

root.mainloop()
