import urllib
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.federalreserve.gov/releases/g19/current/default.htm').read()
soup = BeautifulSoup(url,features="html.parser").find(class_='data-table')#.getText()

matrix = [soup.getText().splitlines()]
List = matrix[0]
matrix = list(filter(None,List))
print(matrix)
# temp_idx = List.index('')
# res = [List[:temp_idx], List[temp_idx + 1:]]
# print(res)

# print(type(soup.getText()))
# df = pd.DataFrame(matrix)

# print(df)
    




    # row = non_revolving.find_all(class_='indent2a sticky sticky-column-cell')

