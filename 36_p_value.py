# the p-value is about the strength of a hypothesis. We build hypothesis based
# on some stastical model and compare the model's validity using p-value. One
# way to get the p-value is by using T-test.

# this is a two-sided test for the null hypothesis that the expected value(mean)
# of a sample of independent observations 'a' is equal to the given population
# mean, popmean. 

from scipy import stats
rvs = stats.norm.rvs(loc=5, scale=10, size=(50,2))
print(stats.ttest_1samp(rvs,5.0))

# Comparing two samples