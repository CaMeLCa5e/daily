import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

names = ['bob', 'jessica', 'mary', 'john', 'mel']
births = [687, 144, 77, 578, 973]

BabyDataSet = zip(names,births)
print BabyDataSet

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print df

df.dtypes
df.Births.dtypes

print df.dtypes

Sorted = df.sort(['Births'], ascending=False)
Sorted.head(1)

df['Births'].max()




# df.to_csv('births1880.csv', index=False,header=False)