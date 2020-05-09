import numpy as np
import random
import pandas as pd
df = pd.DataFrame({'stringA':[i for i in range(100)], 'stringB':[i for i in range(100)], 'num':[i for i in range(100)]})
list1 = [random.randrange(1,10) for i in range(10)]
list2 = [random.randrange(1,10) for i in range(100)]
# list3 = [ i  if i == j else j for i,j in zip(list1,list2) ]
# print(list3)
list4 = [i if i == x else x for i,x in zip(df.stringA,list1)]
print(list4)
print(df)
