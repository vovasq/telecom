#task 5
# % matplotlib inline
# why we get a moved signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
from scipy.signal import butter, lfilter, freqz

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y



# discrete frequency
Fs = 300
t = np.linspace(0.1, 1, 2 * Fs)

# depth 
m = 0.75

# signal
phi = 0.43 * np.pi
f_m = 3
s_m = m * np.cos(f_m * 2 * np.pi * t) #+ phi)

# carrier signal
f_c = 20 
# phi_c = 0.7 * np.pi
s_c = np.cos(f_c * 2 * np.pi * t) 
#              + phi_c)

# single side modulation
U_m = 0.5
s_am = U_m * s_m * s_c + 0.5 * m * U_m  * (np.cos((f_c + f_m)* t)  + phi_c)  
vovas = U_m * s_m * s_c
fig = plt.figure()
plt.plot(t, s_am)
#     fig.savefig('pictures/004_signal.png', dpi=100)
plt.show()

# spectrus
N = len(t)
T = 1.0 / Fs
s_amf = fft(s_am)
xf = fftfreq(N, 1.0 / Fs)
fig = plt.figure()
plt.xlim(-20, 20)
plt.ylim(0, 27)
plt.grid()
plt.plot(xf, np.abs(s_amf))
#     fig.savefig('pictures/004_spectr.png', dpi=100)
plt.show()

# demodulation
# multiplication with carrier
# fig = plt.figure()
# plt.title('multiple res')
# plt.plot(t, s_d)
# plt.show()

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

order = 5
# s_d = s_am * s_c
s_d = vovas * s_c
# b, a = butter(order, )

# nyq = 0.5 * fs
# normal_cutoff = cutoff / nyq
# b, a = butter(order, normal_cutoff, btype='low', analog=False)
# y = lfilter(b, a, data)



# cutoff = 1.5
# for cutoff in frange(0, 4, 0.2):
#     full_dem = butter_lowpass_filter(s_d, cutoff, f_m, order)
b, a = butter(order+1, 2*f_m  / Fs, btype='low', analog=False)
full_dem =  4 * lfilter(b, a, s_d)

fig = plt.figure()
plt.plot(t, full_dem, 'g-')
plt.plot(t, s_m, 'b-')
plt.show()
