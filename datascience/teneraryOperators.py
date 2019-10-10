## Lists
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = ('9+' in content_ratings)
is_in_dictionary_2 = (987 in content_ratings)

# if '17+' in content_ratings:
#     result = "It exists"
#     print(result)

# is_in_dictionary_3 = ('17+' in content_ratings)    
# print(is_in_dictionary_3)
results = 'It exits' if '17+' in content_ratings else None
print('It exists' if '17+' in content_ratings else None)

## Dictionaries
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

stats = {'a':1000, 'b':3000, 'c': 100}
inverse = [(value, key) for key, value in stats.items()]
print( max(inverse)[1])

def functionOne(para, paraa, parab):
    arguments = locals()
    print(arguments)
    for keys in arguments:
        arguments[keys] = str(arguments[keys]).lower()
        print (arguments[keys])
    # para = para.lower()
    # paraa = paraa.lower()
    # parab = parab.lower()
    # print (locals())

functionOne('HP', 'MA', 'aM')

T = (10,20,30,40,50)
for var in T:
   print (var)

values = [0,1,2,3,4,5,6]
movie_names = ['wtf','why am i doing this','just to kill time','and torture myself','hell', 'no', 'fuck']
year = ['200{}'.format(i) for i in range(8)]
# print(year)

high_ratings = {}
low_ratings = {}
years = {}

lists = [{'movies':[high_ratings,low_ratings,years]}]

# print(lists)

temp = dict(zip(movie_names, values))
# print(list(temp.values()))
print(temp.items())

for tem in temp.items():
    if tem[1] <= 3:
        low_ratings[tem[0]] = tem[1]
    elif tem[1] > 3:
        high_ratings[tem[0]] = tem[1]
print(low_ratings)
print(high_ratings)
print(lists)


