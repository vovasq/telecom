
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.fftpack import fft, fftfreq, ifft


sig = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0])
parcel = np.array([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
sigF = fft(sig)
parcelF = fft(parcel)
corr_fast = ifft(sigF * parcelF.conjugate()) / len(sig)
corr_fast = corr_fast.real

print('Fast correlation')
print(len(corr_fast))
for i in corr_fast: 
    print('{0:2.4f}'.format(i), end=' ')
    
corr = signal.correlate(sig, parcel, mode='same') / len(sig)    
print('\nUsual corrrelation')
print(len(corr))
for i in corr: print('{0:2.4f}'.format(i), end=' ')