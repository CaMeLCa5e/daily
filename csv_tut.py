#! usr/bin/python 

import os
import csv
import random
import string 

os.getcwd()

filename = "import1.txt"
print filename

file_path = os.path.join(os.getcwd(), filename)
print file_path