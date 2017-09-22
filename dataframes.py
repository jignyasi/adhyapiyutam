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

#Getting
print df3.loc[[1,4,9],['A','B']]
print df3.iloc[[1,4,9],[0,1]]