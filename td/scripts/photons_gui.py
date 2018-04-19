import numpy as np
def f(theta, beta):
      return (1-beta**2)/(1-beta*np.cos(theta))**2

r = np.arange(0, 1, 0.0001)
theta = 2*np.pi*r

import matplotlib.pyplot as plt
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
plt.subplots_adjust(bottom=0.25)

l, = ax.plot(theta, f(theta, beta=0))
ax.set_rticks([])

def update(val):
    y = f(theta, beta=val)
    l.set_ydata(y)
    ax.set_ylim(0, 1.1*np.max(y))
    fig.canvas.draw_idle()

# Définition des sous-figures où afficher les sliders
axbeta = plt.axes([0.15, 0.10, 0.75, 0.03])
from matplotlib.widgets import Slider
sbeta = Slider(axbeta, r"$\beta$", 0, 0.999999, valinit=0)
sbeta.on_changed(update)

plt.show()
