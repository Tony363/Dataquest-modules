import statistics
import pandas_datareader as pdr
import xgboost as xgb

# https://www.tutorialspoint.com/How-to-generate-prime-twins-using-Python
def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
    matrix = []
    List = []
    great_50 = []
    less_50 = []
    for i in range(start, end):
        
        j = i + 2
        if(is_prime(i) and is_prime(j)):
            # print("{:d} and {:d}".format(i, j))
            pairs = [i,j]
            matrix.append(pairs)
            List.append(i)
            List.append(j)
    
    sum_100 = sum(List)
    print(sum_100)
    for prime in range(0,len(List),5):
        print(List[prime:prime+5])
    
    for prime in List:
        if prime > 50:
            great_50.append(prime)
    sum_great_50 = sum(great_50)
    print(sum_great_50)
    sum_less_50 = sum([prime for prime in List if prime < 50])
    print(sum_less_50)

    return matrix
    
def difference():
    matrix = generate_twins(0,100)
    # print(list(zip(matrix,matrix)))
    matrix = [y[1] - x[1] for x,y in zip(matrix,matrix[1:])]
    
    # print(matrix)
    return matrix

print(generate_twins(0,100))
print(max(difference()))
# print(generate_twins(0,100))

a = [i for i in range(10)]
b = [i for i in range(10,0,-1)]
print(list(zip(a,b)))
    
    
  
        

        
