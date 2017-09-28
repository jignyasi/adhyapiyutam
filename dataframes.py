import os, sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages') ##***
import pandas as pd
import numpy as np

# pip install pandas
# pip install numpy
##Numpy basics
sal1 = [49,51,63,72,34]
print map(lambda x: x*1000, sal1)
sal2 = np.array([49,51,63,72,34])
print type(sal1), type(sal2)
print sal2*1000
print map(lambda x: x*1000, sal2)

#filter all values <= 55
print filter(lambda x: x<=55, sal1)
print sal2 <= 55
print sal2[sal2 <= 55]
#Indexing can be done through bool vector
print sal1[1,4]
#Indexing can be done through numbers
print sal2[[1,4]]

##Dataframe basics
WD = '/Users/anand/Documents/consulting/adhyapiyutam/'
df = pd.read_csv(WD+'UniversalBank.csv')#.head()
print df.head(3)
print df.dtypes
#dimensions of the data
print df.shape
print df.columns
print df['Age'] * 50

print map(lambda x: x*1000, myDF['Age'])

#PANDAS OPERATIONS
# Object Creation
    # Reading from file
        # pd.read_csv
    # Manual Creation
    #     DataFrame
    #     Series
# Reading from file
df = pd.read_csv(WD+'UniversalBank.csv')
print df.shape
print df.head()
print df.tail()

print [49,51,63,72,34] #list
print np.array([49,51,63,72,34]) #numpy array
print pd.Series([49,51,63,72,34]) #pandas series
# Manual Creation
age = pd.Series([49,51,63,72,34])
myDF = {"Age" : [10,20,40], \
"Experience":[1,3,2], \
"Family" : [1,2,1]
}
df2 = pd.DataFrame(myDF)
df3 = pd.DataFrame({'A':range(10),'B':list('abcdefghij')})
print df3
df4 = pd.DataFrame({'A':[88],'B':['xyz']}) #val shld always be in list
print df4
mylist = [[10, 20, 40], [1, 2, 1], [1, 3, 2]]
print pd.DataFrame(mylist,columns = ['A','B','C']).head()
# Meta Info
#     shape       
#     dtypes
print df3.shape
print df3.dtypes #int,float,object,bool
# Input/Output
#     Read & Write
print dir(df3)
df3.to_csv(WD+'df3.csv',index = False)

# Viewing Data
#     head
#     columns
#     index
print df3.head()
print df3.columns
print df3.index
print df3.columns.tolist()
print df3.index.tolist()

#COLUMNS
print df.Age.head()
print df['Age'].head()
print df[['Age','Experience']].head()

#ROWS
print df[3:5]
print df.index.tolist()
#df.loc[rows,cols]
#df.iloc[rows,cols] #row and cols should be numbers
print df.iloc[[1,3,5],[1,3]].head()
print df.loc[[1,3,5],['Family','CCAvg']].head()

temp = df.head().copy()
print temp
temp.index = list('abcde')
print temp.loc[['b','d','e'],['Family','CCAvg']].head()

#Setting Vals
print df['Age'].head()
df['TEMP'] = np.random.randint(3,30,5000)
print df.head()
df['Age'] += 5
df.loc[3,'Age'] = 60
df.loc[3,:] = 60

#DataWrangling
temp1 = temp.T #Transpose
print temp1, temp1.shape
print temp.describe()
temp['MYCOL'] = np.random.choice(list('ab'),5)
temp= temp.sort_index(ascending =False)
print temp.sort_values(['Age','Experience'], ascending =[True,False])
print temp.sort_values('MYCOL')

t1 = temp.iloc[:,[2,3]]
t2 = temp.iloc[:,[5,8]]
t1['ID1'] = np.arange(5)
t2['ID2'] = np.arange(5)
t2 = t2.sort_values('ID2', ascending = False)
print pd.merge(t1,t2,on ='ID')
t3 = t1.merge(t2, left_on = 'ID1', right_on = 'ID2')
print t3.drop(['ID1','ID2'],axis = 1)
print t3.drop([1,3],axis = 0)
t3['NEWCOL'] = ['hyd','pune','hyd','bang','pune']
t4 = t3.iloc[3]
t3 = t3.append(t4)
t3.loc[3,'Income']
t3 = t3.reset_index(drop = True)

