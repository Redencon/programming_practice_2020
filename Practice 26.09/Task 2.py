import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.50, 3.50, 0.01)
plt.plot(x, x**2 - x - 6, 'r', x, 0*x, 'k')
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x) = x^2 - x - 6$')
plt.show()
