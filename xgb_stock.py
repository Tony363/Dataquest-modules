import warnings
import shap
import pickle
import pandas as pd
import yfinance as yf
import numpy as np 
import matplotlib.pyplot as plt
import xgboost as xgb
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, StratifiedKFold
from datetime import datetime
from sklearn.metrics import roc_auc_score, mean_squared_error
from xgboost.sklearn import XGBRegressor
from sklearn.metrics import mean_squared_error


path = r'/home/tony/Downloads/AMEX_20190905.csv'

df = pd.read_csv(path,names=['stock','date','open','high','low','close','volume','dividends'])

df.head()

df = df.loc[:4,'stock']

data = []

for i,stock in enumerate(df):
    names = yf.Ticker(stock)
    history = names.history(start='2002-02-01',end='2020-02-25')
    names = pd.DataFrame(history)

    # names['PCT_Change_Close'] =  names.Close.pct_change()
    # names['PCT_Change_Low'] = names.Low.pct_change()
    # names['PCT_Change_Open'] = names.Open.pct_change()
    # names['PCT_Change_High'] = names.High.pct_change()
    # names['PCT_Change_Vol'] = names.Volume.pct_change()
    names['Stock'] = stock
   
    names.drop(names.index[0],inplace=True)
    names = names.reset_index()
   
    # names = names[['Stock','PCT_Change_Close','PCT_Change_Open','PCT_Change_Low','PCT_Change_High','PCT_Change_Vol','Date']]

    matrix = []
    for i in range(30):

        # days = names.PCT_Change_Close.shift(i)
        days = names.Close.shift(-i)
        df = pd.DataFrame({f'Days_{i}':days.values})       
        matrix.append(df)
    matrix = pd.concat(matrix,axis=1)
    matrix.insert(loc=0, column='Date',value=names.Date)
    data.append(matrix)

stock = data[3]

stock.drop(stock.index[:30],inplace=True)
stock.set_index('Date',inplace=True)
data = pd.concat(data)

warnings.filterwarnings('ignore')

X = stock.loc[:,'Days_1':]
y = stock['Days_0']


def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))


PARAMETERS={
    'max_depth':6,
    'min_child_weight': 1,
    'eta':.3,
    'subsample': 1,
    'colsample_bytree': 1,
    'nthread':-1,
 'objective':'reg:squarederror',
 'eval_metric':'rmse'}

param_grid = {
    'n_estimators': [400, 700, 1000],
    'colsample_bytree': [0.7, 0.8],
    'max_depth': [15,20,25],
    'reg_alpha': [1.1, 1.2, 1.3],
    'reg_lambda': [1.1, 1.2, 1.3],
    'subsample': [0.7, 0.8, 0.9],
    
}

# manual feature training by 80%
X_train = stock.iloc[:round(stock.shape[0]*.8),1:29]
y_train = stock.iloc[:round(stock.shape[0]*.8),0]

X_test = stock.iloc[round(stock.shape[0]*.8):,1:29]
y_test = stock.iloc[round(stock.shape[0]*.8):,0]

data_train = xgb.DMatrix(X_train, y_train,nthread=-1)
data_test = xgb.DMatrix(X_test, y_test,nthread=-1)



bst = xgb.train(params=PARAMETERS,
                dtrain=data_train,
                num_boost_round=999,
                evals=[(data_test,"Test")],
                early_stopping_rounds=10,)

initial_predict = bst.predict(data_test,pred_leaf=False)

print(initial_predict)


print(bst.eval(data_test,name='eval'))
print(bst.eval_set([(data_test,"Test")]))
print(bst.eval(data_train,name='eval'))
print(bst.eval_set([(data_train,"Train")]))

print(bst.get_score('',importance_type='weight'))

xgb.plot_importance(bst,max_num_features=10)


xgb.plot_tree(bst)
plt.rcParams['figure.figsize'] = [10,5]
plt.show()

explainer = shap.TreeExplainer(bst)
shap_values_XGB_test = explainer.shap_values(X_test)
shap_values_XGB_train = explainer.shap_values(X_train)

df_shap_XGB_test = pd.DataFrame(shap_values_XGB_test)
df_shap_XGB_train = pd.DataFrame(shap_values_XGB_train)

j = 0
shap.initjs()
shap.force_plot(explainer.expected_value,shap_values_XGB_test[j],X_test.iloc[[j]])
shap.force_plot(explainer.expected_value,shap_values_XGB_test,X_test)

shap.summary_plot(shap_values_XGB_train,X_train,plot_type='bar')
shap.summary_plot(shap_values_XGB_train,X_train)
shap.dependence_plot('Days_1',shap_values_XGB_train,X_train)


