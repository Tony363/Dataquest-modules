### Some hardcoding string parsing

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

        
    
