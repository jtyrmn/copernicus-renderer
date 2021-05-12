import math
from math import sin, cos, radians

import numpy as np

# vector3 is a simple 3-dimensional vector container for repesenting positions and rotations

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    #basic operations
    def __add__(self, vector):
        return Vector3(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    def __sub__(self, vector):
        return Vector3(self.x - vector.x, self.y - vector.y, self.z - vector.z)
    def __truediv__(self, divisor):
        return Vector3(self.x / divisor, self.y / divisor, self.z / divisor)
    def __mul__(self, factor):
        return Vector3(self.x * factor, self.y * factor, self.z * factor)
    def __mod__(self, divisor):
        return Vector3(self.x % divisor, self.y % divisor, self.z % divisor)

    #returns magnitude of vector
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    # rotate() returns this vector rotated around (0, 0, 0) in 3d space.
    # The one parameter is a vector3 containing rotation around x, y, z, axis (in radians) 
    def rotate(self, rotation):

        #define x,y,z rotational matrices
        rotation_x_matrix = np.array([
            [1, 0, 0],
            [0, cos(rotation.x), -sin(rotation.x)],
            [0, sin(rotation.x), cos(rotation.x)]
        ])
        rotation_y_matrix = np.array([
            [cos(rotation.y), 0, -sin(rotation.y)],
            [0, 1, 0],
            [sin(rotation.y), 0, cos(rotation.y)]
        ])
        rotation_z_matrix = np.array([
            [cos(rotation.z), -sin(rotation.z), 0],
            [sin(rotation.z), cos(rotation.z), 0],
            [0, 0, 1]
        ])

        #convert vector to np.array and perform vector multiplications on it
        rotated_vector = np.array([
            [self.x],
            [self.y],
            [self.z]
        ])
        
        rotated_vector = np.matmul(rotation_x_matrix, rotated_vector)
        rotated_vector = np.matmul(rotation_y_matrix,rotated_vector)
        rotated_vector = np.matmul(rotation_z_matrix,rotated_vector)

        #convert back
        return Vector3(rotated_vector[0][0], rotated_vector[1][0], rotated_vector[2][0])
    
    # return a vector of length 1
    def normalize(self):
        return self/self.length()
    
    # for if a vector3 stores rotations in degrees
    # else-wise, don't use!
    def to_radians(self):
        return Vector3(radians(self.x), radians(self.y), radians(self.z))

    #returns physical distance between vector1, vector2
    @staticmethod
    def distance(vector1, vector2):
        return (vector1 - vector2).length()