import pandas as pd 
import numpy as np 

data = np.array(['a','b','c','d','e'])
s = pd.Series(data)
print(s)

data_2 = {'Name':['Tom', 'Jack', 'Steve','Ricky'],'Age':[28, 34, 29, 42]}
df = pd.DataFrame(data_2, index=['rank1','rank2','rank3','rank4'])
print(df)

data_3 = {
    'Item1' : pd.DataFrame(np.random.randn(4,3)),
    'Item2' : pd.DataFrame(np.random.randn(4,2))
}
p = pd.Panel(data_3)
print(p)