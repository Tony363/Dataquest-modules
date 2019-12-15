import urllib
# import requests
import pandas as pd
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.federalreserve.gov/releases/g19/current/default.htm').read()
soup = BeautifulSoup(url,features="html.parser")
# print(soup)

Consumer_Oustanding = soup.find('table',title='Consumer Credit Outstanding')

table = Consumer_Oustanding.find_all('tr')
# print(table)
for row in table:
    items = row.find_all('td')
    value = items.text
    print(value)
# matrix = [soup.getText().splitlines()]
# List = matrix[0]
# matrix = list(filter(None,List))
# print(matrix)


# print(type(soup.getText()))
# df = pd.DataFrame(matrix)

# print(df)
    




    # row = non_revolving.find_all(class_='indent2a sticky sticky-column-cell')

