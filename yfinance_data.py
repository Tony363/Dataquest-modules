
import pandas as pd
import yfinance as yf
import numpy as np 
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBRegressor


path = r'/home/tony/Downloads/AMEX_20190905.csv'

df = pd.read_csv(path,names=['stock','date','open','high','low','close','volume','dividends'])

df['stock'].value_counts(normalize=True).sort_values()

df = df.loc[:10,'stock']



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
#         days = names.PCT_Change_Close.iloc[i:]
        days = names.PCT_Change_Close.shift(-i)
        df = pd.DataFrame({f'Days {i}':days.values})
        # print(df)
        
        matrix.append(df)
    matrix = pd.concat(matrix,axis=1)
    matrix.insert(loc=0, column='Stock', value=stock)
    data.append(matrix)

stock_0 = data[0]
stock_0.drop(stock_0.index[-99:],inplace=True)
# print(stock_0)
# print(stock_0.loc[:,'Days 1':])
# print(stock_0['Days 0'])

X = np.array(stock_0.loc[:,'Days 1':])
y = np.array(stock_0['Days 0'])



X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state = 2)

classifier = xgb.sklearn.XGBRegressor(max_depth=2,reg_lambda=1,gamma=0,min_child_weight=0)

   

classifier.fit(X_train,y_train)

predictions = classifier.predict(X_test)

accuracy = classifier.score(X_test,y_test)

print(f"accuracy is : {accuracy}")








