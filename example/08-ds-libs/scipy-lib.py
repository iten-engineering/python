# =============================================================================
# Python examples - data science library scipy
# =============================================================================

# Scipy ist eine Sammlung von mathematischen Funktionen und Algorithmen
# - basiert auf numpy
# - organisiert mit Sub Packages
# - normalerweise werden direkt individuelle Packages importiert
#   from scipy import linalg

# Scipy Packages
# Details see https://docs.scipy.org/doc/scipy/reference/

# -----------------------------------------------------------------------------
# Optimize
# -----------------------------------------------------------------------------

print("#")
print("# Optimize")
print("#")

import numpy as np
from scipy import optimize

x = np.arange(0,10)
y = 2 * x + 3 + np.random.random(10)

res = optimize.curve_fit(lambda x, a, b: a*x + b, x, y)
print(res)


# -----------------------------------------------------------------------------
# Statistics
# -----------------------------------------------------------------------------

print("#")
print("# Statistics")
print("#")

from scipy import stats

x = np.arange(0,10)
print(stats.describe(x))

# Correlation
# stats.pearson(b, b)

# T-Test
# stats.ttest_1samp(b, mean)

# -----------------------------------------------------------------------------
# Cluster
# -----------------------------------------------------------------------------

print("#")
print("# Cluster")
print("#")

from scipy import cluster

data = np.array([[1,2], [0.1,1],[3,0],[4,-0.1]])

res = cluster.vq.kmeans(data, 2)        # Classify a set of observations into
print(res)                              # k clusters using k-means algorithm.

# -----------------------------------------------------------------------------
# Further details
# -----------------------------------------------------------------------------

# Links:
# - https://docs.scipy.org/doc/scipy/reference/

# =============================================================================
# The end.

