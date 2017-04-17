

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

Fs = 1000 # discrete frequency
t = np.linspace(-1, 1, 2 * Fs)
A = 5         
fig = plt.figure()
y = A * signal.square( 2 * np.pi * 5 * t, 0.2)
plt.plot(t, y)
# fig.savefig('pictures/003_1rectImplses.png', dpi=100)
plt.show()
N = len(t)
T = 1.0 / Fs
yf = fft(y)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.title('Амплитудный спектр')
# plt.ylim(0, 200)
plt.xlim(-70, 70)
plt.plot(xf, np.abs(yf)) 
# fig.savefig('pictures/003_2rectImplSpectr.png', dpi=100)
plt.show()