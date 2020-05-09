import urllib
# import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.federalreserve.gov/releases/g19/current/default.htm').read()
soup = BeautifulSoup(url,features="html.parser")
# print(soup)

Consumer_Oustanding = soup.find('table',title='Consumer Credit Outstanding')

table = Consumer_Oustanding.find('tbody')
# print(table)
row = table.find_all('tr')
# print(row)
matrix = []
for tr in row:
    # List = []
    text = str(tr.getText())
    value = text.split('\n')
    value = [i for i in value if i != '']
    
    
    matrix.append(value)
print(matrix) 
   
# matrix = [soup.getText().splitlines()]
# List = matrix[0]
# matrix = list(filter(None,List))
# print(matrix)


# print(type(soup.getText()))
df = pd.DataFrame(matrix)
df.set_index(0)


print(df.head())
    






