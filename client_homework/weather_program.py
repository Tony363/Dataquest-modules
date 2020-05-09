import requests
import json
import ast

def by_city(city,api_key):

    city_call = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(city_call)
    request = r.content
    data = ast.literal_eval(request.decode('utf-8'))
    with open('by_city.json','w') as weather:
        json.dump(r.json(),weather,sort_keys=True, indent=4)

    return f'{city} weather today is {data["weather"][0]["description"]}' 


def by_zip(zip_code,country_code,api_key,):

    
    zip_call = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}'
    r = requests.get(zip_call)
    request = r.content
    data = ast.literal_eval(request.decode('utf-8'))
    with open('by_zip.json','w') as weather:
        json.dump(r.json(),weather,sort_keys=True, indent=4)

    return f'Location with this zip_code,{zip_code}, in the country of {country_code.upper()} has a weather of {data["weather"][0]["description"]}'

def forcast_city(city_name,api_key):

    forcast_call = f'https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city_name},us&&appid=b6907d289e10d714a6e88b30761fae22'
    print(forcast_call)


    r = requests.get(forcast_call)
    request = r.content
    data = ast.literal_eval(request.decode('utf-8'))
    with open('forcast_ciy.json','w') as weather:
        json.dump(r.json(),weather,sort_keys=True, indent=4)

    return data

def forcast_zip(zip_code,api_key):

    forcast_zip = f'https://samples.openweathermap.org/data/2.5/forecast/hourly?zip={zip_code}us&&appid={api_key}'

    r = requests.get(forcast_zip)
    request = r.content
    data = ast.literal_eval(request.decode('utf-8'))
    with open('forcast_zip.json','w') as weather:
        json.dump(r.json(),weather,sort_keys=True, indent=4)

    return data


if __name__ == "__main__":

    api_key = '17b30353debc07c2cea7fcb5f3b0bb89'
    print('Welcome to the weather program!')
    print()

    while True:
        
        contd = str(input('Let\'s continue our query:[y]/n '))
        print()
        if contd.lower() == 'n':
            print('thank you for using our program')
            print()
            break
        elif contd.lower() == 'y':
            pass
        else:
            print('please indicate your decision to use our program')
            print()
            continue

        query = str(input('query by [city],[zip_code],[forcast_city] or [forcast_zipcode]? '))
        print()
    
        if query.lower() == 'city':
            city = str(input('enter city name: '))
            print()
            try:
                print(by_city(city,api_key))
                print()
            except KeyError:
                print('please enter correct city name')
                print()

        elif query.lower() == 'zip_code':
            zip_code = int(input('enter zip code: '))
            print()
            country_code = str(input('enter country code: '))
            print()
            try:
                print(by_zip(zip_code,country_code,api_key))
                print()
            except KeyError:
                print('please enter correct zip_code and country code')
                print()
        elif query.lower() == 'forcast city':
        
            city_name = str(input('please enter city name: '))
           
            try:
                print(forcast_city(city_name,api_key))
                print()
            except KeyError:
                print('please enter a existing city name ')
                print()
        
        elif query.lower() == 'forcast zipcode':
            zip_code = str(input('please enter zip code: '))
            
            try:
                print(forcast_zip(zip_code,api_key))
            except KeyError:
                print('please enter a valid zipcode: ')
                print()

        else:
            print('please query weather by [city] or by [zip_code]')
            print()

