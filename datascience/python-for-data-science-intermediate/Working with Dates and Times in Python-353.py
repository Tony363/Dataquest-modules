## 1. Introduction ##

from csv import reader

opened_file = open('potus_visitors_2015.csv')
read_file = csv.reader(opened_file)
potus = list(read_file)
potus = potus[1:]


## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911,6,16)
man_on_moon = dt.datetime(1969,7,20,20,17)
random_time = dt.datetime.now()
print(random_time)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
import csv
import datetime as dt

opened = open("potus_visitors_2015.csv")
read = csv.reader(opened)
list_potus = list(read)
potus_header = list_potus[0]
potus = list_potus[1:]
print(potus_header)  

date_format = "%m/%d/%y %H:%M"

for po in potus:
    start_date = po[2]
    formated = dt.datetime.strptime(start_date, date_format)
    po[2] = formated
    print(po[2])

## 6. Using Strftime to format dates ##

import datetime as dt

visitors_per_month = {}

for po in potus:
    start_date = po[2]
    formated = dt.datetime.strftime(start_date, "%B, %Y")
    if formated not in visitors_per_month:
        visitors_per_month[formated] = 1
    else:
        visitors_per_month[formated] += 1

## 7. The Time Class ##

import datetime as dt

appt_times = []

for po in potus:
    start_time = po[2]
    time = dt.datetime.time(start_time)
    appt_times.append(time)
# print(appt_times

time_now = dt.datetime.now()
print(time_now)
print(time_now.time())

## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##

import datetime as dt
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths = {}

for po in potus:
    start_date = po[2]
    end_date = po[3]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)
print(appt_lengths)