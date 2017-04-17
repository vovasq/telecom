import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

Fs = 1000 # discrete frequency
t = np.matrix(np.arange(-0.4, 0.8, (1 / Fs))).transpose()
A = 5         
fig = plt.figure()
plt.plot(t, A *signal.square( 2 * np.pi * 5 * t, 0.2))
fig.savefig('picturesNote/007rectImplses.png', dpi=100)
plt.show()