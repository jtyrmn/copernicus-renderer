from math import sin, cos, pi

from celestial_bodies.trajectories.trajectory import Trajectory
from vector3 import *

# this class will demonstrate an elliptical orbit but won't be scientifically accurate or reliable for predictions
# to how an elliptical orbit would function in reality. It's just to look cool for screenshots

class Ellipse_Mock(Trajectory):
    # don't worry too much about each parameter, they aren't precise anyways
    # eccentricity is a value within [0,1). The closer to one, the more oval-like
    # tilt is rotation around the x-axis, in radians
    def __init__(self, orbited, mean_radius, eccentricity, period, phase, tilt):
        self.orbited = orbited
        self.mean_radius = mean_radius
        self.eccentricity = eccentricity
        self.period = period
        self.phase = phase
        self.tilt = tilt
    
    def calculate_position_at_time(self, time):
        param = 2*pi*time/self.period + self.phase
        x = self.mean_radius * cos(param)
        z = self.mean_radius * sin(param)

        position = Vector3(x,0,z) 
        position = position.rotate(Vector3(self.tilt, 0, 0))

        return position + self.orbited.position_at(time)