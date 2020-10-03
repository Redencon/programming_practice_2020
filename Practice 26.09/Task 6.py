import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.001)
y = []
a = 3
b = 0.5
for i in x:
    cur = 0
<<<<<<< HEAD
    for n in range(1, 100):
=======
    for n in range(0, 100):
>>>>>>> origin/master
        cur += b**n * np.cos(a**n * np.pi * i)
    y.append(cur)
plt.plot(x, y, label='Функция Вейерштрасса')
plt.title('Функция Вейерштрасса')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
<<<<<<< HEAD
=======
plt.grid(True)
>>>>>>> origin/master
plt.show()
