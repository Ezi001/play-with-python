import numpy as np
import matplotlib.pyplot as plt

N = 64
n = np.arange(N)

x_1 = 64*np.cos(2*np.pi*15*n/N)
x_2 = 32* 0.5*np.cos(2*np.pi*27*n/N)


plt.plot(n, np.abs(np.fft.fft(x_1 + x_2)), "o-")
plt.title("x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()