#inputs = column of interest as string, column for coloring as string, df of our data, SHAP df, 
#      x postion of the black dot, y position of the black dot
def dep_plt(col, color_by, base_actual_df, base_shap_df, overlay_x, overlay_y): 
    cmap=sns.diverging_palette(260, 10, sep=1, as_cmap=True) #seaborn pallete 
    f, ax = plt.subplots() 

    points = ax.scatter(base_actual_df[:,col], base_shap_df[col], c=base_actual_df[:,color_by], s=20, cmap=cmap)
    f.colorbar(points).set_label(color_by) 
    ax.scatter(overlay_x, overlay_y, color='black', s=50) 
    plt.xlabel(col) 
    plt.ylabel("SHAP value for " + str(col)) 
    plt.show()
 


# get list of model inputs in order of SHAP importance
imp_cols = df_shap_XGB_train.abs().mean().sort_values(ascending=False).index.tolist()

# # loop through this list to show top 3 dependency plots
for i in range(0, len(imp_cols)):
    #plot the top var and color by the 2nd var
    if i == 0 :  
        dep_plt(imp_cols[i],  
        imp_cols[i+1],  
        np.asarray(X_train),  
        df_shap_XGB_train, 
        X_test.iloc[j,:][imp_cols[i]], 
        df_shap_XGB_test.iloc[j,:][imp_cols[i]]) 
     #plot the 2nd and 3rd vars and color by the top var
    if (i > 0) and (i < 3) :  
        dep_plt(imp_cols[i],  
        imp_cols[0],  
        np.asarray(X_train),  
        df_shap_XGB_train, 
        X_test.iloc[j,:][imp_cols[i]],  
        df_shap_XGB_test.iloc[j,:][imp_cols[i]])



# + set maximum num_boost_round node iterations, but set early_stopping_rounds at 10
# ## Using XGBoost CV
# + set params
# + set dtrain
# + use large number of num_boost_round and count on early_stopping_rounds to find optimal number of rounds before reaching the maximum
# + seed similar to train_test_splits random_state, but for running cross validation states because each train and each split is designated randomly by computer
# + number of folds in CV
# + set metrics used for scoring model

cv_results = xgb.cv(
    PARAMETERS,
    data_train,
    num_boost_round=999,
    seed=42,
    nfold=5,
    early_stopping_rounds=10,
    as_pandas=True,
)
print("cv results{}".format(cv_results))
print(f"best RSME score with cv :{cv_results['test-rmse-mean'].min()}")


# + cv return table where rows correspond number of boosting trees used
# + 4 columns correspond to mean and standard deviation for both train and test
# + goal in cv to optimize scoring for eval_metric param during cv

# ## Optimize max_depth and min_child_weight
# + max_depth is maximum number of nodes allowed from root to the farthest leaf of a tree. Deeper trees can model more complex relationships by adding more nodes, but as we go deeper, splits become less relevant and are sometiems only due to noise, causing model to overfit.
# + min_child_weight is the minimum weight(or of samples if all samples have a weight of 1) required in order to create a new node in the tree. A small min_child_weight allows the alogorithm to create children that corresponds to fewer samples, thus allowing for more complex trees, but again more likely to overfit.
# + important to tune together to find good trade-off between model bias and variance

"""
can try wider intervals with larger step between each value then narrow it down.

better try that myself to find optimal ranges

"""

gridsearch_params = [
    (max_depth,min_child_weight)
    for max_depth in range(9,13)
    for min_child_weight in range(5,8)
]

# + make list containing all combinations of max_depth/min_child_weight

min_rmse = float("Inf")
best_depth = None

for max_depth,min_child_weight in gridsearch_params:
    print(f"CV with max_depth={max_depth}, min_child_weight={min_child_weight}")

    PARAMETERS['max_depth'] = max_depth
    PARAMETERS['min_child_weight'] = min_child_weight

    cv_results = xgb.cv(
        PARAMETERS,
        data_train,
        num_boost_round=999,
        seed=42,
        nfold=5,
        metrics={'rmse'},
        early_stopping_rounds=10,
        as_pandas=True
    )

    mean_rmse = cv_results['test-rmse-mean'].min()
    boost_rounds = cv_results['test-rmse-mean'].argmin()
    print(f"\tRMSE {mean_rmse} for {boost_rounds}")

    if mean_rmse < min_rmse:
        min_rmse = mean_rmse
        best_depth = (max_depth,min_child_weight)

print(f"Best params: {best_depth[0]}, {best_depth[1]}, RMSE: {min_rmse}")

# + assign min rmse to infinite
# + loop through gridseach params(need to find custom optimal intervals from wide range then narrow down)
# + print current max_depth and min_child_weight iteration
# + update max_depth, min_child_weight to params
# + run cross validation for current iteration of max_depth,min_child_weight
# + aggregate test-rmse-mean minimum value and positional index of that value in array
# + print optimal scoring in array rounds per iteration
# + if current iteration of mean_rmse is less than previous iteration of mean_rmse, aggregate as min_rmse
# + print best params

