import numpy as np
import matplotlib.pyplot as plt

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

Fs = 1000
t = np.matrix(np.arange(-0.84, 0.84, (1 / Fs))).transpose()
width = 0.2
A = 5
s = -A *rect_impls_1(t + width / 2, width) + A * rect_impls_1(t - width / 2 ,width)
plt.title('Прямоугольный импульс')
plt.plot(t,s)
plt.gcf().savefig('picturesNote/004rectImp.png', dpi=100)
plt.show()