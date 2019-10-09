## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]

def max(a_list):
    return "No max value returned"

print(max(a_list))

max_val_test_0 = max(a_list)
print(max_val_test_0)
del(max)


## 3. Default Arguments ##

# INITIAL CODE
from collections import Counter
def open_dataset(file_name):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset('AppleStore.csv')
dic = [app[:3] for app in apps_data[1:]]
print(dic)

## 4. The Official Python Documentation ##

one_decimal = round(3.43, 1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2223227, 5)