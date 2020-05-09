## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for mo in moma:
    date = mo[6]
    if date != "":
        date = int(date)
        mo[6] = date

## 2. Calculating Artist Ages ##

ages = []
for mo in moma:
    date = mo[6]
    birth = mo[3]
    if isinstance(birth, int):
        age = date - birth
        ages.append(age)
    elif type(birth) is not int:
        age = 0
        ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_age = age
        final_ages.append(final_age)
    elif age <= 20:
        final_age = 'Unknown'
        final_ages.append(final_age)

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
decades = []
for age in final_ages:
    if age == 'Unknown':
        decade = age
        decades.append(decade)
    elif age != 'Unknown':
        decade = str(age)[:-1] + '0s'
        decades.append(decade)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    elif decade in decade_frequency:
        decade_frequency[decade] += 1
        

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
print("{}'s birth year is {}".format(artist,birth_year))

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for mo in moma:
    artist = mo[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    elif artist in artist_freq:
        artist_freq[artist] += 1

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    num_artworks = artist_freq[name]
    return "There are {} artworks by {} in the data set".format(num_artworks, name)

print(artist_summary("Henri Matisse"))
print(artist_freq["Henri Matisse"])

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]


for pop in pop_millions:
    country = pop[0]
    population = pop[1]
    print("The population of {} is {hey:,.2f} million".format(country, hey=population))


## 9. Challenge: Summarizing Artwork Gender Data ##

freq_table = {}
for mo in moma:
    gender = mo[5]
    if gender not in freq_table:
        freq_table[gender] = 1
    elif gender in freq_table:
        freq_table[gender] += 1
for gender in freq_table:
    
        
        
    print("There are {freq:,} artworks by {artists} artists".format(freq=freq_table[gender], artists=gender))