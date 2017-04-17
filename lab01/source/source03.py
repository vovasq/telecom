import numpy as np
import matplotlib.pyplot as plt


Fs = 40000 # discrete frequency 
t = np.matrix(np.arange(0.0, 1.0, (1 / Fs))).transpose()
f = np.matrix([600, 800, 1000, 1200, 1400])

s3 = np.matrix(np.cos(2*np.pi * t * f)) # 5 channels signal

fig = plt.figure(figsize=(8, 8))
plt.title('5-канальный сигнал')
plt.plot(t[1:50], s3[1:50])
fig.savefig('picturesNote/003_5chnls.png', dpi=200)
plt.show()