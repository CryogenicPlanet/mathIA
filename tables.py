from random import shuffle
import hashlib
from statistics import mean
import pickle
from itertools import product
from string import ascii_uppercase

#example_table = list(range(0,32768))
#shuffle(example_table)
#print(example_table)
#print(len(example_table))
keywords = [''.join(i) for i in product(ascii_uppercase, repeat = 6)]
with open('outfile.txt', 'wb') as fp:
    pickle.dump(keywords, fp)