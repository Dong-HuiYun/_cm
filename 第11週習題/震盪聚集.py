import numpy as np
import matplotlib.pyplot as plt

# 建立接近 0 的點
t = np.linspace(0.005, 0.1, 1000)
y = np.sin(1/t)

plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title(r'Oscillations of $f(t) = \sin(1/t)$ near $t=0$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.show()