from math import cos, sin, pi

from vector3 import *
from celestial_bodies.trajectories import trajectory
from celestial_bodies.trajectories import rotation

# This class represents circular orbit. Perfectly circular orbit isn't realistic but it's easy to implement for testing and was acceptable before 
# 1609. For simplicity, I won't bother with tilt/eccentrism/Milankovich cycles/etc and will leave that to the ellipsical class 

class Circular(trajectory.Trajectory):
    def __init__(self, orbited, radius, period, phase, rotation):
        self.orbited = orbited # Vector3, represents the celestial body to be orbited by this trajectory
        self.radius = radius # distance from orbited object
        self.period = period # time it takes for a full revolution
        self.phase = phase # sin/cos offset
        self.rotation = rotation

        #function for vertical movement would be radius * cos((2pi*time/period)+phase)
        
        #TODO figure out what unit of time to use
    
    def calculate_position_at_time(self, time):
        x = self.radius * cos(2*pi*time/self.period + self.phase)
        z = self.radius * sin(2*pi*time/self.period + self.phase)
        offset = Vector3(x, 0, z)

        return self.orbited.position_at(time) + offset
    
    def calculate_rotation_at_time(self, time):
        return rotation.rotation_at_time(time)