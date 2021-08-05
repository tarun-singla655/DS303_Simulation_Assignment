
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def function(x):
    if 0 < x < 5:
        return (1/40) * (2 * x + 3)
    return 0
# finding inverser from cdf of fx
def invfunction(x):
    return -1.5 + np.sqrt(9+160*x)/2 




# generating random samples 
U = np.random.uniform(size=1000)
X = invfunction(U)
plt.grid(True)
xx = np.linspace(-10, 10, 1000)
plt.hist(X, bins=40, density=True, ec='violet', fc='purple', alpha=0.75)
plt.plot(xx, np.fromiter([function(x) for x in xx], xx.dtype, xx.size), c='red')
plt.title("random sampling of function f(x) using inverse transform sampling")
plt.legend()
plt.show()
