## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)
# avg_rating_free = mean(free_apps_ratings)
# avg_rating_free = float(numpy.mean(free_apps_ratings))

## 2. Booleans ##

a_price = 0

if a_price == 0:
    print('This is free')
elif a_price == 1:
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price > 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price== 0.0:
        free_apps_ratings.append(rating)
    
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)




## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []
for apps in apps_data[1:]:
    rating = float(apps[7])
    genre = apps[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

average_rating_gaming_apps = 3.69
# if average_rating_gaming_apps > avg_rating_non_games:
print(average_rating_gaming_apps > avg_rating_non_games)
print(average_rating_gaming_apps < avg_rating_non_games)    



## 5. Multiple Conditions ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

## 6. The or Operator ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price > 0:
        free_games_social_ratings.append(rating)
        
avg_non_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Non-free apps (average)

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

price_greater_9 = []
price_less_9 = []
for apps in apps_data[1:]:
    rating = float(apps[7])
    price = float(apps[4])
    if price > 9:
        price_greater_9.append(rating)
    else:
        price_less_9.append(rating)
n_apps_less_9 = len(price_less_9)
n_apps_more_9 = len(price_greater_9)
avg_rating = sum(price_greater_9)/len(price_greater_9)


## 9. The else Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_data[0].append("free_or_not")
for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    elif price > 0.0:
        app.append('non-free')

for app in apps_data[0:6]:
    print(app)

## 10. The elif Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_data[0].append('price_label')
for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    elif price > 0.0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    else:
        app.append('very expensive')
print(apps_data[:7])
