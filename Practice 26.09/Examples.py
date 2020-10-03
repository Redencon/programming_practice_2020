import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), label=r'$f_1 = sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2 = cos(x)$')
plt.plot(x, -x, label=r'$f_3 = -x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x) = cos(x), f_2(x) = sin(x), f_3(x) = -x$')
plt.grid(True)
plt.legend(loc='best')
plt.show()
