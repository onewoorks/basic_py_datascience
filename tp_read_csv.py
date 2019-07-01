import pandas as pd 
data = pd.read_csv('./csv_data.csv')
print(data)

print("\n")
print("Read specific row")
print(data[0:5]['salary'])

print("\n")
print("Read specific columns")
print(data.loc[:,['salary','name']])

print("\n")
print("Read specific columns and rows")
print("------------------------------")
print(data.loc[[1,3,5],['salary','name']])

print("\n")
print("Reading specific columns for a range of rows")
print("--------------------------------------------")
print(data.loc[2:6,['salary','name']])