import particle
import numpy as np
import math
import matplotlib.pyplot as plt

theta = float(input("Launch angle in degrees?: "))*math.pi/180.0
r = np.array([0.0, 0.0])
v = np.array([25.0*math.cos(theta), 25.0*math.sin(theta)])
a = np.array([0.0, -9.8])
p = particle.particle(10.0, r, v, a)
dt = 0.06

x = np.zeros(100)
y = np.zeros(100)
t = np.zeros(100)

for i in range(1,100):
    if (p.r[1] < 0):
        break
    p.velVerlet(dt)
    x[i] = p.r[0]
    y[i] = p.r[1]
    t[i] = t[i - 1] + dt
    
plt.plot(x,y,"o")
plt.show()
