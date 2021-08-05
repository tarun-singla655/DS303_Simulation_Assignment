
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)

def f(x):
    return (1/np.sqrt(2*np.pi)) * np.exp((-1/2) * x**2)

def g(x):
    return 1/(np.pi * (1 + x**2))

M = np.sqrt(2 * np.pi / np.exp(1))
print(f'M = {M}')

xs = np.linspace(-5, 5, 100)
plt.plot(xs, f(xs))
plt.grid(True)
plt.plot(xs, M * g(xs))
plt.show()
figure, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 50)
ax.grid(True)
_, _, bars = ax.hist(np.zeros(1000), bins=xs, range=(-5,5), ec='y', fc='g', alpha=0.5)
hist_data = []
nvals = 0
rvals = 0
# yeilding cauchy distribution
def cauchy():
    while True:
        yield np.random.uniform(), np.random.standard_cauchy()
# accepting and rejecting samples
def updatevalue(data):
    global nvals, rvals
    u, c = data
    nvals += 1
    if u < f(c)/(M * g(c)):
        hist_data.append(c)
        n, _ = np.histogram(hist_data, bins=xs, range=(-5,5))
        for count, p in zip(n, bars.patches):
            p.set_height(count)
    else:
        rvals += 1
    return bars.patches

ani = FuncAnimation(figure, updatevalue, cauchy(), interval=1, repeat=False)
ani.save('normalpdfcauchy.gif',writer='pillow')
plt.show()
