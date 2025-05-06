import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure()
plt.subplots_adjust(bottom = 0.3, hspace = 0.7)

ax1 = plt.subplot(311)
x = np.linspace(0, 4 * np.pi, 1000)
wave1, = ax1.plot(x, np.sin(x))
ax1.set_title('Волна 1', fontsize = 11)
ax1.set_ylim(-5, 5)

ax2 = plt.subplot(312)
wave2, = ax2.plot(x, np.sin(x))
ax2.set_title('Волна 2', fontsize = 11)
ax2.set_ylim(-5, 5)

ax3 = plt.subplot(313)
result_wave, = ax3.plot(x, np.sin(x) + np.sin(x))
ax3.set_title('Результат сложения', fontsize = 11)
ax3.set_ylim(-5, 5)


ax_amp1 = plt.axes([0.2, 0.2, 0.65, 0.03])
ax_freq1 = plt.axes([0.2, 0.15, 0.65, 0.03])

amp_slider1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 3.0)
freq_slider1 = Slider(ax_freq1, 'Частота 1', 0.1, 3.0)

ax_amp2 = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_freq2 = plt.axes([0.2, 0.05, 0.65, 0.03])

amp_slider2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 3.0)
freq_slider2 = Slider(ax_freq2, 'Частота 2', 0.1, 3.0)

def update(val):
    amp1 = amp_slider1.val
    freq1 = freq_slider1.val
    amp2 = amp_slider2.val
    freq2 = freq_slider2.val
    
    wave1.set_ydata(amp1 * np.sin(freq1 * x))
    wave2.set_ydata(amp2 * np.sin(freq2 * x))
    result_wave.set_ydata(amp1 * np.sin(freq1 * x) + amp2 * np.sin(freq2 * x))
    
    fig.canvas.draw_idle()

amp_slider1.on_changed(update)
freq_slider1.on_changed(update)
amp_slider2.on_changed(update)
freq_slider2.on_changed(update)

plt.show()