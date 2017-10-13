import os, sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages') ##***
import pandas as pd
import numpy as np

WD = '/Users/anand/Documents/consulting/adhyapiyutam/'
df = pd.read_csv(WD+'UniversalBank.csv')#.head()
df['city'] = np.random.choice(['hyd','bang','chennai'],5000, True)
df['Family'] = df['Family'].astype('category')
print df.head(3)
print df.tail(3)
# Meta information
print df.dtypes
print df.shape
print df.columns
print df.index
QUESTION: find all numeric attrbs
QUESTION: find all categorical attrbs
print df['city'].head(10)
print df[['city','CreditCard']].head(10)
print df.loc[0]
print df.iloc[10,5] #index by integer
print df.loc[10,'Age'] #index by integer
print df.loc[10,:] #index by integer
df1 = df.loc[5:10,:]
QUESTION: subset df from 100 to 150 rows and 2 to 7 columns
print df1.iloc[0,0]
print df1.loc[5,'Age']
# df1 = df1.reset_index(drop = True)
df1.reset_index(drop = True, inplace = True)
print df1.head()
print df1.loc[3,'Age']
df2 = df1.describe()
print df2.index
print df2.head()
print df2.iloc[0,0]
print df2.loc['count',:]
df3 = df2.T
print df3.sort_values('mean',ascending = False)
print df3.sort_values(['mean','std'],ascending = [False,True])

# Row binding and Column Binding
df4 = df.describe()
df4 = df4.T
print df3.shape, df4.shape
print df3.tail(), df4.head()
#row binding
df5 = df3.append(df4)
print df5
# adding a column
df3['myCol'] = np.random.choice(range(100),12)
print df3.tail()
#column binding
df6 = pd.concat([df3,df4],axis = 1).head()
print df6
df3['ID'] = np.random.choice(range(1,13),12,False)
df4['ID'] = np.random.choice(range(1,13),12,False)
print df3.tail(), df4.head()
#column binding through merging
df7 = pd.merge(df3, df4,on = 'ID').head()
print df7
print df7.mean()
print df7.quantile([.25,.5,.75])
print dir(df7)
print df7['mean_x']
print df7['mean_x'].cumsum()
print (df7['mean_x'] * 5)/13
print df['city'].value_counts()
print (df['CreditCard'].value_counts()/df.shape[0])*100
print pd.crosstab(df['city'],df['CreditCard'])
df8 = pd.crosstab(df['city'],df['CreditCard'])
print df8
print df8.apply(lambda x: x*100/x.sum(), axis = 1)
print df8.transform(lambda x: x*2)
print df8.aggregate(lambda x: (x[0],x[1]))























