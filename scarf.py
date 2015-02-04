#! usr/bin/python 

#make a scarf with different designs.  

#Variable 1 
colors = ['#zzxxzzx', '|fffOOgO']

#Var 2
color_length = 1

#var 3
pattern_length = 25

#var 4
pattern_width = 10

print ('Here is your scarf: \n')
for pos in range(int(pattern_width * pattern_length)):
	print( colors[int((pos)/color_length) % len(colors)])
	if (pos % pattern_width) == pattern_width-1:
		print("")