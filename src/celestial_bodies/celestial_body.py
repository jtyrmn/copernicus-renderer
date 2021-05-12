import abc

import render
from vector3 import *
from copy import deepcopy

# This is the master class we will use to represent any planet, sun, etc.
# trajectory is a Trajectory subclass' object
# color is a 3-element tuple, not Vector3
class Celestial_Body(abc.ABC):
    def __init__(self, trajectory, radius, color = (255, 108, 150)):
        self.trajectory = trajectory
        self.radius = radius
        self.color = color
    
    def position_at(self, time):
        return self.trajectory.calculate_position_at_time(time)
    
    # render this object at a specific time
    def render(self, camera, time):
        position = self.position_at(time)
        detail_level = render.detail_level(15, 250*self.radius/camera.fov, Vector3.distance(position, camera.position))

        render.draw_sphere(camera, self.radius, position, detail_level, self.color)
    
    # render the trajectory of this body during time interval [time_begin, time_final] at step intervals of time_step
    def render_trajectory(self, camera, time_begin, time_final, time_step):
        previous_point = self.position_at(time_begin)
        for current_time in range(time_begin + time_step, time_final, time_step):
            current_point = previous_point + self.position_at(current_time)
            # definetly a more efficient way to draw entire trajectory, which I will do when 
            # creating the planetary system data structure container class thingy
            render.draw_vector(camera, previous_point, current_point, (200,200,0), 1)