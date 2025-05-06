import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

a = 1
frames = 100
t = np.linspace(0, 2 * np.pi)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Вращающаяся фигура Лиссажу")
line, = ax.plot([], [])

def init():
    line.set_data([], [])
    return line,
def lisajous_curve_animate(f):
    b = f / frames
    x = np.sin(a * t)
    y = np.sin(b * t)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, lisajous_curve_animate, frames = frames, init_func = init, blit = True, interval = 100)

plt.show()
