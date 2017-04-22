import euler_project as ep

# To generate random integer values
from numpy.random import randint

for key, fcn in ep.projects.items():
    n = randint(1000)
    print("Testing Euler project n°{} with value n={}".format(key, n))
    print("-> Solution = {}".format(str(fcn(n))))
