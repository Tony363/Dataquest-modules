## 1. Storing Data ##

content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]
content_rating_numbers = [content_ratings, numbers]

## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_17 = content_ratings['17+']
over_9 = content_ratings['9+']
print(over_9,over_17)

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622


over_12_n_apps = content_ratings['12+']

## 5. Key-Value Pairs ##

d_1 = {
    'key_1': 'first_value', 
    'key_2': 2,
    'key_3': 3.14,
    'key_4': True,
    'key_5': [4,2,1],
    'key_6': {'inner_key' : 6}
      }
if d_1 :
    error = True
else:
    error = False
    

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = ('9+' in content_ratings)
is_in_dictionary_2 = (987 in content_ratings)

# if '17+' in content_ratings:
#     result = "It exists"
#     print(result)
    
result = 'It exists' if '17+' in content_ratings else None
print(result)


## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+':0, '9+':0,'12+':0,'17+':0}
for app in apps_data[1:]:
    c_rating = app[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)

## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for app in apps_data[1:]:
    c_rating = app[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
print(content_ratings)

## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for app in apps_data[1:]:
    genre = app[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for ratings in content_ratings:
    content_ratings[ratings] /= total_number_of_apps
    content_ratings[ratings] *= 100
percentage_17_plus = content_ratings['17+']

import itertools

percentage_15_allowed_dic = dict(itertools.islice(content_ratings.items(), 3))
percentage_15_allowed = sum(percentage_15_allowed_dic.values())
print(percentage_15_allowed)

## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_percentages = {
    ratings:content_ratings[ratings]/ total_number_of_apps * 100 for ratings in content_ratings 
                         }
c_ratings_proportions = {ratings:content_ratings[ratings] / total_number_of_apps for ratings in content_ratings}

# for ratings in content_ratings:
#     proportion = content_ratings[ratings] / total_number_of_apps
#     percentage = proportion * 100
#     c_ratings_percentages[ratings] = percentage
#     c_ratings_proportions[ratings] = proportion


    

## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)



data_sizes = [float(app[2]) for app in apps_data[1:]]
# for app in apps_data[1:]:
#     size = float(app[2])
#     data_sizes.append(size)
min_size = min([float(app[2]) for app in apps_data[1:]])
max_size = max([float(app[2]) for app in apps_data[1:]])

## 13. Filtering for the Intervals ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_count_tot = [int(app[5]) for app in apps_data[1:]]
print(rating_count_tot)

ratings_max = max(rating_count_tot)
ratings_min = min(rating_count_tot)
print(ratings_max, ratings_min)

data_sizes = {'0-10 MB':0,'10 - 50 MB':0,'50 - 100 MB':0,'100 - 500 MB':0, '500+ MB':0}

for app in apps_data[1:]:
    data_size = float(app[5])
    
    
    if data_size <= 10000:
        data_sizes['0-10 MB'] += 1
    elif 10000 < data_size <= 50000:
        data_sizes['10 - 50 MB'] += 1
    elif 50000 < data_size <= 100000:
        data_sizes['50 - 100 MB'] += 1
    elif 100000 < data_size <= 500000:
        data_sizes['100 - 500 MB'] += 1
    elif data_size > 500000:
        data_sizes['500+ MB'] += 1

print(data_sizes)