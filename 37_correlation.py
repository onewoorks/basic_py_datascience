# correlation refers to some statical relationship involving dependence 
# between two data sets. Simple examples of dependent phenomena include the
# correlation between the physical appearence of parents and the offspring,
# and the correlation between the price for a product and its supplied quantity

import matplotlib.pyplot as plt 
import seaborn as sb 

df = sb.load_dataset('iris')

sb.pairplot(df, kind="scatter")
plt.show()