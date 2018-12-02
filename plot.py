import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df  = pd.read_csv("compiledProbabilty.csv")
#print(df)
labelrange = [x for x in range(0,1000)]
Probailities = df['Values'][0:1000]
#print(labelrange)
#x =[]
print(len(labelrange))
#print(len(Probailities))
print(Probailities)
newdf = pd.DataFrame(labelrange,Probailities)#
plt.autoscale(enable=True, axis='x', tight=True)
#plt.scatter(labelrange,Probailities, color='r')
#plt.xlabel("Possible Inputs(4 Characters)")
#plt.ylabel('Probailities')
#g = sns.jointplot(x=labelrange, y=Probailities, data=newdf, kind="kde");
#g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
#g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$X$", "$Y$");
#sns.distplot(Probailities)
plt.hist(df['Values'][0:57123], color = 'blue', edgecolor = 'black', bins = 57123)
plt.show()
#df.plot(kind='scatter',x='x',y='y') # scatter plot
#df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram
