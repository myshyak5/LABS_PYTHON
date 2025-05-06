import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre

x = np.linspace(-1, 1)
fig, ax = plt.subplots()

for n in range(1, 8):
    Pn = legendre(n)
    y = Pn(x)
    ax.plot(x, y, label = f'n = {n}')

ax.set_title("Полиномы Лежандра")

plt.legend()
plt.show()