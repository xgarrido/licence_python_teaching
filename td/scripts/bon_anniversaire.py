%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6,8))
plt.subplots_adjust(bottom=0.25, left=0.25)

distance = 4 # a.l

def trajectory(beta=4/5):
    x = [0, distance, 0]
    y = [0, distance/beta, 2*distance/beta]
    return x, y

x, y = trajectory(beta=4/5)
l, = plt.plot(x, y, "-o")

plt.plot([0, 2*distance], [0, 2*distance], "--", color="C3")
plt.xlim(0, 2*distance)
plt.ylim(0, 10)
plt.xlabel(r"$x^1$ = distance [a.l.]")
plt.ylabel(r"$x^0 = ct$ [années]")
plt.text(distance*1.75, distance*1.80, "cône de lumière", color="C3", rotation=45, ha="center", va="center")
plt.fill_between([0, 2*distance], [0, 2*distance], color="lightgray")
plt.yticks(np.arange(11))
plt.grid()

def update(val):
    x, y = trajectory(val)
    l.set_ydata(y)
    fig.canvas.draw_idle()

# Définition des sous-figures où afficher les sliders
axbeta = plt.axes([0.25, 0.10, 0.65, 0.03])
from matplotlib.widgets import Slider
sbeta = Slider(axbeta, r"$\beta$", 0, 1, valinit=4/5)
sbeta.on_changed(update)

plt.show()
