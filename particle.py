import numpy as np
 
class particle:
    def __init__(self, mass, r, v, a):
        self.r = r
        self.v = v
        self.m = mass
        self.a = a
         
    def updatePos(self, dt):
        self.r = self.r + self.v*dt + 0.5*self.a*dt
        
    def updateVel(self, dt):
        self.v = self.v + self.a*dt
        
    def velVerlet(self, dt):
        self.updateVel(0.5*dt)
        self.updatePos(dt)
        self.updateVel(0.5*dt)
