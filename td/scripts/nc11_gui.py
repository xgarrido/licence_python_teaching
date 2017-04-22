import numpy as np

# Définition des constantes du problème
ni  = 3e8   # noyaux/s
T12 = 20.36 # min
t0  = 3     # hours

def n(t, ni=ni, t0=t0, T12=T12):
    T12 /= 60  # hours
    ni *= 3600 # noyaux/h
    l = np.log(2)/T12
    conds = [t <= t0, t > t0]
    funcs = [lambda t: ni/l*(1-np.exp(-l*t)),
             lambda t: ni/l*(1-np.exp(-l*t0))*np.exp(-l*(t-t0))]
    return np.piecewise(t, conds, funcs)

t = np.linspace(0, 10, 1000) #hours

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
l, = plt.plot(t, n(t))
plt.xlabel("temps [heures]")
plt.ylabel(r"$n(^{11}\mathrm{C})$")

# Définition des sous-figures où afficher les sliders
axni  = plt.axes([0.25, 0.10, 0.65, 0.03])
axt12 = plt.axes([0.25, 0.15, 0.65, 0.03])
axt0  = plt.axes([0.25, 0.20, 0.65, 0.03])

plt.subplots_adjust(bottom=0.35)

from matplotlib.widgets import Slider
sni = Slider(axni, r"$n_i [\times10^8]\mathrm{/s}$", 1, 10, valinit=ni/1e8)
st12 = Slider(axt12, r"$T_{1/2}$ [min]", 1, 60, valinit=T12)
st0 = Slider(axt0, r"$t_{0}$ [h]", 1, 10, valinit=t0)

def update(val):
    nx = n(t, sni.val*1e8, st0.val, st12.val)
    l.set_ydata(nx)
    ax.set_ylim(ax.get_ylim()[0], 1.1*np.max(nx))
    fig.canvas.draw_idle()

sni.on_changed(update)
st12.on_changed(update)
st0.on_changed(update)

plt.show()
