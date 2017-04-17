
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
from scipy.fftpack import fft, fftfreq

%matplotlib inline

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 6
fs = 30.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)


clear_data  = np.sin(1.2*2*np.pi*t)
mf_noize = 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

fig = plt.figure()
plt.title('Cигнал без шумов')
plt.plot(t, clear_data)
fig.savefig('pictures/001_true_sig.png', dpi=70)
plt.show()


fig = plt.figure()
plt.title('Cигнал без шумов')
clear_dataf = fft(clear_data)
xdataf = fftfreq(n , 1.0 / n)
plt.plot(xdataf, np.abs(clear_dataf))
fig.savefig('pictures/002_true_sig_spec.png', dpi=70)
plt.show()

# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = clear_data + mf_noize

fig = plt.figure()
plt.plot(t, data, 'b-', label='Сигнал с шумами')
plt.plot(t, clear_data, 'g-', linewidth=2, label='Отфильтрованный сигнал ')
plt.grid()
plt.legend()
fig.savefig('pictures/003_signals.png', dpi=70)
plt.show()

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)


fig = plt.figure()
plt.title('Cигнал c шумами')
dataf = fft(data)
xdataf = fftfreq(n , 1.0 / n)
plt.plot(xdataf, np.abs(dataf))
fig.savefig('pictures/004_spctr_noisy_signa.png', dpi=70)
plt.show()

fig = plt.figure()
plt.title('Отфильтрованный сигнал')
yf = fft(y)
xf = fftfreq(n , 1.0 / n)
plt.plot(xf, np.abs(yf))
fig.savefig('pictures/005_spctr_signa.png', dpi=70)
plt.show()