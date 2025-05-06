import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = (X - Y) ** 2

fig, ax1 = plt.subplots(subplot_kw = {"projection": "3d"})
ax1.plot_surface(X, Y, Z, cmap = 'viridis')
ax1.set_title('MSE (Normal Scale)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

fig, ax2 = plt.subplots(subplot_kw = {"projection": "3d"})
Z_log = np.log1p(Z)
ax2.plot_surface(X, Y, Z_log, cmap = 'plasma')
ax2.set_title('MSE (Log Scale)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(Z)')

plt.tight_layout()
plt.show()