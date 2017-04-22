import numpy as np
data = np.loadtxt("./data/seattle2014.csv", delimiter=",")

day  = data[:,0]
prcp = data[:,1]/100 # cm
Tmax = data[:,2]/10  # °C
Tmin = data[:,3]/10  # °C

import matplotlib.pyplot as plt
plt.hist(prcp, 365)

plt.title("Distribution des précipitations à Seattle en 2014")
plt.xlabel("hauteur des précipitations [cm]")
plt.ylabel("nombre de jours")

plt.yscale("log")
# Remove exponential notation
from matplotlib.ticker import ScalarFormatter
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

# Affiche valeur moyenne et écart type
mean = np.mean(prcp)
std  = np.std(prcp)

ymin, ymax = plt.gca().get_ylim()
plt.annotate(r"$\mu$ = {0:.2f} $\pm$ {1:.2f} cm".format(mean, std),
             xy=(mean, ymin), xytext=(mean, 10),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Variation des températures minimale et maximale au cours de l'année 2014
import pandas as pd
day = pd.to_datetime(day, format="%Y%m%d")

plt.figure()
plt.plot(day, Tmin, label=r"T$_\mathrm{min.}$")
plt.plot(day, Tmax, label=r"T$_\mathrm{max.}$")
plt.title("Variation de la température à Seattle en 2014")
plt.ylabel("température [°C]")
plt.legend(loc="lower center", ncol=2)

# Distributions normalisées des températures minimale et maximale
plt.figure()
kwargs = dict(histtype="stepfilled", alpha=0.5, bins=40, range=(-10, 40))
plt.hist(Tmin, label=r"T$_\mathrm{min.}$", **kwargs, weights=np.ones_like(Tmin)/len(Tmin))
plt.hist(Tmax, label=r"T$_\mathrm{max.}$", **kwargs, weights=np.ones_like(Tmax)/len(Tmax))
plt.xlabel("température [°C]")
plt.ylabel("probabilité")
plt.legend(loc="upper center", ncol=2)

# Show everything !
plt.show()
