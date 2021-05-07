import abc

import render
from vector3 import *

# This is the master class we will use to represent any planet, sun, etc.
class Celestial_Body(abc.ABC):
    def __init__(self, trajectory, radius, color):
        self.trajectory = trajectory
        self.radius = radius
        self.color = color
    
    def position_at(self, time):
        return self.trajectory.calculate_position_at_time(time)
    
    # render this object at a specific time
    def render(self, camera, time):
        render.draw_circle(camera, self.radius, self.position_at(time))