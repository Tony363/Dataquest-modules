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

import re

class Movie():
    def __init__(self, title, year, rating=1):
        self.title = title
        self.year = year
        self.rating = rating

    def __repr__(self):
        return """Movie("{}", {}, {})""".format(self.title, self.year, self.rating)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


movies = [
    Movie("Avengers: Endgame", 2019),
    Movie("Star Wars: The Rise of Skywalker", 2019),
    Movie('Code Geass: R2', 2006),
    Movie('Code Geass: Lelouch of Rebellion', 2006),
    Movie('Eureka Seven', 2002),
    Movie('Gundam Seed', 2002),
    Movie('Evangelion Neogensis', 2005),
    Movie('Gundam Seed Destiny', 2005)
]

def get_movie_catalog_by_year(movie_list):
    movie_dictionary = {} # key is year, value is a list of movie tuples
    for movie in movie_list:
        current_year_movies = movie_dictionary.get(movie.year, [])
        
        current_year_movies.append(movie)

        movie_dictionary[movie.year] = current_year_movies

    return movie_dictionary


print(get_movie_catalog_by_year(movies))
# print(movies[0])

# movies = []
# for row in csvReader.getline():
#     m = Movie(row[0], row[1], row[2])
#     movies.append(m)


values = [i for i in range(7)]
# print(values)
movie_names = ['wtf','why am i doing this','just to kill time','and torture myself','hell', 'no', 'fuck']
years = ['200{}'.format(i) for i in range(7)]
# print(year)

high_ratings = {key:[movie for i,movie in enumerate(movie_names) if i == key  ] for key in values if key > 3 }
low_ratings = {key:[movie for i,movie in enumerate(movie_names) if i == key ] for key in values if key <= 3 }
years_dict = {year: [(movie,value) for movie,value in zip (movie_names, values) ] for year in years}

lists = [{'movies':[high_ratings,low_ratings,years]}]



print(lists)

temp = dict(zip(movie_names, values))
# print(list(temp.values()))
# print(temp.items())

# for tem in temp.items():
#     if tem[1] <= 3:
#         low_ratings[tem[0]] = tem[1]
#     elif tem[1] > 3:
#         high_ratings[tem[0]] = tem[1]
# print(low_ratings)
# print(high_ratings)
# print(lists)

# mydic = {key:[] for key in movie_names}
# print(mydic)

#### 1 if A else 2 if B else 3

def myexpr(A, B):
    if A:
        return 1
    else:
        if B:
            return 2
        else:
            return 3

#[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2)]
nested_ternary_loop = [(i, j, k) for i in range(1) for j in range(2) for k in range(3)]

'''
+-----------------------------------------------------------------------------------+
|                                    Problem:                                       |
+-----------------------------------------------------------------------------------+
| Convert a                                                                         |
| nested if-else block into                                                         |
| a single line of code by using Pythons ternary expression.                        |
| In simple terms convert:                                                          |
|                                                                                   |
|      1.f_nested_if_else(*args) (  which uses                                      |
|      ````````````````````        nested if-else's)                                |
|            |                                                                      |
|            +--->to its equivalent---+                                             |
|                                     |                                             |
|                                     V                                             |
|                              2.f_nested_ternary(*args) (     which uses           |
|                              ```````````````````       nested ternary expression) |
+-----------------------------------------------------------------------------------+
'''
'''
Note:
C:Conditions  (C, C1, C2)
E:Expressions (E11, E12, E21, E22)
Let all Conditions, Expressions be some mathematical function of args passed to the function
'''    

#-----------------------------------------------------------------------------------+
#| 1. |      Using nested if-else                                                   |
#-----------------------------------------------------------------------------------+
def f_nested_if_else(*args):
    if(C):
        if(C1):
            return E11
        else:
            return E12
    else:
        if(C2):
            return E21
        else:
            return E22

#-----------------------------------------------------------------------------------+
#| 2. |      Using nested ternary expression                                        |
#-----------------------------------------------------------------------------------+
def f_nested_ternary(*args):
    return ( (E11) if(C1)else (E12) )   if(C)else   ( (E21) if(CF)else (E22) )


#-----------------------------------------------------------------------------------+
#-----------------------------------------------------------------------------------|
#-----------------------------------------------------------------------------------|
#-----------------------------------------------------------------------------------|
#-----------------------------------------------------------------------------------+

#     +-----------------------------------------------------------------------------+
#     |                               Visualization:                                |
#     +-----------------------------------------------------------------------------+
#     |         Visualize the ternary expression like a binary tree :               |
#     |           -Starting from the root and  moving down to the leaves.           |
#     |           -All the internal nodes being conditions.                         |
#     |           -All the leaves being expressions.                                |
#     +-----------------------------------------------------------------------------+
#                                      _________________
#                                      |f_nested_ternary|                                 
#                                      ``````````````````
#             ( (E11) if(C1)else (E12) )   if(C)else   ( (E21) if(C2)else (E22) )
#                 |       |        |          |            |       |        |
#                 |       |        |          |            |       |        |
#                 V       V        V          V            V       V        V                                                                             
# Level-1|                  +----------------(C)-----------------+         
# --------             True/          __________________           \False         
#                         V           |f_nested_if_else|            V              
# Level-2|          +----(C1)----+    ``````````````````     +----(C2)----+     
# --------     True/              \False                True/              \False
#                 V                V                       V                V     
# Level-3|    ( (E11)            (E12) )               ( (E21)            (E22) ) 

# def array_count9(nums):
#     count = 0
#     for i in nums:
#         if i == 9:
#             count += 1
#     return count

def array_count9(nums):
    return sum(1 if num == 9 else 0 for num in nums)

print(array_count9([i for i in range(999)]))

# def take_string(string):
#     return False if (ord(char) > 127) else True for char in string

def take_string(string):
    count = 0
    for char in string:
        if ord(char) > 127:
            count += 1 
    if count > 3:
        return False
    else:
        return True
        
print(take_string('Instagram'),take_string('爱奇艺PPS -《欢乐颂2》电视剧热播'),take_string('Docs To Go™ Free Office Suite'),take_string('Instachat 😜'))

# ["A" if b=="e" else "d" if True else "x" for b in "comprehension"]
# ['d', 'd', 'd', 'd', 'd', 'A', 'd', 'A', 'd', 'd', 'd', 'd', 'd']

##https://stackoverflow.com/questions/2951701/is-it-possible-to-use-else-in-a-list-comprehension