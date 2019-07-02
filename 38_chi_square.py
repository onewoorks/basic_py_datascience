# Chi Square test is a statistical method to determine if two categorical
# variables have significate correlation between them. Both those variables
# shout be from same population and the should be categorical like - Yes/No,
# Male/Female, Red/Green etc. 

from scipy import stats
import numpy as numpy
import matplotlib.pyplot as plt 

x = numpy.linspace(0,10,100)
fig, ax = plt.subplots(1,1)

linestyles = [':','--','-.','-']
deg_of_freedom = [1,4,7,6]

for df, ls in zip(deg_of_freedom, linestyles):
    ax.plot(x, stats.chi2.pdf(x,df), ls)

plt.xlim(0,10)
plt.ylim(0,0.4)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Chi-Square Distribution")
plt.legend()
plt.show()