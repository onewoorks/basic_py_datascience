from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('data/time_series.csv')
df = pd.DataFrame(data, columns=['ValueDate', 'Price'])

df['ValueDate'] = pd.to_datetime(df['ValueDate'])

df.index = df['ValueDate']
del df['ValueDate']

df.plot(figsize=(15,6))
plt.show()