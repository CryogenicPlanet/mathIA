import pandas as pd
import matplotlib.pyplot as plt
import statistics 
df  = pd.read_csv("compiledProbabilty.csv")
Probailities = df['Values']
print(Probailities.mean())
print(Probailities.mode())
print(Probailities.median())

