import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 8, 0.1)
y = np.cos(x) * x
plt.plot(x, y)
plt.axis([0, 10, -8, 8])
plt.show()
