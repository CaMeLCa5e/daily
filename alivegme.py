#! usr/bin/python

import tkinter

okToPressReturn = okToPressReturn

hunger = 100
day = 0 

def startGame(event):
	global okToPressReturn
	if okToPressReturn == False
		pass

	else:
		startLabel.config(text = '')
		updateHunger()
		updateDay()
		updateDisplay()

		okToPressReturn = False

def updateDisplay():
	global hunger
	global day 

	if hunger <= 50:
		catPic.config(image = hungryphoto)
	else:
		catPic.config(image = normalphoto)

	hungerLabel.config(text = 'Hunger:' + str(hunger))

	dayLabel.config(tect='day: '+ str(day))

	catPic.after(100, updateDisplay)

def updateHunger():
	global hunger
	hunger -=1

	if  isAlive():
		hungerLabel.after(500, updateHunger)

def updateDay():
	global day
	day += 1

	if isAlive():
		dayLabel.after(5000, updateDay)

def feed():
	global hunger

	if isAlive():
		if isAlive():
			if hunger <= 95:
				hunger += 20
			else:
				hunger -= 20 

def isAlive():
	global hunger

	if hunger <= 0:
		startLabel.config(text="Game Over")
		return False
	else:
		return True 

root = tkinter.Tk()
root.title('Alive')
root.geometry("500x300")

startLabel = tkinter.label(root, text="press start")





















