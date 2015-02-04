import random

my_dict = {
			"Base-2 number system" : "binary",
			"Number system that uses the characters O-F" : "hexidecimal",
			"7-bit text encoding standard" : "ascii",
			"16-bit text encoding standard" : "unicode", 
			"A number that is bgger than the maximum number that can be stored": "overflow",
			"8 bits" : "byte",
			"1024 bytes" : "kilobyte",
			"Picture Element. The smallest component of a bitmapped image" : "pixel",
			"A continuously changing wave, such as natural sound" : "sample rate",
			"A bunary representation of a program" : "machine code"
}

print ("Computing Quiz")
playing  = True 

while playing == True:
	score = 0

	num = int(input("\nHow many questions would you like?"))

	for i in range(num):
		question = (random.choice( list(my_dict())))
		answer = my_dict[question]

		print("\nQuestion " + str(i+1) )
		print(question + "?")

		guess = input("> ")

		if guess.lower() == answer.lower():
			print("Correct!")
			score += 1
		else:
			print("Nope!")

	print("\nYour final score was" + str(score))

	again = input("Enter any key to play again, or 'q' to quit.")

	if again.lower() == 'q':
		playing = False
		