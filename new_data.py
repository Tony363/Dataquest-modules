import random
import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def baby_data():
    """
    Returns
    -------
    X : fiddled features.
    y : fiddled labels.

    """
    X = [i for i in range(100)]
    y = [i + random.random()*5-2.5 for i in X]
    z = [i**2 for i in X]
    df = {'X':X,'Z':z,'y':y}
    df = pd.DataFrame(df)

    X = df[['X','Z']]
    y = df.y
    return X,y

def mock_data():
    X_mock = range(50,60)
    Z_mock = range(50,60)
    Y_mock = range(50,60)
    
    array = pd.DataFrame({'X':X_mock,'Z':Z_mock,'Y':Y_mock})
    x_mock = array[['X','Z']]
    y_mock = array['Y']
    return x_mock,y_mock

def MVND(pred_leaf):
    """ 
    Parameters
    ----------
    pred_leaf : Enter prediction with pred_leaf = True.
    
    Returns
    -------
    matrix : Multivariate Normal Distribution Matrix

    """
    tree_pandas = []
    tree_numpy = []
    for column in range(max([len(x) for x in pred_leaf])):
        tree = []
        for row in pred_leaf[:,column]:
            lst = [0] * pred_leaf[:,column].max()
            try:
                lst[row-1] = 1
                tree.append(lst)
            except IndexError:
                pass
        stats = np.asarray(tree)
        tree_numpy.append(stats)
        df = pd.DataFrame(tree)
        df.columns = [f'T{column+1}L{i+1}' for i in df.columns]
        df = df.loc[:, (df != 0).any(axis=0)]
        # df.reset_index(inplace=True)
        tree_pandas.append(df)
    
    matrix = pd.concat(tree_pandas,axis=1)
    
    print(matrix)
    return matrix

def scatter_plot(y_test,pred_test):
    """
    Parameters
    ----------
    y_test : validation set.
    pred_test : prediction on test.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.scatter(y_test,pred_test, color='b')
    #ax.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'k--',lw=4)
    ax.set_xlabel('preds')
    ax.set_ylabel('y_test')
    ax.set_title('scatter plot')
    plt.show()

# params
params = {
    'max_depth':5,
    'min_child_weight': 3,
    'eta':.1,
    'subsample': .8,
    'colsample_bytree': .8,
    'nthread':-1,
    'objective':'reg:squarederror',
    'eval_metric':'rmse',
}


"""
predict on baby data
"""

X,y = baby_data() # load features and labels

# shuffling
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
# deciding on Dmatrices
dtrain = xgb.DMatrix(X_train,label=y_train,nthread=-1)
dtest = xgb.DMatrix(X_test, label=y_test,nthread=-1)
    
# training
bst = xgb.train(
        params=params,
        dtrain=dtrain,
        num_boost_round=999,
        evals=[(dtest,'test')],
        early_stopping_rounds=10
    )

pred_leaf = bst.predict(dtrain,pred_leaf=True)# with leaves
pred_train = bst.predict(dtrain)# predict on train
pred_test = bst.predict(dtest)# predict on testoad fucked up data to DMatrix



baby_MVND = MVND(pred_leaf)# show multivariate normal distribution matrix

scatter_plot(y_train,pred_train)# scatter plot

bst.save_model('baby_model.model')# save the trained model from baby data

print(pred_train)
print(pred_test)

"""
predict on mock data
"""

loaded_model = xgb.Booster()
loaded_model.load_model('baby_model.model')# load baby model

x_mock,y_mock = mock_data()# load fucked up data

# manual training and validation set engineering because train test split shuffling causes different 
# results every time
X_mocktrain = x_mock.loc[:round(x_mock.shape[0]*0.8)]
y_mocktrain = y_mock.loc[:round(y_mock.shape[0]*0.8)]
X_mocktest = x_mock.loc[round(x_mock.shape[0]*0.8):]
y_mocktest = y_mock.loc[round(y_mock.shape[0]*0.8):]


dmock_train = xgb.DMatrix(X_mocktrain,label=y_mocktrain,nthread=-1)# load train mock DMatrix
dmock_test = xgb.DMatrix(X_mocktest,label=y_mocktest,nthread=-1)# load test mock DMatrix

mock = loaded_model.predict(dmock_train,pred_leaf=True)# with leaves

mock_predtest = loaded_model.predict(dmock_test) # on test
mock_predtrain = loaded_model.predict(dmock_train)# on train

print(mock_predtest)
print(mock_predtrain)

mock_MVND = MVND(mock)# multivariate normal distribution matrix on mock train data
scatter_plot(y_mocktrain,mock_predtrain) # plotting on mock train and 

