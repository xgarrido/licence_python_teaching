import particle

# Create an empty list of particles
particles = []
particles.append(particle.Particle("electron", 511e3, -1.6e-19))
particles.append(particle.Particle("muon", 155e6, -1.6e-19))
particles.append(particle.Particle("proton", 939e6, +1.6e-19))

for p in particles:
    print(p)
