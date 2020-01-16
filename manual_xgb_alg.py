
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:45:23 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:06:52 2019

@author: x224517
"""

"""
Get examples for XGBoost
"""

import numpy as np
import xgboost as xgb
from yfinance_data import *
from sklearn.model_selection import train_test_split


PARAMETERS = {'max_depth': 2,
              'eta': 0.5,
              'lambda': 1,
              'gamma': 0,
              'min_child_weight': 0,}
# PARAMETERS = {
#     'max_depth': 2,
#     'eta': 2,
#     'verbosity': 1,
# }

def example_1(objective,X,y):
    """
    Simple data
    """

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

    # nc = len(np.unique(y_train))

    parameters = PARAMETERS.copy()
    parameters['objective'] = objective
    # parameters['num_class'] = 3

    # if objective == 'reg:squarederror':
    #     X_train = np.array([[0],
    #                         [1],
    #                         [2]])
    #     y_train = np.array([0, 1, 2])
    #     X_test = np.array([[-1],
    #                        [0],
    #                        [1],
    #                        [2],
    #                        [3]])
    #     y_test = np.array([-1, 0, 1, 2, 3])
        
    # elif objective == 'binary:logistic':
    #     X_train = np.array([[0],
    #                         [1]])
    #     y_train = np.array([0, 1])
    #     X_test = np.array([[0],
    #                        [1],
    #                        [np.nan]])
    #     y_test = np.array([0, 1, 0])
    # elif objective == 'multi:softprob':
    #     X_train = np.array([[0],
    #                         [1],
    #                         [2]])
    #     y_train = np.array([0, 1, 2])
    #     X_test = np.array([[0],
    #                        [1],
    #                        [2],
    #                        [np.nan]])
    #     y_test = np.array([0, 1, 2, 0])
    #     parameters['num_class'] = 3
    # else:
    #     raise ValueError('Not a recognized objective')

    

    data_train = xgb.DMatrix(X_train, y_train)
    data_test = xgb.DMatrix(X_test, y_test)

    bst = xgb.train(params=parameters,
                    dtrain=data_train,)
                    # num_boost_round=3)

    dump = bst.get_dump(with_stats=True)
    for tree in dump:
        print(tree)

    print(bst.predict(data_test))


if __name__ == '__main__':
   example_1('reg:squarederror',X,y)
#    example_1('binary:logistic',X,y)
    # example_1('multi:softprob',X,y)



    # PARAMETERS = {'max_depth': 2,
    #           'eta': 0.5,
    #           'lambda': 1,
    #           'gamma': 0,
    #           'min_child_weight': 0}
    # parameters = PARAMETERS.copy()

    # objective = 'multi:softprob'
    # parameters['objective'] = objective
    # #parameters['objective']='multi:softprob'

    # X_train = np.array([[0],
    #                 [1],
    #                 [2]])
    # y_train = np.array([0, 1, 2])
    # X_test = np.array([[0],
    #                [1],
    #                [2],
    #                [np.nan]])
    # y_test = np.array([0, 1, 2, 0])
    # parameters['num_class'] = 3
    # data_train = xgb.DMatrix(X_train, y_train)
    # data_test = xgb.DMatrix(X_test, y_test)

    # bst = xgb.train(parameters,data_train,3)
#
#    dump = bst.get_dump(with_stats=True)
#    for tree in dump:
#        print(tree)
#
#    print(bst.predict(data_test))

