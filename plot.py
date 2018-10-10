import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("compiledProbabilty.csv")
print(df)
labelrange = [x for x in range(0,456976)]
Probailities = df['Values']
#print(labelrange)
#x =[]
print(len(labelrange))
print(len(Probailities))
print(Probailities)
plt.autoscale(enable=True, axis='x', tight=True)
plt.scatter(labelrange,Probailities, color='r')
plt.xlabel("Possible Inputs(4 Characters)")
plt.ylabel('Probailities')

plt.show()
#df.plot(kind='scatter',x='x',y='y') # scatter plot
#df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram