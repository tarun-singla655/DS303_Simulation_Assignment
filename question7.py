#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def is_psd(x):
    try:
        np.linalg.cholesky(x)
        return True
    except np.linalg.LinAlgError:
        return False

# -- (a) --

# c*I
# generating random variable
c = np.random.uniform(-1, 1)
cov = c * np.identity(2)
# while matrix is not positive definite 
while not is_psd(cov):
    c = np.random.uniform(-1, 1)
    cov = c * np.identity(2)
# ploting 
B = np.random.multivariate_normal(np.zeros(2), c * np.identity(2), size=100_000)
fig, ax = plt.subplots(figsize=(5,5))
ax.grid(True)
ax.set_title('Cov. matrix = c * Identity')
ax.scatter(*B.T, c='r', alpha=0.2)
plt.show()



# -- (b) --
fig, ax = plt.subplots(figsize=(5,5))
a1 = np.random.uniform(-1, 1)
a2 = np.random.uniform(-1, 1)
cov = np.diag([a1, a2])
while not is_psd(cov):
    a1 = np.random.uniform(-1, 1)
    a2 = np.random.uniform(-1, 1)
    cov = np.diag([a1, a2])
B = np.random.multivariate_normal(np.zeros(2), cov, size=100_000)
ax.grid(True)
ax.set_title('Cov. matrix = diag(a1, a2)')
ax.scatter(*B.T, c='r', alpha=0.2)
plt.show()

# -- (c) --
a = np.random.uniform(0, 1)
c = np.random.uniform(0, 1)
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(8,7))
# Fix main diagonal elements and vary off diagonal
bs = np.linspace(-np.sqrt(a*c), np.sqrt(a*c), 16)
# generating covariance matrix and ploting 
for axis, b in zip(ax.flatten(), bs):
    cov = np.array([
        [a, b],
        [b, c]
    ])
    B = np.random.multivariate_normal(np.zeros(2), cov, size=10000)
    axis.grid(True)
    axis.set_title(f'Corr = {b/np.sqrt(a*c):.2f}')
    axis.scatter(*B.T, c='r', alpha=0.2)
plt.tight_layout()
plt.show()

print('We can see that when correlation between the two normal random variable equals 0 we get a standard  plot.  When the two random variables are completely correlated then scatter plot reduces to a 1-D plot.')
print()
print('we can  observe for other distributions as well.')
