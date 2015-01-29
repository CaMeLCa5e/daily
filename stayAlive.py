#! usr/bin/python 

#StayAlive

#import mods for GUI
import tkinter

okToPressReturn = okToPressReturn

#player attributes
hunger = 100
day = 0 

def startGame(event):

	global okToPressReturn

	if okToPressReturn == False 
		pass

	else:
		#update time 
		startLabel.config(text = "")

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

	#update time left label
	hungerLabel.config(text = 'Hunger:' + str(hunger))

	#update time 
	dayLabel.config(tect='day: ' + str(day))

	#run the function after 100 ms
	catPic.after(100, updateDisplay)

def updateHunger():

	global hunger

	hunger -= 1

	if isAlive():
		#run function again after 500 ms
		hungerLabel.after(500, updateHunger)

def updateDay():
	global day 
	#decrement the hunger
	day += 1

	if isAlive():
		#run fun after 5 sec
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

		startLabel.config(text="Game over. you killed it!")
		return False
	else:
		return True 

#create a GUI window
root = tkinter.Tk()
root.title('Stay Alive!')
root.geometry("500x300")

startLabel = tkinter.Label(root, text="Press return to start", font=('Helvetica', 12))
startLabel.pack()

dayLabel = tkinter.Label(root, text="Hunger: " +str(hunger), font('Helvetica', 12))
dayLabel.pack()

hungryphoto = tkinter.PhotoImage(file="hungry.gif")
normalphoto = tkinter.PhotoImage(file="normal.gif")

catPic = tkinter.Label(root, image=normalphoto)
catPic.pack()

btnFeed.pack()

#run the start game when return is pressed. 
root.bind('<Return>', startGame)

#start GUI
root.mainloop()




















