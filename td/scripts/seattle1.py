import numpy as np

def print_report(prcp, Tmin, Tmax):

    print("Hauteur des précipitations:")
    print("  valeur moyenne = {} cm".format(np.mean(prcp)))
    print("  valeur médiane = {} cm".format(np.median(prcp)))
    print("      écart type = {} cm".format(np.std(prcp)))
    print("     valeur min. = {} cm".format(np.min(prcp)))
    print("     valeur max. = {} cm".format(np.max(prcp)))
    print("  quantile à 25% = {} cm".format(np.percentile(prcp, 25)))
    print("  quantile à 75% = {} cm".format(np.percentile(prcp, 75)))
    print("\n")

    print("Température minimale:")
    print("  valeur moyenne = {} °C".format(np.mean(Tmin)))
    print("  valeur médiane = {} °C".format(np.median(Tmin)))
    print("      écart type = {} °C".format(np.std(Tmin)))
    print("     valeur min. = {} °C".format(np.min(Tmin)))
    print("     valeur max. = {} °C".format(np.max(Tmin)))
    print("  quantile à 25% = {} °C".format(np.percentile(Tmin, 25)))
    print("  quantile à 75% = {} °C".format(np.percentile(Tmin, 75)))
    print("\n")

    print("Température maximale:")
    print("  valeur moyenne = {} °C".format(np.mean(Tmax)))
    print("  valeur médiane = {} °C".format(np.median(Tmax)))
    print("      écart type = {} °C".format(np.std(Tmax)))
    print("     valeur min. = {} °C".format(np.min(Tmax)))
    print("     valeur max. = {} °C".format(np.max(Tmax)))
    print("  quantile à 25% = {} °C".format(np.percentile(Tmax, 25)))
    print("  quantile à 75% = {} °C".format(np.percentile(Tmax, 75)))
    print("\n")

data = np.loadtxt("./data/seattle2014.csv", delimiter=",")

day = data[:,0]
prcp = data[:,1]/100 # cm
Tmax = data[:,2]/10  # °C
Tmin = data[:,3]/10  # °C

print("* Valeurs annuelles")
print_report(prcp, Tmin, Tmax)

print("* Valeurs estivales")
summer = (day > 20140401) & (day < 20140930)
print_report(prcp[summer], Tmin[summer], Tmax[summer])

print("Hauteur totale d'eau en 2014 : {} cm".format(np.sum(prcp)))
print("Nombre de jours avec pluie : {}".format(np.sum(prcp > 0)))
print("Nombre de jours pairs avec pluie : {}".format(np.sum((prcp > 0) & (day % 2 == 0))))

import matplotlib.pyplot as plt
plt.hist(prcp, 40)

plt.show()
