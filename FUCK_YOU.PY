# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
path = r'/home/tony/Downloads/AMEX_20190905.csv'

df = pd.read_csv(path,names=['stock','date','open','high','low','close','volume','dividends'])


# %%
df.head()


# %%
df['stock'].value_counts(normalize=True).sort_values()


# %%
df = df.loc[:10,'stock']
df


# %%
import yfinance as yf

data= []

for i,stock in enumerate(df):
    names = yf.Ticker(stock)
    history = names.history(start='2018-01-01',end='2020-02-01')
    names = pd.DataFrame(history)

    names['PCT_Change_Close'] =  names.Close.rolling(2).apply(lambda x:(x[1]-x[0])/x[0] * 100)
    names['PCT_Change_Low'] = names.Low.rolling(2).apply(lambda x:(x[1]-x[0])/x[0] * 100)
    names['PCT_Change_Open'] = names.Open.rolling(2).apply(lambda x:(x[1]-x[0])/x[0] * 100)
    names['PCT_Change_High'] = names.High.rolling(2).apply(lambda x:(x[1]-x[0])/x[0] * 100)
    names['PCT_Change_Vol'] = names.Volume.rolling(2).apply(lambda x:(x[1]-x[0])/x[0] * 100)
    names['Stock'] = stock
    names.drop(names.index[0],inplace=True)
    names = names.reset_index()
    names = names[['Stock','PCT_Change_Close','PCT_Change_Open','PCT_Change_Low','PCT_Change_High','PCT_Change_Vol','Date']]

    matrix = []
    for i in range(100):
        days = names.PCT_Change_Close.iloc[i:]
        df = pd.DataFrame({f'Days {i}':days.values})
        print(df)
        
        matrix.append(df)
    matrix = pd.concat(matrix,axis=1)
    matrix.insert(loc=0, column='Stock', value=stock)
    data.append(matrix)

#     names = names[['Stock','Date','PCT_Change_Close']]
#     matrix = pd.pivot_table(names,index='Stock',columns='Date',values='PCT_Change_Close')

# pd.options.display.float_format = '${:,.2f}'.format
    


# %%
data[1].head(100)


# %%
list_data = pd.concat(data)

# %% [markdown]
# percent change matrix row index days percent till 100. column day percent of previous days

# %%
list_data.iloc[:100]


# %%
list_data.corr()


# %%
import pandas_profiling as pp
pp.ProfileReport(list_data)


# %%
# import numpy as np


# %%
# array = np.concatenate((list_data.PCT_Change_Close.values[1:], np.array([np.nan])))


# %%
# list_data = list_data.reset_index()


# %%
# Close_array = list_data.PCT_Change_Close


# %%
# type(Close_array)


# %%
# data.corr()


# %%



