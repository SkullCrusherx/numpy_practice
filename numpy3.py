import numpy as np
# Random Value 1D ready
var = np.random.rand(5)
print(var)

#randn() for neg can get and close to 0 also get
var_rnd = np.random.randn(5)
print(var_rnd)

#ranf()
# 0 to 1 work only this side

"""var_rndf = np.random.ranf((5,3))
print(var_rndf)"""

var_randint = np.random.randint(min(5,10),max(5,10))
print(var_randint)
