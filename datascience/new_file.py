### Some hardcoding string parsing
import networkx as nx
from networkx.algorithms.components import strongly_connected_components

x = 'Tony is ,'
new_string = []
for char in x:
    if char == ',':
        char = ''
        new_string.append(char)
    else:
        new_string.append(char)

new_line = ''.join(new_string)

print(new_line)

array = [1,2,3,4,5,6,7,5,3,2,45,2]
print(set(array))


        
    
x = [['Goodday' for j in range(8)] for i in range(8)]
print(x)
x = [['Badday' for j in range(8)] for i in range(8)]
y = []
for row in x:
#     print(row)
    for word in row:
        word = 'Badday'
        # print(word)
print(x)

