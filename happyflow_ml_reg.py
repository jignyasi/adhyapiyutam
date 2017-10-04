import numpy as np
import pandas as pd
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy import stats
import matplotlib.pyplot as plt
# Preprocessing
# Target is Income
WD = '/Users/anand/Documents/consulting/adhyapiyutam/'
df = pd.read_csv(WD + 'UniversalBank.csv')
print df.head()
print df.isnull().sum()
print df.dtypes
df['Securities.Account'] = df['Securities.Account'].astype('category')
df['CD.Account'] = df['CD.Account'].astype('category')
df['Online'] = df['Online'].astype('category')
df['class'] = df['class'].astype('category')
df['CreditCard'] = df['CreditCard'].astype('str')
df = pd.get_dummies(df)

# Modelling
Target = 'Income'
allXs = df.columns.tolist()
allXs.remove(Target)
clf = RandomForestRegressor(n_estimators = 3000, max_depth=6, random_state=0, n_jobs = 8)
clf.fit(df[allXs], df[Target])
predictions = clf.predict(df[allXs])

# Cross-Validation
actuals = df[Target]
print math.sqrt(mean_squared_error(actuals, predictions)) #RMSE
# MAPE: MEAN ABSOLUTE PERC ERR
err = predictions - actuals
abserr = abs(err)
print np.mean((abserr/actuals) * 100) #MAPE
# RMSE: ROOT MEAN SQR ERR
print math.sqrt(np.mean((err * err))) #RMSE
# MaxAPE: Max ABSOLUTE PERC ERR
print max((abserr/actuals)*100) #MaxAPE
# SMAPE: Symmetric Mean Abs Perc ERR
avgVals = (actuals + predictions)/2
print np.mean(abs(err)/avgVals)*100 #SMAPE

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(range(1,5), [11, 25, 9, 26], color='darkgreen', marker='^')
ax.scatter(range(1,5), [12.3, 21, 9.8, 24], color='lightblue')
plt.show()

actuals = np.array([11, 25, 9, 26])
predictions = np.array([12.3, 23.7, 10, 25])
predictions = np.array([11.1, 24.99, 9.01, 26.01])
#AVG ERR
err = predictions - actuals
print err.mean()
print math.sqrt(np.mean((err * err))) #RMSE
# RMSE is abs err
# if actual is 1 and we predicted 2 
# 	abs err is 1 unit
# 	relative err is 100%
# if actual is 25 and we predicted 26
# 	abs err is 1 unit
# 	relative err is 4%

actuals = np.array([1,11, 25, 9, 26])
predictions = np.array([2, 12.3, 23.7, 8, 25])
err = predictions - actuals
abserr = abs(err)
print np.mean((abserr/actuals) * 100) #MAPE
print max((abserr/actuals) * 100) #MaxAPE
sal = [400, 200]+[10]*10
print np.mean(sal)
print np.median(sal)
print stats.mode(sal)[0][0]

actuals = np.array([0.0,1,11, 25, 9, 26])
predictions = np.array([0.1, 2, 12.3, 23.7, 8, 25])
err = predictions - actuals
abserr = abs(err)
# SMAPE: mean(abs(err)/avg(actual & predict))*100
avgVals = (actuals + predictions)/2
print np.mean(abs(err)/avgVals)*100 #SMAPE
