import numpy as np
import matplotlib.pyplot as plt

# 定義方波 (有限間斷點)
t = np.linspace(-2*np.pi, 2*np.pi, 1000)
f_t = np.sign(np.sin(t))

# 模擬傅立葉級數逼近 (吉布斯現象)
def fourier_series(t, n_terms):
    s = np.zeros_like(t)
    for n in range(1, n_terms + 1, 2):
        s += (4 / (np.pi * n)) * np.sin(n * t)
    return s

plt.plot(t, f_t, label='Original Square Wave')
plt.plot(t, fourier_series(t, 20), label='Fourier Series (n=20)')
plt.title("Square Wave with Finite Discontinuities")
plt.legend()
plt.show()