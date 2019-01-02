import pickle
ten = []
with open ('ten.txt', 'rb') as fp:
    ten = pickle.load(fp)
correctHash = 186
trueCases  = 0
def hash8(message, table,mod):
    global trueCases
    hashed = len(message) % mod
    #print("Intial:")
    #print(hashed)
    for i in message:
        #print("Ord:")
        #print(ord(i))
        #print("postion :")
        #print( (hashed+ord(i))%256)
        #print("In loop hashed:")
        hashed = table[(hashed+ord(i)) % mod]
        if hashed == correctHash:
            trueCases = trueCases +1
        #print(hashed)
    return hashed
from itertools import product
from string import ascii_uppercase
#userInput = input("Enter 4 Letter Word : ")
keySet = []
for i in range(3,6):
    keywords = [''.join(i) for i in product(ascii_uppercase, repeat = i)]
    keySet.append(keywords)
#print(len(keywords))
testWords = ["BAT","MATH","MATHS","CHANCE"]
number = 0
for i in range(3):
    print("Word : ")
    word = testWords[i]
    print(word)
    correctHash = hash8(word,ten,len(ten))
    keywords = keySet[i]
    
    trueCases = 0
    for word in keywords:
        output = hash8(word,ten,1024)
        #byte = bytes(word,encoding='utf-8')
        #temp = hashlib.sha256(byte).hexdigest()
        #if temp == correctHashSha:
            #trueForSha = trueForSha + 1
    #print(trueCases)
    #print(len(keywords))
    #print(trueForSha)
    print(trueCases)
    print(" ------- ")    