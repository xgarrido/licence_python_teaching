class Particle:
    def __init__(self, name=None, mass=None, charge=None):
        self.name = name
        self.mass = mass
        self.charge = charge
    def __str__(self):
        return "Particle name {}, mass = {} eV and electric charge = {} C".format(self.name,
                                                                                  self.mass,
                                                                                  self.charge)
