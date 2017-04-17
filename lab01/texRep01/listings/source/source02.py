import numpy as np
import matplotlib.pyplot as plt

def elem_multiple(a, b):
	if a.shape != b.shape:
		raise IOError("Shapes of matrices are not the same")
		return
	else:
		res = np.zeros(a.shape)
		for i in range(a.shape[0]):
			for j in range(a.shape[1]):
				res[(i,j)] = a[(i,j)] * b[(i,j)]
		# print(res.shape)
		return res
     
Fs = 8000 # discrete frequency 
t = np.matrix(np.arange(0.0, 1.0, (1 / Fs))).transpose()
f0 = 1000
phi =  np.pi /4 
alpha = 1000
s2 = elem_multiple(s1, np.exp(-alpha * t))
fig = plt.figure(figsize=(6,6))
plt.title('Затухающий сигнал')
plt.plot(t[1:100],s2[1:100])
fig.savefig('picturesNote/002harmonic.png', dpi=100)
plt.show()
