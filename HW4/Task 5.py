import matplotlib.pyplot as plt
import numpy as np


def func(x: float):
    """
    Returns the value of function determined by the task
    """

    if x < -5:
        return -2 * x - 1
    elif x < 5:
        return x * x
    else:
        return 2 * x


arg = np.arange(-10, 10, 0.01)
rez = [func(elem) for elem in arg]  # function works with integers and floats, not aranges, so we calculate rez ahead
plt.plot(arg, rez)
plt.show()
