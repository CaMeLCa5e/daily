import pandas as pd 
from numpy import random 
import matplotlib.pyplot as plt 
import sys 

# %matplotlib inline

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range (1000)]

print random_names[:10]

births = [random.randint(low=0,high=1000) for i in range(1000)]
print births[:10]

births = [687, 144, 77, 578, 973]

BabyDataSet = zip(names,births)

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print df[:10]

# Create an excel file
d = {'Channel':[1], 'Number':[255]}
df = pd.DataFrame(d)
print df

