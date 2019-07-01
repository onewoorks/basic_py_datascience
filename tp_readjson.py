import pandas as pd

data = pd.read_json("json_data.json")

print("All Data")
print("--------")
print(data)

print("\n")
print("Reading Specific Columns and Rows")
print(data.loc[1:6,['Salary','Name']])