

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 8000 # discrete frequency 
t = np.linspace(0, 0.5, Fs)
fig = plt.figure()
plt.title('Последовательность треугольных импульсов')
y = signal.sawtooth(2 * np.pi * 8  * t)
plt.plot(t, y)
fig.savefig('pictures/004_1sawtooth.png', dpi=100)
plt.show()
N = len(t)
T = 1.0 / Fs
yf = fft(y)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.title('Амплитудный спектр')
# plt.ylim(0, 200)
# plt.xlim(-70, 70)
plt.xlim(-10, 10)
plt.plot(xf, np.abs(yf)) 
fig.savefig('pictures/004_2sawToothSpectr.png', dpi=100)
plt.show()