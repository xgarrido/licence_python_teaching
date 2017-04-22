import numpy as np

# Définition des constantes du problème
ni  = 3e8*3600  # noyaux/h
T12 = 20.36/60  # hours
l   = np.log(2)/T12

def carbon11(t, t0):
    conds = [t <= t0, t > t0]
    funcs = [lambda t: ni/l*(1-np.exp(-l*t)),
             lambda t: ni/l*(1-np.exp(-l*t0))*np.exp(-l*(t-t0))]
    return np.piecewise(t, conds, funcs)

t0 = 3 # hours
t  = np.linspace(0, 10, 1000)
n  = carbon11(t, t0)

import matplotlib.pyplot as plt
plt.plot(t, n)
plt.xlabel("temps [heures]")
plt.ylabel(r"$n(^{11}\mathrm{C})$")

plt.show()
