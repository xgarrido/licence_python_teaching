import numpy as np

data = np.loadtxt("./data/iris.csv", delimiter=",")

sepal_length = data[:, 0]
sepal_width  = data[:, 1]
petal_length = data[:, 2]
petal_width  = data[:, 3]
species      = data[:, 4]

# Distributions des longueurs
import matplotlib.pyplot as plt

style = dict(histtype="stepfilled", alpha=0.5, bins=20)

iris = {0 : "iris setosa", 1 : "iris versicolor", 2 : "iris virginica"}
labels = {"longueur des sépales [cm]" : sepal_length,
          "largeur des sépales [cm]"  : sepal_width,
          "longueur des pétales [cm]" : petal_length,
          "largeur des pétales [cm]"  : petal_width}

for xlabel, data in labels.items():
    # Determine best range and bin probability
    r=(np.min(data), np.max(data))
    plt.figure()
    for key, name in iris.items():
        d = data[species == key]
        w = np.ones_like(d)/len(d)
        plt.hist(d, **style, label=name, range=r, weights=w)
        plt.xlabel(xlabel)
        plt.ylabel("probabilité")
        plt.legend()

# Diagrammes longueur vs. largeur sépales
plt.figure()
plt.scatter(sepal_length, sepal_width, s=100*petal_width,
            c=species, cmap="viridis", alpha=0.2)
plt.xlabel("longueur des sépales [cm]")
plt.ylabel("largeur des sépales [cm]")

# Création d'une légende à partir d'un scatter plot vide
color = plt.cm.get_cmap("viridis")
for key, name in iris.items():
    rgba = color(key/2)
    plt.scatter([], [],c=rgba, alpha=0.2, label=name)
    plt.legend()

# Changement de taille de police uniquement pour cette figure
with plt.rc_context({"font.size": 5}):
      # Définition d'une grille de sous-figures
      fig, ax = plt.subplots(len(labels), len(labels),
                             sharex="col", sharey="row",
                             figsize=(1.5*len(labels), 1.5*len(labels)))

      for l1, d1 in labels.items():
            i1 = list(labels.keys()).index(l1)
            for l2, d2 in labels.items():
                  i2 = list(labels.keys()).index(l2)
                  for key, name in iris.items():
                        sc = (species == key)
                        if l1 == l2:
                              ax[i1, i2].hist(d1[sc], alpha=0.5, bins=10, normed=True)
                        else:
                              ax[i1, i2].scatter(d2[sc], d1[sc], s=5, alpha=0.5)
                              ax[-1, i1].set_xlabel(l1)
                              ax[i1, 0].set_ylabel(l1)

      # Création d'une légende à partir d'un scatter plot vide
      for key, name in iris.items():
            plt.scatter([], [], label=name)
            plt.legend(title="iris", bbox_to_anchor=(1, len(iris)/2+1), loc="upper left")
            fig.subplots_adjust(right=0.9)
plt.show()
