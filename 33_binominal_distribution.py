# The binominal distribution model deals with finding the probablity of success of
# an event which has only two possible outcomes in a series experiments. For
# example, tossing a coin always gives a head or a tail. The probability of 
# finding exactly 3 heads in tossing a coin repeatly for 10 times is estimated 
# during the binominal distribution.

# We use the seaborn library which has in-built functions to create such
# probabilty distribution graphs. Also, the scipy package helps is creating
# the binominal distribution

from scipy.stats import binom
import seaborn as sb 
import matplotlib.pyplot as plt 

binom.rvs(size=10, n=20, p=0.8)

data_binom = binom.rvs(n=20, p=0.8, loc=0, size=1000)
ax = sb.distplot(data_binom, kde=True, color='b', hist_kws={"linewidth":25, 'alpha':1})
ax.set(xlabel='Binomial', ylabel="Frequency")
plt.show()