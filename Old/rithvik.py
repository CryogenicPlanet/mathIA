import itertools

pairs = list(itertools.product([1,2,3,4,5,6], repeat=2))

spaces_moved = range(2,37)
dictionary = {}

for elem in spaces_moved:
    dictionary[elem] = 0
jail = []
sum = 0
sum2 = 0
sum3 = 0
for elem in pairs:
    sum = elem[0] + elem[1]
    if elem[0] != elem[1]:
        dictionary[sum] += 1
    else:
        #print("SUM1:")
        #print(sum)
        for x in pairs:
            sum2 = x[0] + x[1] + sum
            
            if x[0] != x[1]:
                dictionary[sum2] += 1

            else:
                
                #print("SUM1 + SUM2:")
                for y in pairs:
                    sum3 = y[0] + y[1] + sum2
                    #print(sum3)
                    
                    if y[0] != y[1]:

                        dictionary[sum3] += 1

                    else:
                        jail.append(1)
print(dictionary)
print(jail)