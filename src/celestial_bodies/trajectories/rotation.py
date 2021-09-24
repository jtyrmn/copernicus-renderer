from abc import ABC, abstractmethod

#this file is like trajectory.py,  except it deals with rotation of a body and not position
class Rotation:
    # rotational_tilt is the (in radians) static rotational offset, aka body's rotation at time 0
    # rotational_movement is the rotational movement that the body moves by over one unit of time, if that makes sense. Also in radians
    def __init__(self, rotational_tilt, rotational_movement):
        self.rotational_tilt = rotational_tilt
        self.rotational_movement = rotational_movement
    
    # returns the body's Vector3 rotation at specific time
    def rotation_at_time(self, time):
        return self.rotational_tilt + self.rotational_movement*time