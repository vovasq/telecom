import numpy as np
import math
import matplotlib.pyplot as plt

from scipy import signal
from scipy.fftpack import fft, fftfreq
from scipy import special




# function that multiple matrices with same size by the elements
# a = [1, 2], b = [3, 4] res of function = [1*3, 4*2]
# this is all about '.*' operation in Matlab
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

# this is all about '^*' operation in Matlab
def elem_pow(a, b):
	if a.shape != b.shape:
		raise IOError("Shapes of matrices are not the same")
		return
	else:
		res = np.zeros(a.shape)
		for i in range(a.shape[0]):
			for j in range(a.shape[1]):
				res[(i,j)] = a[(i,j)] ** b[(i,j)]
		# print(res.shape)
		return res

# some basics from DSP
def dsp_basics():
	Fs = 8000 # discrete frequency 
	# t = np.array(range(0,1, 1 / Fs))
	t = np.matrix(np.arange(0.0, 1.0, (1 / Fs))).transpose()

	A = 2 # amplitude
	f0 = 1000
	phi =  np.pi /4 
	alpha = 1000

	s1 = A * np.cos(2 * np.pi *  f0 * t + phi) # harmonic signal
	print(s1.shape)
	print(s1.ndim)
	s2 = elem_multiple(s1, np.exp(-alpha * t))

	fig = plt.figure()

	plt.subplot(2,1,1)
	plt.xticks([])
	# plt.yticks([])
	plt.title('Гармонический сигнал')
	plt.plot(t[1:200],s1[1:200])

	plt.subplot(2,1,2)
	# plt.xticks([])
	# plt.yticks([])
	plt.title('Затухающий сигнал')

	plt.plot(t[1:200],s2[1:200])
	fig.savefig('pictures/001_commons.png', dpi=200)
	
#introduces  multichannel signal
def mlt_chnl():
	
	Fs = 8000 # discrete frequency 
	# t = np.array(range(0,1, 1 / Fs))
	t = np.matrix(np.arange(0.0, 1.0, (1 / Fs))).transpose()
	f = np.matrix([600, 800, 1000, 1200, 1400])
	print(f)
	s3 = np.matrix(np.cos(2*np.pi * t * f)) # 5 channels signal
	# print(s3[1:10])
	fig = plt.figure()
	print(s3.shape)
	plt.title('5-канальный сигнал')
	plt.plot(t[1:100], s3[1:100])
	fig.savefig('pictures/002_5chnls.png', dpi=200)
	# plt.show()

# rectangular impulse
def rect_impls_1(t, width): #t,width
	sig = np.zeros(len(t))
	for i in sig:
		if -width/2 <= i < width / 2:
			i = 1
	for i in range(len(sig)):
		if -width/2 <= t[i] < width / 2:
			sig[i] = 1

	# print(sig)
	# fig = plt.figure()
	# plt.title('Прямоугольный импульс')
	# plt.plot(t,sig)
	# plt.show()
	return sig



def rect_impls():
	Fs = 1000 # discrete frequency
	t = np.matrix(np.arange(-0.4, 0.8, (1 / Fs))).transpose()
	A = 5 
	duty = np.zeros(t.shape)
	for i in range(len(duty)):
		if  500 < i < 600:
			duty[i] = 1 
	fig = plt.figure()
	plt.subplot(2,1,1)
	plt.title('Прямоугольные импульсы')
	plt.plot(t, signal.square(2 * np.pi * 5 * t, duty))
	plt.ylim(-2, 2)

	plt.subplot(2,1,2)
	plt.plot(t, signal.square( 2 * np.pi * 5 * t, 0.1))
	plt.ylim(-2, 2)
	fig.savefig('pictures/003_rect_impls.png', dpi=100)
	# plt.show()

# gauss impulse and spectrum
def gaus_impls():
	Fs = 800 
	t = np.linspace(-1, 1, 2 * Fs)
	i, e = signal.gausspulse(t, fc=5, retenv=True)
	fig = plt.figure()
	plt.plot(t, i, t, e, '--')
	plt.title('Гауссов импульс')
	fig.savefig('pictures/004_gaus.png', dpi=100)
	# plt.show()
	N = len(t)
	Fs = 800
	T = 1.0 / Fs
	x = t #np.linspace(0.0, N*T, N)
	y = i #np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
	yf = fft(y)
	xf = fftfreq(N, 1.0 / Fs)
	fig = plt.figure()
	plt.title('Амплитудный спектр')
	plt.plot(xf, np.abs(yf)) #int(N/4):int(3*N/4)
	plt.grid()
	fig.savefig('pictures/005_spctrgaus.png', dpi=100)

	# plt.show()

# triangle also sawtooth signal
def triangle_impls():
	Fs = 8000 # discrete frequency 
	t = np.linspace(0, 0.5, Fs)
	fig = plt.figure()
	plt.title('Последовательность треугольных импульсов')
	plt.plot(t, signal.sawtooth(2 * np.pi * 5  * t))
	fig.savefig('pictures/006_sawtooth.png', dpi=100)
	# plt.show()

# diricle function
def dirichle():
	x = np.linspace(-8*np.pi, 8*np.pi, num=201)
	fig = plt.figure(figsize=(8, 8))
	for idx, n in enumerate([7, 8]):
	    plt.subplot(2, 1, idx+1)
	    plt.plot(x, special.diric(x, n))
	    plt.title('Функция Дирихле, n={}'.format(n))
	fig.savefig('pictures/007_dirichle.png', dpi = 200)
	plt.show()



# dsp_basics()
# mlt_chnl()
# rect_impls()
# gaus_impls()
# triangle_impls()
# dirichle()

Fs = 1000
t = np.matrix(np.arange(-0.84, 0.84, (1 / Fs))).transpose()
width = 0.2
A = 5
s = -A *rect_impls_1(t + width / 2, width) + A * rect_impls_1(t - width / 2 ,width)
fig = plt.figure()
plt.title('Прямоугольный импульс')
plt.plot(t,s)
plt.show()