t1 = temp.iloc[:,[2,3]]
t2 = temp.iloc[:,[5,8]]
print pd.concat([t1,t2],axis = 1)
t1.index = np.arange(5)
t2.index = np.arange(6,11)
print pd.concat([t1,t2],axis = 1)
print pd.concat([t1.reset_index(drop=True),t2.reset_index(drop=True)],axis = 1)


#AVG VAL FOR EACH COL
print df2.mean()
print df2.median()
print df2.max()
print df2.quantile([.2,.7])
print df2.cumsum()
#AVG VAL FOR EACH ROW
print df2.mean(axis = 1)
print df2.median(axis = 1)
print df2.max(axis = 1)
print df2[['Age','Family']].mean(axis = 1)
print df2.quantile([.2,.7],axis = 1)
print df2.cumsum(axis = 1)

#Multiply each col with 2
print df2*2/4
#if Age>15 add exp else sub exp from rowsum
df2[['Age','Family']].sum(axis=1) + df2['Experience']*np.where(df2['Age']<15, -1, 1)

def f1(x):
    y = -x['Experience'] if x['Age'] < 15 else x['Experience']
    return x['Age'] +x['Family'] + y
print df2.apply(f1,axis = 1)

def f2(x):
    return None

print df2.applymap(f2)
i,_ = df2.shape
for k in range(i):
    x,y, z = df2.loc[k,:]
    print x+y+z

df = pd.DataFrame({'loc':np.random.choice(['hyd','pune'],100),
    'age': np.random.choice(np.arange(10,20),100)})

def f(x): 
    return x + myDict[x.name]

def f2(x): 
    return x['age'].between(*myDict[x['loc'].unique()[0]])
# (10-15]:high_school
# (15-17]:plus1&2
# (17-20]:undergrads
print df['age'].head(10)
df['age_binned'] = pd.cut(df['age'], bins = [10,15,17,20], \
    labels = ['high_school','plus1&2','undergrads'])
df['gender'] = np.random.choice(list('mf'),100)
'''
print df['loc'].value_counts()
print df.groupby('loc').size()
print df['age_binned'].value_counts()
print pd.crosstab(df['loc'], df['age_binned'])
print df.groupby(['loc','age_binned']).size().unstack() #data shrink
print df.groupby('loc')['age'].aggregate(f) #data shrink
print df.groupby('loc')['age'].mean() #data shrink
#if hyd add 10 if pune add 20
myDict = {'hyd':10, 'pune':20}
df['corrected_age'] = df.groupby('loc')['age'].transform(f) #data size will remain as is, but you might add
#filter all guys between 12 to 14 in each loc
print df[df['age'].between(12,14)].head()
myDict = {'hyd':(12,14), 'pune':(16,18)}

print df.groupby('loc').filter(f2) #you will filter it 
print df.groupby('loc').filter(lambda x: x['age'].between(*myDict[x['loc'].unique()[0]])).head()
print df.groupby('loc').filter(lambda x: len(x['age']) >10).head()
'''

print df['loc'].value_counts()
print pd.crosstab(df['loc'],df['age_binned'])
print pd.crosstab(df['loc'],df['gender'])
print pd.crosstab(df['loc'],df['gender'])
df['gender'] = df['gender'].str.replace('m','male')
df['gender'] = df['gender'].str.replace('f','female')
df['gender'] = np.random.choice(list('mf'),100)
df['gender'] = df['gender'].replace({'m':'male','f':'female'}).head()
df.columns = ['A','B','C','D']
colNames = dict(zip(['A','B','C','D'], ['age','loc','age_binned','gender']))
df = df.rename(columns = colNames)

df = pd.read_csv(WD+'UniversalBank.csv').head()
print df.transform(lambda x: x.cumsum()) #restricts output to be a series
print df.apply(lambda x: x.cumsum()) #no such restriction
print df.aggregate(np.cumsum) #no such restriction
print df.agg(np.cumsum) #no such restriction
print df.transform(lambda x: x.sum()) #restricts output to be a series

df = pd.DataFrame({'loc':np.random.choice(['hyd','pune'],100),
    'age': np.random.choice(np.arange(10,20),100)})
df['age_binned'] = pd.cut(df['age'], bins = [10,15,17,20], \
    labels = ['high_school','plus1&2','undergrads'])
