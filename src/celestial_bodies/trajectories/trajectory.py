from abc import ABC, abstractmethod

# this abstract class will represent all the possible motions a planet/moon/etc will follow
# it's most significant base class would be elliptical orbit (realistic orbit) as well as
# circular or no trajectory (for stationary bodies like suns)
class Trajectory(ABC):
    
    # this method takes a Time object and calculates what it's position would be at that time.
    # note that this position is relative to the orbited body which we treat as (0, 0, 0)
    @abstractmethod
    def calculate_position_at_time(self, time):
        pass