import pandas as pd

data = pd.read_csv("data/planets.csv")

years = data["year"].values
methods = data["method"].values
orbital_period = data["orbital_period"].values
distance = data["distance"].values

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.hist(years[years == 2005], align="left")

# Total distribution of planets per year
plt.figure()
plt.hist(years, align="left", range=(1990, 2015), bins=25)
plt.ylabel("nombre de planètes extrasolaires")
plt.xticks(np.arange(1990, 2015), fontsize=10, rotation=90)
plt.grid()

# Distribution of planets discovered per year and per method
plt.figure()
for idx, method in enumerate(np.unique(methods)):
    h, bins = np.histogram(years[methods == method], range=(1990, 2015), bins=25)
    plt.bar(bins[:-1], h, label=method)
    plt.legend()

# Orbital period versus distance
plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0, wspace=0)
main = plt.subplot(grid[:-1, 1:], xticklabels=[], yticklabels=[],
                   xscale="log", yscale="log")

selected_methods = ["Radial Velocity", "Transit"]
for method in selected_methods:
    mask = (methods == method)
    x , y = distance[mask], orbital_period[mask]
    nonan = (~np.isnan(x) & ~np.isnan(y))
    main.plot(x[nonan], y[nonan], "o", alpha=0.5, label=method)
main.legend(ncol=2, bbox_to_anchor=(0.5, 1.05), loc="center")

xlims = main.get_xlim()
x_hist = plt.subplot(grid[-1, 1:], yticklabels=[],
                     xlim=xlims, xscale="log", xlabel=r"distance [light years]")
x_hist.invert_yaxis()

ylims = main.get_ylim()
y_hist = plt.subplot(grid[:-1, 0], xticklabels=[],
                     ylim=ylims, yscale="log", ylabel=r"orbital period [days]")
y_hist.invert_xaxis()

kwargs = dict(alpha=0.5, histtype="stepfilled")
for method in selected_methods:
    mask = (methods == method)
    x , y = distance[mask], orbital_period[mask]
    nonan = (~np.isnan(x) & ~np.isnan(y))
    x_hist.hist(x[nonan], orientation="vertical", **kwargs,
                bins=np.logspace(np.log10(xlims[0]), np.log10(xlims[1]), 50))
    y_hist.hist(y[nonan], orientation="horizontal", **kwargs,
                bins=np.logspace(np.log10(ylims[0]), np.log10(ylims[1]), 50))

plt.show()
