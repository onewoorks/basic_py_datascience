# A poisson distribution is a distribution which shows the likely number of times
# thant an event will occur within a pre-determined period of time. It is used for
# independent events which occur at a constant rate within a given interval of 
# time. The Poisson Distribution is a discrete function, meaning that the event 
# can only be measured as occuring or not as occuring, meaning the variable
# can only be measured in whole number.

from scipy.stats import poisson
import seaborn as sb 
import matplotlib.pyplot as plt 

data_binom = poisson.rvs(mu=4, size=1000)
ax = sb.distplot(data_binom, kde=True, color='green', hist_kws={"linewidth":25, 'alpha':1})
ax.set(xlabel="Poisson", ylabel="Frequency")
plt.show()