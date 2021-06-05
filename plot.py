import matplotlib.pyplot as plt
import numpy as np
a = np.arange(0.0, 5.0, 0.04)
b = 1 + np.cos(2 * np.pi * a)

fig, ax = plt.subplots()
ax.plot(a, b)

ax.set(xlabel='put your label here', ylabel='put your y label here',
       title='simple plot of cos graph with grid')
ax.grid()
plt.show()