df['gender'] = np.random.choice(list('mf'),100)
catg_cols = ['loc','age_binned','gender']
print df[catg_cols].apply(lambda x: x.value_counts().to_dict())
print df[catg_cols].agg(lambda x: x.value_counts().to_dict())

#why do we group
# 1. check how data differs between groups
#     groupby, pivot_table
# 2. apply some logic for each group
#     only groupby
#for checking how data differs between groups

# df.to_csv(WD+'data_forgrouping.csv',index = False)
print df.pivot_table(values='age',index = 'loc',columns = 'gender')
print df.pivot_table(values='age',index = 'loc',columns = 'gender',aggfunc = lambda x: len(x))
print df[(df['loc']=='hyd') & (df['gender'] =='f')].shape
print df.pivot_table(values='age',index = ['age_binned','loc'],columns = 'gender')
print df.pivot_table(values='age',index = ['age_binned','loc'],columns = 'gender').stack().reset_index()
print df.pivot_table(values='age',index = 'loc')

grpd = df.groupby('loc')
print grpd.groups
print grpd['gender'].value_counts()
print df.groupby('loc')['gender'].value_counts()
print df.groupby('loc')['gender'].apply(lambda x: x.value_counts())
print df.groupby('loc')['age'].agg(lambda x: x.quantile([.4,.6])) #will throw error
print df.groupby('loc')['age'].apply(lambda x: x.quantile([.4,.6]))
print df.groupby(['loc','age_binned'])['age'].apply(lambda x: x.quantile([.4,.6]))
# in groupby
#     if you return single number use agg
#     if you return a series or single number or anything else use apply
#     if you return only a series use transform
#     if you return only a part of series use filter

# if grp: 'pune','high_school' add 10
# if grp: 'pune','undergrads' add 20
print df.pivot_table(values='age',index = 'loc',columns = 'age_binned')
def f(x):
    if x.name == ('pune','high_school'):
        return x+10
    elif x.name == ('pune','undergrads'):
        return x+20
    else:
        return x

df['age'] = df.groupby(['loc','age_binned'])['age'].apply(f)
print df.pivot_table(values='age',index = 'loc',columns = 'age_binned')
print df.head(20)

def f(x):
    if x.name == ('pune','high_school'):
        return False
    elif x.name == ('pune','undergrads'):
        return False
    else:
        return True
print df.groupby(['loc','age_binned']).filter(f).head(20)

print df.pivot_table(values='age',index = 'loc')
print df.pivot_table(values='age',index = 'loc',columns = 'age_binned')


df['bmi_index'] = np.random.randn(df.shape[0]).round(1)
df.rename(columns = {"age": 'x', 'bmi_index':'y'}, inplace = True)
# sqrt((x2-x1)^2+(y2-y1)^2) #euclidian distance in 2d space
print df.loc[0:1,['x','y']]
print pd.get_dummies(df['loc']).head()
print pd.get_dummies(df['age_binned']).head()
df1 = pd.get_dummies(df)
# sqrt((x2-x1)^2+(y2-y1)^2+(z2-z1)^2) #euclidian distance in 3d space
print df1.head()
# distance between x,y,hyd to x,y,pune == x,y,pune to x,y,bang...
df.rename(columns = {'x':"age", 'y':'bmi_index'}, inplace = True)
df.to_csv(WD+'sample_df.csv',index = False)

df2 = pd.read_csv(WD+'sample_df.csv', na_values = ['NA','','NULL',None])
# missing val summary
print df2.isnull().head()
print df2.isnull().sum()
print pd.get_dummies(df2['age_binned']).head(10)
# handling missing vals
    # by dropping
print df2.shape
print df2.dropna(how = 'any').shape
print df2.dropna(how = 'any').head(10)
    # by filling
print df2.fillna(9999).head(10)
myDtypes = df2.dtypes.reset_index()
catgCols = myDtypes['index'][myDtypes[0]=='object']
numCols = myDtypes['index'][~myDtypes['index'].isin(catgCols)]
#missing vals are replaced by means for numerics and modes for catg
df2 = df2.apply(lambda x:  x.fillna(x.mean()) if x.name in numCols else x.fillna(x.mode()[0])).head(25)