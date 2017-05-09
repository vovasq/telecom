# tasks 1, 2, 3

# 42a31d9ca0c60be06316882941d994df575848a63275c84f
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

% matplotlib inline


def sig_modulation(m, t, picname):
    # phi = 0.43 * np.pi
    #i = 0.43 * np.pi
    #A_m = 5 
    #modulation depth 

    # 0.75
    F_m = 1
    s_m = np.cos( F_m* 2 * np.pi * t) 
                      # + phi)
    # carrier signal
    f_c = 20 
#     phi_c = 0.7 * np.pi
    s_c = np.cos(f_c * 2 * np.pi * t) 
                 # + phi_c)
    A_0 = 3

    # modulation
    s_am = A_0 * (1 + m * s_m) * s_c

    fig = plt.figure()
    s = 'Depth = ' + str(m) 
    plt.title(s)
    plt.plot(t, s_am)
    fig.savefig('pictures/' + picname + 'sig.png', dpi=100)
    plt.show()

    # spectrus
    N = len(t)
    T = 1.0 / Fs
    s_amf = fft(s_am)
    xf = fftfreq(N, 1.0 / Fs)
    fig = plt.figure()
    plt.title(s)
    plt.xlim(0, 60)
    plt.ylim(0, 270)
    plt.grid()
    plt.plot(xf, np.abs(s_amf)) 
    fig.savefig('pictures/' + picname + 'spec.png', dpi=100)
    plt.show()

# discrete frequency
Fs = 100
t = np.linspace(-1, 1, 2 * Fs)
sig_modulation(0, t, '001_d0')
sig_modulation(0.5, t, '002_d5')
sig_modulation(1, t, '003_d1')
sig_modulation(2, t, '004_d2')