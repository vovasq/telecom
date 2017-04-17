import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq

Fs = 800 
t = np.linspace(-1, 1, 2 * Fs)
i, e = signal.gausspulse(t, fc=5, retenv=True)
fig = plt.figure()
plt.plot(t, i, t, e, '--')
plt.title('Гауссов импульс')
fig.savefig('picturesNote/005_gaus.png', dpi=70)
plt.show()
N = len(t)
Fs = 800
T = 1.0 / Fs 
y = i 
yf = fft(y)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.title('Амплитудный спектр')
plt.plot(xf[1:800], np.abs(yf[1:800])) 
fig.savefig('picturesNote/006_spctrgaus.png', dpi=70)
plt.show()