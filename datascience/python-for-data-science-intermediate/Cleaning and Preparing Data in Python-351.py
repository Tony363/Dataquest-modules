## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows = len(moma)
print(num_rows)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
moma = list(read_file)

# remove the first row of the data, which
# contains the column names
moma = moma[1:]

# Write your code here
print(moma)


## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('one','two')
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
# print(moma)
for mo in moma:
    nationality = mo[2].replace('(','').replace(')','')
    mo[2] = nationality
    gender = mo[5].replace('(','').replace(')','')
    mo[5] = gender
print(moma)
    

## 5. String Capitalization ##

for mo in moma:
    Gender = mo[5].title()
    
    if Gender == '':
        Gender = 'Gender Unknown/Other'
    mo[5] = Gender
    Nationality = mo[2].title()
    
    if Nationality == '':
        Nationality = 'Nationality Unknown'
    mo[2] = Nationality

# print(list(mo[5] for mo in moma))
print(list(mo[2] for mo in moma))

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for mo in moma:
    BeginDate, EndDate = mo[3],mo[4]
    mo[3], mo[4] =  clean_and_convert(BeginDate), clean_and_convert(EndDate) 
print(moma)

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    return string.replace('(','').replace(')','').replace('c','').replace('C','').replace('.','').replace('s','').replace("'",'').replace(' ','')

stripped_test_data = []

for string in test_data:
    cleaned = strip_characters(string)
    stripped_test_data.append(cleaned)
print(stripped_test_data)
    

## 8. Parsing Numbers from Complex Strings, Part Two ##

import statistics

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def process_date(string):
    if '-' in string:
        value = [int(i) for i in string.split('-')]
        return round(statistics.mean(value))
    else:
        return int(string)
        
        
        
    
    
processed_test_data = []

for data in stripped_test_data:
    processed = process_date(data)
    processed_test_data.append(processed)
print(processed_test_data)

for mo in moma:
    Date = mo[6]
    cleaned = strip_characters(Date)
    processed = process_date(cleaned)
    mo[6] = processed
# print(list(mo[6] for mo in moma))
    