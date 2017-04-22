def heaviside(x):
    return 0.5 * (np.sign(x) + 1)

import numpy as np
x = np.linspace(-10, 10, 100)

import matplotlib.pyplot as plt
plt.plot(x, heaviside(x))
plt.xlabel(r"$x$")
plt.ylabel(r"$\Theta(x)$")

plt.show()
