import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import special


x = np.linspace(-8*np.pi, 8*np.pi, num=201)
fig = plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(x, special.diric(x, 7))
plt.title('Функция Дирихле, n={}'.format(7))
plt.subplot(2, 1, 2)
plt.plot(x, special.diric(x, 8))
plt.title('Функция Дирихле, n={}'.format(8))
fig.savefig('pictures/009_dirichle.png', dpi = 200)
plt.show()