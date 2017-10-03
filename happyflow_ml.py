import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# Preprocessing
# Target is class
WD = '/Users/anand/Documents/consulting/adhyapiyutam/'
df = pd.read_csv(WD + 'UniversalBank.csv')
print df.head()
print df.isnull().sum()
print df.dtypes
df['Securities.Account'] = df['Securities.Account'].astype('category')
df['CD.Account'] = df['CD.Account'].astype('category')
df['Online'] = df['Online'].astype('category')
df['CreditCard'] = df['CreditCard'].astype('str')
df = pd.get_dummies(df)
print df['class'].value_counts()/float(df.shape[0]) * 100

# Modelling
Target = 'class'
allXs = df.columns.tolist()
allXs.remove(Target)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(df[allXs], df[Target])
predictions = clf.predict(df[allXs])

# Cross-Validation
actuals = df[Target]
print accuracy_score(actuals, predictions)
print precision_score(actuals, predictions)
print recall_score(actuals, predictions)
print f1_score(actuals, predictions)
df['Predicted_Val'] = predictions
