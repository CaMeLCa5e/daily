#! usr/bin/python


filename = "famaFrench.txt"
#
# with open(filename) as myfh:
#     for line in myfh:
#         print line


with open(filename) as myfh:
    listOfLines = myfh.readlines()
    newstring = filename.rstrip()

    # newListOfLines =


for line in open('famaFrench.txt'):
    line = line.rstrip()
    line_words = line.split()
    print line_words[1]

# if value in raw_input() == year:


year = mystr[0:4]
# upperbound is non-inclusive
# filename[4:3:66]

# use is_digit() for processing num in raw_input()




#
#
# print newstring
# print listOfLines
#




__author__ = 'computerlab'
