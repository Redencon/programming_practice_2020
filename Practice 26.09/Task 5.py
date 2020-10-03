import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
plt.plot(x, y, 'ko')
plt.errorbar(x, y, xerr=0.05, yerr=0.1, ecolor='#D3D3D3')
v = np.polyfit(x, y, deg=1)
apr = []
for i in x:
    apr.append(v[0]*i + v[1])
plt.plot(x, apr, 'b')
v = np.polyfit(x, y, deg=2)
apr = []
for i in x:
    apr.append(v[0]*i**2 + v[1]*i + v[2])
plt.plot(x, apr, 'r')
plt.show()
