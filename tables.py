from random import shuffle
import hashlib
from statistics import mean
import pickle


example_table = list(range(0,32768))
shuffle(example_table)
print(example_table)
print(len(example_table))
with open('outfile.txt', 'wb') as fp:
    pickle.dump(example_table, fp)