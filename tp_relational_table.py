from sqlalchemy import create_engine
from pandas.io import sql

import pandas as pd 


data = pd.read_csv('csv_data.csv')

engine = create_engine("sqlite:///:memory:")

data.to_sql('data_table',engine)

res1 = pd.read_sql_query("SELECT * FROM data_table", engine)
print("Result 1")
print(res1)

res2 = pd.read_sql_query("SELECT dept, sum(salary) FROM data_table GROUP BY dept",engine)
print("\n")
print("Result 2")
print(res2)

#insert new row
sql.execute("INSERT INTO data_table VALUES(?,?,?,?,?,?)", engine, params=['8','9','Irwan','812.00','2019-04-10','IT'])
res3 = pd.read_sql_query("SELECT * FROM data_table", engine)
print("\n")
print("Insert new row")
print('--------------')
print(res3)