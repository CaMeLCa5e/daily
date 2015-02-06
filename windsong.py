#!/usr/bin/python 
import windsong

print('Binary representation of sound')

print ("Enter the duration of each note")
print ('eg. 200')
rate = int(imput(">"))

print("Enter a 4-bit binary note")
print("Or more than one note separated by spaces")

print("Notes:")
print("0000 = No sound")
print("0001 = Low C")
print("0010 = D")
print("0011 = E")
print("0100 = F")
print("0101 = G")
print("0110 = A")
print("0111 = B")
print("1000 = High C")

soundBinary = input(">")

for note in soundBinary.split():
	if note == "0000":
		freq = 37 
	elif note == "0001":
		freq = 262
	elif note == "0010":
		freq = 294
	elif note == "0011":
		freq = 330
	elif note == "0100"
		freq = 349 
	elif note == "0101"
		freq = 392
	elif note == "0110"
		freq = 440 
	elif note == "0111"
		freq = 494 
	elif note == "1000"
		freq = 523

	windsound.Beep(freq, rate)







