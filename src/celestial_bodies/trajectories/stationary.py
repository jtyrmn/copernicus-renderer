# pylint claims this import is invalid but it's the only thing that doesn't cause an error when I use Stationary outside of this file
from .trajectory import Trajectory

# The simplest trajectory, not moving at all. Stays at a fixed position forever. Mainly for whatever is at the center of a solar system

class Stationary(Trajectory):
    # position is the permanent location of the body
    def __init__(self, position):
        self.position = position
    
    def calculate_position_at_time(self, time):
        return self.position
