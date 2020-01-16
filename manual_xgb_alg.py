
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xgboost as xgb
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import style
 
#####GOTTA FIGURE OUT HOW TO USE n_estimators
style.use('ggplot')

def example_1(objective,X,y):
    """
    Simple data
    """

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

    # nc = len(np.unique(y_train))

    parameters = PARAMETERS.copy()
    parameters['objective'] = objective
    # parameters['num_class'] = 3
    #print(len(y_test))
    #print(len(y_train))

    
    data_train = xgb.DMatrix(X_train, y_train)
    data_test = xgb.DMatrix(X_test, y_test)

    bst = xgb.train(params=parameters,
                    dtrain=data_train,)
                    # num_boost_round=3)

    dump = bst.get_dump(with_stats=True)
    for tree in dump:
        print(tree)
    pred = bst.predict(data_test)
    pred = pd.DataFrame(pred)
    pred['y_test'] = y_test
    print(pred)
    
    #pred[0].plot()
    #pred['y_test'].plot()
   # plt.xlabel('preds')
    #plt.ylabel('y_test')
    #plt.show()
  
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    #ax.scatter(pred[0], color='r')
    ax.scatter(pred[0] ,pred['y_test'], color='b')
    ax.set_xlabel('preds')
    ax.set_ylabel('y_test')
    ax.set_title('scatter plot')
    plt.show()
    


PARAMETERS = {'max_depth': 2,
              'eta': 0.5,
              'lambda': 1,
              'gamma': 0,
              'min_child_weight': 0,}


path = r'C:\Users\Tony\Downloads\TONY_AMEX_20190905.csv'

df = pd.read_csv(path,names=['stock','date','open','high','low','close','volume','dividends'])


df['stock'].value_counts(normalize=True).sort_values()

df = df.loc[:10,'stock']

data = []

for i,stock in enumerate(df):
    names = yf.Ticker(stock)
    history = names.history(start='2010-01-01',end='2020-02-01')
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
        #print(df)
        
        matrix.append(df)
    matrix = pd.concat(matrix,axis=1)
    matrix.insert(loc=0, column='Stock', value=stock)
    data.append(matrix)
    
stock = data[0]
#print(stock)

stock.drop(stock.index[-99:],inplace=True)

X = np.array(stock.loc[:,'Days 1':])
y = np.array(stock['Days 0'])


example_1('reg:squarederror',X,y)




