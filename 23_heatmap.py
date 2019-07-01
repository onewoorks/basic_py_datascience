import pandas as pd 
import matplotlib.pyplot as plt

data = [
    {2,2,1,3},
    {6,2,7,3},
    {8,5,1,4},
    {1,7,4,3},
    {2,8,3,6}
]
index = ['I1','I2','I3','I4','I5']
cols = ['C1','C2','C3','C4']
df = pd.DataFrame(data, index=index, columns = cols)

plt.pcolor(df)
plt.show()