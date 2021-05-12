from abc import ABC, abstractmethod
from copy import copy
import render

# this abstract class will represent all the possible motions a planet/moon/etc will follow
# it's most significant base class would be elliptical orbit (realistic orbit) as well as
# circular or no trajectory (for stationary bodies like suns)
class Trajectory(ABC):
    
    # this method takes a Time object and calculates what it's position would be at that time.
    # note that this position is relative to the orbited body which we treat as (0, 0, 0)
    @abstractmethod
    def calculate_position_at_time(self, time):
        pass
    
    # draw this trajectory's path during time interval [time_begin, time_final] at step intervals 
    # of time_step
    def render(self, camera, time_begin, time_final, time_step):
        previous_point = self.calculate_position_at_time(time_begin)
        for current_time in range(time_begin, time_final + time_step, time_step):
            current_point = self.calculate_position_at_time(current_time)
            # definetly a more efficient way to draw entire trajectory, which I will do when 
            # creating the planetary system data structure container class thingy
            render.draw_line(camera, previous_point, current_point, (200,200,0), 1)
            previous_point = copy(current_point)