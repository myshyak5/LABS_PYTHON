import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 600)

def lisajous_curve(a, b, delta = np.pi / 2):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

a_b = [(3, 2), (3, 4), (5, 4), (5, 6)]

for elem in a_b:
    x, y = lisajous_curve(elem[0], elem[1])
    plt.figure()
    plt.plot(x, y)
    plt.axis('equal')
    plt.title(f'Фигура Лиссажу ({elem[0]}:{elem[1]})')

plt.show()