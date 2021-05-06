from abc import ABC, abstractmethod

# this abstract class will represent all the possible motions a planet/moon/etc will follow
class trajectory(ABC):
    
    # this method takes a time object and calculates what it's position would be at that time.
    @abstractmethod
    def calculate_position_at_time(self, time):
        pass