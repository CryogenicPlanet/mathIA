import pandas as pd
import matplotlib.pyplot as plt
import statistics 
df  = pd.read_csv("compiledProbabilty.csv")
Probailities = df['Values'][0:57122]
print(Probailities.mean())
print(Probailities.mode())
print(Probailities.median())

l = list(Probailities)
noOfOccurance 
for  x in l:
