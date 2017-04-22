import numpy as np
data = np.loadtxt("./data/higgs-gg.csv", delimiter=",")

x, y, yerr = data.T

import matplotlib.pyplot as plt

grid = plt.GridSpec(4, 1, hspace=0, wspace=0)

main = plt.subplot(grid[0:3], xticklabels=[])
main.errorbar(x, y, yerr=yerr, fmt=".k", label="ATLAS data")
main.set_ylabel(r"Nombre d'événements $H\to\gamma\gamma$")

# "Theoritical model" = 4th order polynomial
def model(x, parameters=[6.527e4, -1208.9, 7.697, -1.668e-2]):
    y = 0.0
    for i, p in enumerate(parameters):
        y += p*np.power(x, i)
    return y

xmodel = np.linspace(105, 160, 100)
main.plot(xmodel, model(xmodel), "-r", label="modèle polynomial")

# Plot deviation
sub = plt.subplot(grid[3])
dev = (y - model(x))/yerr
sub.errorbar(x, dev, fmt=".k")
sub.set_ylabel(r"$\frac{y-y_\mathrm{modèle}}{\sigma}$ [$\sigma$]")
sub.set_xlabel(r"$m_{\gamma\gamma}$ [MeV]")

# Calculate chi2/ndf and add it to legend
chi2n = np.sum(dev**2)/(len(dev)-4)
main.plot([], [], linestyle="None", label=r"$\chi^2/$ndf = {0:.2f}".format(chi2n))
main.legend()

mask = (dev > 3)
sub.scatter(x[mask], dev[mask], edgecolors="red", c="none", s=100)

print("Masse du boson de Higgs = {} GeV".format(x[mask][0]))

# Fit with a 4th order polynomial
parameters = np.polyfit(x, y, 3)
fit = np.poly1d(parameters)
print("Best parameters : " + str(parameters))

plt.show()
