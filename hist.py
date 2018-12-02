import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df  = pd.read_csv("compiledProbabilty.csv")
#print(df)
labelrange = [x for x in range(0,1000)]
Probailities = df['Values'][0:1000]
Probailities = Probailities.values.tolist()
dictionary = {'1':labelrange, '2':Probailities}

#print(dictionary)
newdf = pd.DataFrame(data=dictionary)
print(newdf)
plt.hist2d(newdf["1"], newdf["2"])
plt.show()
