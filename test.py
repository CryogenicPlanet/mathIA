import pickle
itemlist = []
with open ('outfile.txt', 'rb') as fp:
    itemlist = pickle.load(fp)
print(itemlist)
print(len(itemlist))