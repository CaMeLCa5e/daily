#!/usr/bin/env python 
"""Example code note"""


def read_file(file_name):
	f = open(file_name)
	data = f.read()
	f.close()
	return data


def split_lyrics(x):
	lyric_count = {}
	lyrics_list = x.split(" ")

	for word in lyrics_list:
		if word in lyric_count:
			lyric_count[word] +=1 
		else:
			lyric_count[word] = 1
	return lyric_count	

if __name__ == '__main__':
	lyrics = read_file("input1.txt")
	lyrics_dictionary = split_lyrics(lyrics)
# 	print lyrics_dictionary
	sorted_lyrics = sorted([(value,key) for (key,value) in lyrics_dictionary.items()])
	sorted_lyrics.reverse()
	print sorted_lyrics[0:100]
	