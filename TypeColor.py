#!/usr/bin/python

import tkinter
import random 

colors = ['Red', 'Blue', 'Green', 'Pink', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0

timeLeft = 30 

def startGame(event):
	if timeLeft == 30:
		countdown()
	nextColor()

def nextColor():
	global score
	global timeLeft

	if timeLeft > 0:
		e.focus_set()

		if e.get().lower() == colors[1].lower():
			score += 1

		e.delete(0, tkinter.END)
		random.shuffle(colors)
		label.config(fg=str(colors[1]), text=str(colors[0]))
		scoreLabel.config(text='Score: '+ str(score))

def countdown():
	global timeLeft

	if timeLeft > 0:
		timeLeft -= 1
		timeLabel.config(text='Time left: ' + str(timeLeft))
		timeLabel.after(1000, countdown)

root = tkinter.Tk()
root.title("Color Countdown")
root.geometry("375x200")

instructions = tkinter.Label(root, text="Type the color of the text", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text=" Time Left" + str(timeLeft), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()











