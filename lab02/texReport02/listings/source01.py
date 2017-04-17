import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq

%matplotlib inline

Fs = 8000 # discrete frequency 
t = np.matrix(np.arange(0.0, 1.0, (1 / Fs))).transpose()
A = 2 # amplitude
f0 = 1000
phi =  np.pi /4 
s1 = A * np.cos(2 *  f0 * t + phi) # harmonic signal
fig = plt.figure(figsize=(6,6))
plt.title('Гармонический сигнал')
plt.plot(t[1:100],s1[1:100])
fig.savefig('pictures/001_1harmonic.png', dpi=200)
plt.show()
N = len(t)
T = 1.0 / Fs
yf = fft(s1)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.title('Амплитудный спектр')
plt.ylim(0, 50)
plt.xlim(-500,500)
plt.plot(xf, np.abs(yf))
fig.savefig('pictures/001_2harmspectr.png', dpi=70)
plt.show()