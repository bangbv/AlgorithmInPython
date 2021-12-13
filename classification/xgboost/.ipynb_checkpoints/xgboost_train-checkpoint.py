import xgboost as xgb

# read in data
dtrain = xgb.DMatrix('/Users/bangbui/workspace/xgboost/demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('/Users/bangbui/workspace/xgboost/demo/data/agaricus.txt.test')
# specify parameters via map
param = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
num_round = 2
bst = xgb.train(param, dtrain, num_round)
# make prediction
preds = bst.predict(dtest)


# NOTE : This is an important note
print("dtest: ", dtest)
print("preds: ", preds)
