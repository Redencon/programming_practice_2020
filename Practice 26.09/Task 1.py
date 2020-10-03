import numpy as np

x = [1, 10, 1000]
for i in x:
    y = np.log((np.exp(1/(np.sin(i) + 1)))/(1.25 + 1/(i**15)))/np.log(1 + i**2)
    print(y)
