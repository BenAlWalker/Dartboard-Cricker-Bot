
import random
import numpy as np
from matplotlib import pyplot as plt

darts_thrown = int(input("How many darts do you want the computer to throw? "))
variance = int(input("On a scale 0-100, how precise do you want the computer to be? "))

# creating the dart board
thetheta = np.linspace(0, 2 * np.pi, 100)
radius0 = 225.5
radius1 = 170
radius2 = 162
radius3 = 107
radius4 = 99
radius5 = 16
radius6 = 6.35

a = radius0 * np.cos(thetheta)
b = radius0 * np.sin(thetheta)
c = radius1 * np.cos(thetheta)
d = radius1 * np.sin(thetheta)
e = radius2 * np.cos(thetheta)
f = radius2 * np.sin(thetheta)
g = radius3 * np.cos(thetheta)
h = radius3 * np.sin(thetheta)
i = radius4 * np.cos(thetheta)
j = radius4 * np.sin(thetheta)
k = radius5 * np.cos(thetheta)
l = radius5 * np.sin(thetheta)
m = radius6 * np.cos(thetheta)
n = radius6 * np.sin(thetheta)

figure, axes = plt.subplots(1)

axes.plot(a, b, color='black')
axes.plot(c, d, color='black')
axes.plot(e, f, color='black', linewidth=0.75)
axes.plot(g, h, color='black', linewidth=0.75)
axes.plot(i, j, color='black', linewidth=0.75)
axes.plot(k, l, color='black', linewidth=0.75)
axes.plot(m, n, color='black', linewidth=0.75)

axes.set_aspect(1)

x1 = np.linspace(-169, 169, 100)
y1 = -0.15838*x1
plt.plot(x1, y1, 'k-', linewidth=0.5)

# plotting the dart board, to scale of a real one

x2 = np.linspace(-167, 167, 100)
y2 = x2*0.15838
plt.plot(x2, y2, 'k-', linewidth=0.5)

x3 = np.linspace(-150, 150, 100)
y3 = x3*0.509525
plt.plot(x3, y3, 'k-', linewidth=0.5)

x4 = np.linspace(-120, 120, 100)
y4 = x4
plt.plot(x4, y4, 'k-', linewidth=0.5)

x5 = np.linspace(-78, 78, 100)
y5 = 1.96261*x5
plt.plot(x5, y5, 'k-', linewidth=0.5)

x6 = np.linspace(-27, 27, 100)
y6 = 6.31375*x6
plt.plot(x6, y6, 'k-', linewidth=0.5)

x7 = np.linspace(-27, 27, 100)
y7 = -6.31375*x7
plt.plot(x7, y7, 'k-', linewidth=0.5)

x8 = np.linspace(-78, 78, 100)
y8 = -1.96261*x8
plt.plot(x8, y8, 'k-', linewidth=0.5)

x9 = np.linspace(-120, 120, 100)
y9 = -1*x9
plt.plot(x9, y9, 'k-', linewidth=0.5)

x10 = np.linspace(-150, 150, 100)
y10 = -0.509525*x10
plt.plot(x10, y10, 'k-', linewidth=0.5)

plt.axis('off')

# darts are thrown using random normal distributions, change in variance changes precision

while darts_thrown > 0:
    plt.plot(random.gauss(0, variance*1.75), random.gauss(0, variance*1.75), 'rx', markersize=4)
    darts_thrown -= 1

plt.show()
