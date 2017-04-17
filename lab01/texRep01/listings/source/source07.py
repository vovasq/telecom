import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 8000 # discrete frequency 
t = np.linspace(0, 0.5, Fs)
fig = plt.figure()
plt.title('Последовательность треугольных импульсов')
plt.plot(t, signal.sawtooth(2 * np.pi * 5  * t))
fig.savefig('picturesNote/008_sawtooth.png', dpi=100)
plt.show()