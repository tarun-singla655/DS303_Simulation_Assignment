#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)
# finding value of y for particular x 
def semi_circle(x):
    return np.sqrt(1 - x**2)


#checking whether points inside function circle
def points_below(N, f):
    X = np.random.uniform(A, B, size=N)
    Y = np.random.uniform(0, C, size=N)
    #return np.sum(Y < f(X))
    count = 0
    Y1 = f(X)
    for i in range(len(Y)):
        if (Y[i] <= Y1[i] ):
            count+=1
    return count

A = -1
B = 1
C = 1


#ploting 
fig, ax = plt.subplots(figsize=(8, 3))
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
graph2, = ax.plot([], [])
graph3, = ax.plot([0, 2])
no_of_p = 0
total_p = 0

def gen_data():
    while True:
        yield np.random.uniform(A, B), np.random.uniform(0, C)

def init():
    global graph3
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 6)
    ax.grid(True)


# updating the values 
def update(data):
    global no_of_p, total_p
    x, y = data
    xdata1.append(x)
    ydata1.append(y)
    total_p += 1
    if y <= semi_circle(x):
        no_of_p += 1
    pi_est = (4 * no_of_p / total_p)
    xdata2.append(total_p)
    ydata2.append(pi_est)
    xmin, xmax = ax.get_xlim()
    if not (xmin < xdata2[-1] < xmax):
        ax.set_xlim(2*xmin, 2*xmax)
        graph3.set_data([2*xmin, 2*xmax], [np.pi]*2)
        ax.figure.canvas.draw()
    graph2.set_data(xdata2, ydata2)


ani = FuncAnimation(fig, update, gen_data(), init, interval=1, repeat=False)
ani.save('pivalue.gif',writer='pillow')
plt.tight_layout()
plt.show()

N = 3000
pi_value = []
pi_l = []

pi_u = []
#finding the confidence interval
z = 1.644854369

for N in range(1, N + 1):
    p_cap = points_below(N, semi_circle)
    l = p_cap - z * np.sqrt(p_cap* (N - p_cap) / N)
    u_est = p_cap + z * np.sqrt(p_cap * (N - p_cap) / N)
    pi_value.append(p_cap * 2 * C * (B-A) / N)
    pi_l.append(l * 2 * C * (B-A) / N)
    pi_u.append(u_est * 2 * C * (B-A) / N)
# plotting 
plt.grid(True)
plt.plot(np.arange(1, N+1), pi_value)
plt.fill_between(np.arange(1, N+1), pi_l, pi_u, alpha=.2)
plt.title('Estimated value of π with 90% confidence interval is ')
plt.plot(np.arange(1,N+1), [np.pi] * N)
plt.show()
