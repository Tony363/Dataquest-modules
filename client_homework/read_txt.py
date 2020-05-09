import pandas as pd
import csv

f_read = open("random.txt","r+")  

array = []
for i in f_read.readlines():
    
    i = i.replace('\n','')
    i = i.replace('\\','')
    # i = i.replace(' ','')
    i = i.strip('\\')
    array.append(i)

array = [x for x in array if x != '' and x != '.' ]

print(array)

# print(' '.join(array))

with open('random_formated.txt',"w") as f:
    f.write(' '.join(array))

f_read.close()
