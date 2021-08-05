#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(2**32-2)

def f(x):
    return (1/27) * (-65536*x**8 + 262144*x**7 - 409600*x**6 + 311296*x**5 - 114688*x**4 + 16384*x**3)

def points_below(N, f):
    X = np.random.uniform(A, B, size=N)
    Y = np.random.uniform(0, C, size=N)
    Y1 = f(X)
    count = 0
    for i in range(len(Y)):
        if(Y[i] <= Y1[i]):
            count+=1
    return count

xx = np.linspace(0, 1, 100)
plt.grid(True)
plt.plot(xx, f(xx))
plt.plot(xx, [1]*len(xx), c='r')
plt.plot(xx, [0]*len(xx), c='r')
plt.plot([1]*len(xx), xx, c='r')
plt.plot([0]*len(xx), xx, c='r')
plt.legend(loc=1)
plt.show()

A = 0
B = 1
C = 1

fig, ax = plt.subplots(figsize=(8, 3))
AA = 0.481599059377
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
graph2, = ax.plot([], [])
graph3, = ax.plot([0, 2], [AA]*2)
no_of_p = 0
total_p = 0

def gen_data():
    while True:
        yield np.random.uniform(A, B), np.random.uniform(0, C)

def init():
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.grid(True)

def update(data):
    global no_of_p, total_p
    x, y = data
    xdata1.append(x)
    ydata1.append(y)
    total_p += 1
    if y <= f(x):
        no_of_p += 1
    f_est = no_of_p / total_p
    xdata2.append(total_p)
    ydata2.append(f_est)
    xmin, xmax = ax.get_xlim()
    if not (xmin < xdata2[-1] < xmax):
        ax.set_xlim(2*xmin, 2*xmax)
        graph3.set_data([2*xmin, 2*xmax], [AA]*2)
        ax.figure.canvas.draw()
    graph2.set_data(xdata2, ydata2)


ani = FuncAnimation(fig, update, gen_data(), init, interval=1, repeat=False)
ani.save('functionintegeral.gif',writer='pillow')
plt.tight_layout()
plt.show()

N = 2000
area_value = []
area_l = []
area_u = []
z = 1.644854369
for N in range(1, N + 1):
    p_cap = points_below(N, f)
    l_est = p_cap - z * np.sqrt(p_cap * (N -p_cap) / N)
    u_est = p_cap + z * np.sqrt(p_cap* (N - p_cap) / N)
    area_value.append(p_cap * C * (B-A) / N)
    area_l.append(l_est * C * (B-A) / N)
    area_u.append(u_est * C * (B-A) / N)
    
plt.grid(True)
plt.plot(np.arange(1, N+1), area_value)
plt.title('Estimated value of integral with 90% confidence interval is')
plt.fill_between(np.arange(1, N+1), area_l, area_u, alpha=.2)
plt.plot(np.arange(1,N+1), [AA] * N)
plt.show()