# ## Optimize for subsample and colsample_bytree
#
# + these are parameters that control the sampling of dataset done at each boosting round
# + thus can build tree on slightly different data at each step making it less likely to overfit to any single sample or feature
# + subsample corresponds to the fraction of observations (the rows) to subsample at each step. default 1, meaning all rows.
# + colsample_bytree corresponds to fraction of features(the columns) to use. default is 1, meaning all columns

gridsearch_params = [
    (subsample, colsample)
    for subsample in [i/10. for i in range(7,11)]
    for colsample in [i/10. for i in range(7,11)]
]


min_rmse = float("Inf")
best_samples = None
# We start by the largest values and go down to the smallest

for subsample, colsample in reversed(gridsearch_params):
    print("CV with subsample={}, colsample={}".format(subsample,colsample)) 
    # We update our parameters

    PARAMETERS['subsample'] = subsample
    PARAMETERS['colsample_bytree'] = colsample    
    # Run CV

    cv_results = xgb.cv(
        PARAMETERS,
        data_train,
        num_boost_round=999,
        seed=42,
        nfold=5,
        metrics={'rmse'},
        early_stopping_rounds=10,
        as_pandas=True
    )    
    # Update best score

    mean_rmse = cv_results['test-rmse-mean'].min()
    boost_rounds = cv_results['test-rmse-mean'].argmin()
    print("\tRMSE {} for {} rounds".format(mean_rmse, boost_rounds))

    if mean_rmse < min_rmse:
        min_rmse = mean_rmse
        best_samples = (subsample,colsample)
        
print("Best params: {}, {}, RMSE: {}".format(best_samples[0], best_samples[1], min_rmse))

# + assign min rmse to infinite
# + We start by the largest values and go down to the smallest
# + print current subsample and colsample iteration
# + update subsample, colsample to params
# + run cross validation for current iteration of subsample, colsample
# + aggregate test-rmse-mean minimum value and positional index of that value in array
# + print optimal scoring in array rounds per iteration
# + if current iteration of mean_rmse is less than previous iteration of mean_rmse, aggregate as min_rmse
# + print best params
# ## Find best params for Learning rate (eta)
# + corresponds to the shrinkage of weights associated to features after each round, in other words it defines the amount of "correction" we make at each step 

min_rmse = float("Inf")
best_eta = None

for eta in [.3,.2,.1,.05,.01,.005]:
    print(f"CV with eta={eta}")

    PARAMETERS['eta'] = eta
    cv_results = xgb.cv(
        PARAMETERS,
        data_train,
        num_boost_round=999,
        seed=42,
        nfold=5,
        metrics={'rmse'},
        early_stopping_rounds=10,
        as_pandas=True
    )

    mean_rmse = cv_results['test-rmse-mean'].min()
    boost_rounds = cv_results['test-rmse-mean'].argmin()
    print(f"\tRMSE {mean_rmse} for {boost_rounds}")

    if mean_rmse < min_rmse:
        min_rmse = mean_rmse
        best_eta = eta

print(f"Best params: {best_eta}, RSME: {min_rmse}")

# + assign min rmse to infinite
# + loop through conventional learning rate (eta)
# + print current eta iteration
# + update eta to params
# + run cross validation for current iteration of eta
# + aggregate test-rmse-mean minimum value and positional index of that value in array
# +  print optimal scoring in array rounds per iteration
# + if current iteration of mean_rmse is less than previous iteration of mean_rmse, aggregate as min_rmse
# + print best params
# + training and best parameters

params = {
    'max_depth': best_depth[0],
    'min_child_weight': best_depth[1],
    'eta': best_eta,
    'subsample': best_samples[0],
    'colsample_bytree': best_samples[1],
    'objective':'reg:squarederror',
    'eval_metric':'rmse',
    'nthread':-1,
}

# + optimal parameters for xgboost API

model = xgb.train(
    params,
    data_train,
    num_boost_round=999,
    evals=[(data_test,"Test")],
    early_stopping_rounds=10,
)

print("Best RMSE: {:.2f} in {} rounds".format(model.best_score,model.best_iteration+1))

# if early stopping occurs, the model will have three additional fields .best_score, .best_iteration, and .best_ntree_limit

num_boost_round = model.best_iteration + 1

# allow for model best_iteration inclusive

best_model = xgb.train(
    params,
    data_train,
    num_boost_round = num_boost_round,
    evals=[(data_test,"Test")]
        
)

# + train data with optimal parameters

trainleaf = best_model.predict(data_train,pred_leaf=True)


testleaf = best_model.predict(data_test,pred_leaf=True)



print(testleaf)

