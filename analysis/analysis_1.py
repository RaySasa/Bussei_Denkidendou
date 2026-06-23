#導体の電気抵抗

import numpy as np
import matplotlib.pyplot as plt

#電流と電圧
I = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
V2 = np.array([-8.98, -8.21, -7.00, -5.17, -2.76, -0.00067, 2.55, 4.54, 6.05, 7.13, 7.87])
V4 = np.array([-3.50, -3.21, -2.74, -2.03, -1.09, 0.000268, 1.09, 2.02, 2.74, 3.26, 3.62])

plt.scatter(I, V2)
plt.show()

plt.scatter(I, V4)
plt.show()