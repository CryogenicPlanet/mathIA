from random import shuffle
import hashlib
from statistics import mean

#example_table = list(range(0, 256))
#shuffle(example_table)
correctHashSha = hashlib.sha256(b"MATH").hexdigest()
correctHash = 186
trueCases = 0
trueForSha = 0
probabilty = []
example_table = [233, 91, 39, 71, 32, 190, 13, 76, 141, 63, 0, 102, 80, 48, 74, 53, 130, 176, 27, 64, 177, 248, 152, 35, 214, 103, 108, 41, 72, 75, 220, 106, 251, 228, 69, 238, 224, 147, 1, 104, 82, 87, 169, 116, 66, 109, 61, 17, 195, 36, 14, 119, 110, 154, 189, 185, 23, 253, 243, 196, 85, 140, 15, 47, 137, 227, 20, 242, 175, 49, 247, 170, 167, 217, 200, 156, 123, 180, 210, 50, 107, 70, 131, 12, 58, 28, 78, 192, 136, 19, 226, 30, 193, 255, 221, 62, 183, 184, 187, 45, 90, 86, 117, 37, 54, 240, 142, 46, 222, 38, 250, 229, 44, 4, 205, 239, 115, 93, 55, 145, 225, 218, 153, 213, 244, 120, 219, 114, 201, 2, 60, 172, 168, 194, 232, 98, 43, 113, 111, 6, 124, 77, 73, 138, 95, 128, 181, 216, 59, 84, 235, 245, 252, 81, 92, 133, 125, 3, 231, 16, 144, 161, 22, 208, 139, 212, 94, 121, 99, 198, 199, 65, 151, 135, 204, 236, 215, 223, 197, 118, 52, 171, 122, 105, 163, 101, 207, 148, 25, 88, 182, 202, 188, 191, 186, 173, 246, 51, 7, 126, 155, 96, 5, 146, 68, 33, 241, 249, 56, 234, 57, 112, 230, 10, 29, 159, 178, 129, 150, 26, 40, 134, 160, 67, 209, 100, 211, 143, 157, 83, 11, 79, 89, 254, 18, 206, 237, 42, 97, 165, 158, 21, 149, 132, 162, 174, 24, 31, 203, 166, 179, 164, 9, 34, 127, 8]
#print(example_table)
def hash8(message, table):
    global trueCases
    hashed = len(message) % 256
    #print("Intial:")
    #print(hashed)
    for i in message:
        #print("Ord:")
        #print(ord(i))
        #print("postion :")
        #print( (hashed+ord(i))%256)
        #print("In loop hashed:")
        hashed = table[(hashed+ord(i)) % 256]
        if hashed == correctHash:
            trueCases = trueCases +1
        #print(hashed)
    return hashed

from itertools import product
from string import ascii_uppercase
#userInput = input("Enter 4 Letter Word : ")

keywords = [''.join(i) for i in product(ascii_uppercase, repeat = 4)]
number = 0
for x in range((6*(len(keywords)))/8,(7*(len(keywords))/8)):
    correctHash = hash8(keywords[x],example_table)
    number = number + 1
    print(number)
    for word in keywords:
        output = hash8(word,example_table)
        #byte = bytes(word,encoding='utf-8')
        #temp = hashlib.sha256(byte).hexdigest()
        #if temp == correctHashSha:
            #trueForSha = trueForSha + 1
    probabilty.append((trueCases/len(keywords)))
    #print(trueCases)
    #print(len(keywords))
    #print(trueForSha)
print(mean(probabilty))
import numpy
a = numpy.asarray(probabilty) 
numpy.savetxt("probabilty.7.csv", a, delimiter=",")