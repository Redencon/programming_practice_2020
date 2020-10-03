import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
fun = input()
plt.plot(x, eval(fun))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title("The plot of your function")
plt.show()
