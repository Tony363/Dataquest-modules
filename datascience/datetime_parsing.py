import numpy as np
import pandas as pd
from datetime import datetime


# def combine_date_time(df, datecol, timecol):
#     return pd.to_datetime(df[datecol].dt.date.astype(str)
#                           + ' '
#                           + df[timecol].astype(str))


# def convert_time(timecol):
#     timecol = str(timecol)
#     timecol = timecol[0:len(timecol)-2]

#     if len(timecol) == 1:
#         rv = '00' + ':0' + timecol[0:1]
#     elif len(timecol) == 2:
#         rv = '00' + ':' + timecol[0:2]
#     elif len(timecol) == 3:
#         rv = '0' + timecol[0] + ':' + timecol[1:3]
#     elif len(timecol) == 4:
#         rv = timecol[0:2] + ':' + timecol[2:4]
#     else:
#         print('it is', timecol, 'length', len(timecol))
#         rv = '00:00'
#         #rv = 'N/A'
#     return rv


# def group_hour(ts):

#     if ts.hour < 4:
#         rv = ts.replace(hour=0)
#     elif ts.hour < 8:
#         rv = ts.replace(hour=4)
#     elif ts.hour < 12:
#         rv = ts.replace(hour=8)
#     elif ts.hour < 16:
#         rv = ts.replace(hour=12)
#     elif ts.hour < 20:
#         rv = ts.replace(hour=16)
#     else:
#         rv = ts.replace(hour=20)

#     rv = rv.replace(minute=0, second=0)
#     return rv


def clean_date(date_str):
    return str(date_str.replace(" :", ""))


def four_hour_temp(filename, date):

    fullpath = r"C:\Users\Tony\Downloads\201406hourlySS.txt"
    # fullpath = filepath + filename
    dateCols = ['Date','Time']
    df = pd.read_csv(fullpath, nrows=500, usecols=[1, 2, 12], parse_dates=dateCols)
    #df = pd.read_csv(fullpath, nrows=50000, usecols=[2])

    #print(df.describe())
    df.dropna
    time = df['Time'].apply(lambda x: x.strptime('%H:%M'))
    print(time)

    # df['time'] = df.apply(lambda row: convert_time(row['Time']), axis=1)
    # df['Date_Time'] = pd.to_datetime(
    # df['Date'].apply(str) + ' ' + df['time'].astype(str))
    # df.set_index('Date_Time', inplace=True)
    #df.index = pd.PeriodIndex(df.index, freq='4H')

    # del df['Date']
    # del df['Time']
    # del df['time']
    # df.drop(df.columns[0], axis=1)
    # # print(type(df))

    # df2 = df.asfreq('4H')

    # print('df is', df.head())
    # print(type(df2))
    # print('df2 is', df2.head())
    # #print('df3 is', df3.head())
    return 1


print(four_hour_temp('201406hourlySS.txt', '2014-06-02'))