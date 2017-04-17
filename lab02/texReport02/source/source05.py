
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import special

Fs = 8000
t = np.linspace(-8*np.pi, 8*np.pi, Fs)
# fig = plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
y1 = special.diric(t, 7)
plt.plot(t,y1)
plt.title('Функции Дирихле, n={}, n={}'.format(7,8))
plt.subplot(2, 1, 2)
y2 = special.diric(t, 8)
plt.plot(t, y2)
# plt.title('Функция Дирихле, n={}'.format(8))
fig.savefig('pictures/005_1dirichle.png', dpi = 200)
plt.show()

N = len(t)
T = 1.0 / Fs
yf1 = fft(y1)
yf2 = fft(y2)
xf = fftfreq(N, 1.0 / Fs)


fig = plt.figure()
plt.subplot(2, 1, 1)
plt.xlim(-100,100)
plt.plot(xf, np.abs(yf1))
plt.title('Спектры Функции Дирихле, n={}, n={}'.format(7,8))
plt.subplot(2, 1, 2)
plt.plot(xf, np.abs(yf2))
plt.xlim(-100,100)
# plt.title('Функция Дирихле, n={}'.format(8))
fig.savefig('pictures/005_2dirichleSpectr.png', dpi = 200)
plt.show()