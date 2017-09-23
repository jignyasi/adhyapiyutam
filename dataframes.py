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