# ## Multi Variate Normal Distribution Matrix
tree_pandas = []
tree_numpy = []
for column in range(max([len(x) for x in testleaf])):
    tree = []
    for row in testleaf[:,column]:
        lst = [0] * testleaf[:,column].max()
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
# + save model
best_model.save_model("xgbregression.model")



# + load model
loaded_model = xgb.Booster()
loaded_model.load_model("xgbregression.model")

print(loaded_model.eval(data_test,name='eval'))
print(loaded_model.eval_set([(data_test,"Test")]))
print(loaded_model.eval(data_train,name='eval'))
print(loaded_model.eval_set([(data_train,'Train')]))
print(loaded_model.get_score('',importance_type='weight'))



# ## Decision Tree/ Feature Importance Visualization

xgb.plot_importance(loaded_model,max_num_features=10)

xgb.plot_tree(loaded_model)
plt.rcParams['figure.figsize'] = [10,5]
plt.show()


predictions_API = loaded_model.predict(data_test,pred_leaf=False)

print(predictions_API)

best_explainer = shap.TreeExplainer(loaded_model)
best_shap_values_XGB_test = best_explainer.shap_values(X_test)
best_shap_values_XGB_train = best_explainer.shap_values(X_train)


best_df_shap_XGB_test = pd.DataFrame(best_shap_values_XGB_test)
best_df_shap_XGB_train = pd.DataFrame(best_shap_values_XGB_train)


shap.force_plot(best_explainer.expected_value,best_shap_values_XGB_test[j],X_test.iloc[[j]])
shap.force_plot(best_explainer.expected_value,best_shap_values_XGB_test,X_test)
shap.summary_plot(best_shap_values_XGB_train,X_train,plot_type='bar')
shap.summary_plot(best_shap_values_XGB_train,X_train)
shap.dependence_plot('Days_1',best_shap_values_XGB_train,X_train)

# # get list of model inputs in order of SHAP importance
imp_cols = df_shap_XGB_train.abs().mean().sort_values(ascending=False).index.tolist()
 
# loop through this list to show top 3 dependency plots
for i in range(0, len(imp_cols)):
    #plot the top var and color by the 2nd var
    if i == 0 :  
        dep_plt(imp_cols[i],  
        imp_cols[i+1],  
        np.asarray(X_train),  
        df_shap_XGB_train, 
        X_test.iloc[j,:][imp_cols[i]], 
        df_shap_XGB_test.iloc[j,:][imp_cols[i]]) 
     #plot the 2nd and 3rd vars and color by the top var
    if (i > 0) and (i < 3) :  
        dep_plt(imp_cols[i],  
        imp_cols[0],  
        np.asarray(X_train),  
        df_shap_XGB_train, 
        X_test.iloc[j,:][imp_cols[i]],  
        df_shap_XGB_test.iloc[j,:][imp_cols[i]])

def scatter_plot(y_test,pred_test):
    """
    Parameters
    ----------
    y_test : validation set.
    pred_test : prediction on test.

    Returns
    -------
    scatter plot.

    """
    fig, ax = plt.subplots()
    ax.scatter(y_test,pred_test, color='b')
    #ax.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'k--',lw=4)
    ax.set_xlabel('preds')
    ax.set_ylabel('y_test')
    ax.set_title('scatter plot')
    plt.show()

# scatter plot
plot = scatter_plot(y_test, predictions_API)


########## With Sklearn xgboost wrapper using GridSearchCV

# param_grid = {
#     'n_estimators': [400, 700, 1000],
#     'colsample_bytree': [0.7, 0.8],
#     'max_depth': [15,20,25],
#     'reg_alpha': [1.1, 1.2, 1.3],
#     'reg_lambda': [1.1, 1.2, 1.3],
#     'subsample': [0.7, 0.8, 0.9],
    
# }

# regressor = XGBRegressor(n_jobs=-1,objective='reg:squarederror')

# grid = GridSearchCV(regressor,param_grid,n_jobs=-1)

# # + https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

# start_time = timer(None)


# grid.fit(X_train,y_train)

# # fitting train data to grid search tuned parameters

# timer(start_time)

# best_pars = grid.best_params_
# best_model = grid.best_estimator_


# pickle.dump(grid.best_estimator_, open('sklearn_xgb_model','wb'))

# predictions = grid.predict(X_test)

# print(mean_squared_error(y_test,grid.best_estimator_.predict(X_test)))

# # mean sqaured error scoring and root squared scoring available from sklearn metrics
# pred = pd.DataFrame(predictions)
# print(predictions)

# fig, ax = plt.subplots()
# ax.scatter(y_test,pred, color='b')
# ax.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'k--',lw=4)
# ax.set_xlabel('preds')
# ax.set_ylabel('y_test')
# ax.set_title('scatter plot')
# plt.show()

