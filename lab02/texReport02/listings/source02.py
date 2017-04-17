
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftfreq


# rectangular impulse
def rect_impls_1(t, width): 
	sig = np.zeros(len(t))
	for i in sig:
		if -width/2 <= i < width / 2:
			i = 1
	for i in range(len(sig)):
		if -width/2 <= t[i] < width / 2:
			sig[i] = 1
	return sig

Fs = 800 
t = np.linspace(-1, 1, 2 * Fs)
witdh = 0.5 
fig = plt.figure()
y = rect_impls_1(t, witdh)
plt.plot(t,y)
plt.title('Прямоугольный импульс')
fig.savefig('pictures/002_1rectImpl.png', dpi=100)
plt.show()
N = len(t)
T = 1.0 / Fs
yf = fft(y)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.title('Амплитудный спектр')
plt.ylim(0, 200)
plt.xlim(-70, 70)
plt.plot(xf, np.abs(yf)) 
fig.savefig('pictures/002_2rectImplSpectr.png', dpi=100)
plt.show()