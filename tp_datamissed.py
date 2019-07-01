import pandas as pd 
import numpy as np 

df = pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','h'], columns=['one','two','three'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

print(df)

print('\n')
print('Check missing values')
print(df['one'].isnull())

print('\n')
print('Replace NaN with a scaler value')

rein = df.reindex(['a','b','c'])
print(rein.fillna(0))

print("\n")
print("Fill NA Forward and backward")
df = df.reindex(['a','b','c','d','e','f','g','h'])

print(df.fillna(method='pad'))

print("\n")
print(df.dropna())

print("\n")
df = pd.DataFrame({
    'one': [10,20,30,40,50,2000],
    'two': [1000,0,30,40,50,60]
})
print(df.replace({1000:10,2000:60}))
