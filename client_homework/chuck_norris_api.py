import sys
import requests
import json
import pandas as pd

# url = 'https://api.chucknorris.io/jokes/random'

# def prompt_input():
#     url = str(input('Please enter request:'))
#     return url

# def more_jokes():
#     confirmations = str(input('[Y]/n: '))

#     return confirmations

# def get_joke(url):
#     r = requests.get(url)
#     with open('chucky.json','w') as chuck:
#         json.dump(r.json(),chuck,sort_keys=True,indent=4)
#     print(r.json()['value'])

if __name__ == "__main__":

    print('Welcome to Chuck Norris Joke generator')
    print()

    while True:

        another_joke =  str(input('Would you like to see a joke, [Y]/n '))
        print()

        if another_joke.lower() == 'n':
            print('jokes on you')
            print()
            break
        elif another_joke.upper() == 'Y':
            try:
                url = str(input('Please enter API request:'))
                print()
                r = requests.get(url)
            
                with open('chucky.json','w') as chuck:
                    json.dump(r.json(),chuck,sort_keys=True,indent=4)
                print(r.json()['value'])
                print()
            except Exception as e:
                print('please enter correct API request')
                print()
        else:
            print('please answer [Y]/n')
            print()
            

