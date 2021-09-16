from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vector3 import *

import pygame
from pygame.locals import *

from controls import Controls

from math import log, radians
from copy import copy

# this class is to manage the first person view of the renderer
# position and rotation are both Vector_3 objects, rotation is in degrees

# width and height means screen size
# speed defines movement speed and sensitivity defines rotation speed
class Camera:
    def __init__(self, position, rotation, width, height, fov = 45, speed = 1, sensitivity = 1, current_time = 0):
        self.position = position
        self.rotation = rotation
        self.width = width
        self.height = height
        self.fov = fov
        self.speed = speed
        self.sensitivity = sensitivity
        # in order to have a consistent speed/sensitivity with an inconsistant frame rate, we need to 
        # keep track of the time. current_time is the current time in miliseconds.
        self.current_time = current_time
        self.delta_time = 1
    
    # this function translates the camera's position *relative to it's rotation* by the position parameter
    # parameter is a Vector_3 that defines the direction to move to 
    def move(self, position):
        rotated_offset = position.rotate(self.rotation.to_radians()) * self.speed * self.delta_time
        #self.position += rotated_offset

        # normally I would just do self.position += rotated_offset but since the x rotation (pitch) is negative when rotating upwards, the y
        # offset needs to be subtracted instead of added, so vertical movements aren't inverted when the camera is facing upwards/downwards 
        self.position.x += rotated_offset.x
        self.position.y -= rotated_offset.y
        self.position.z += rotated_offset.z
    
    # change rotation
    def rotate(self, rotation):
        self.rotation += rotation * self.sensitivity * self.delta_time * self.fov/45
    
    # position translation without respect to camera's rotation or speed
    def absolute_move(self, position):
        self.position += position
    
    def __str__(self):
        return f'camera @ {self.position} facing {self.rotation % 360} w/ fov {self.fov}'

    # call somewhere at end of main loop. time is the current time in miliseconds. Used to re-calculate delta_time every frame
    def at_end_of_loop(self, time):
        self.delta_time = time - self.current_time
        self.current_time = time
        
    # handle input. *Must* be called once per main loop
    # deals with pygame events
    def handle_input(self):
        Controls.handle_input()
        #print(controls.key_a)

        if Controls.key_a:
            self.move(Vector3(-1,0,0))
        if Controls.key_d:
            self.move(Vector3(1,0,0))
        if Controls.key_w:
            self.move(Vector3(0,0,-1))
        if Controls.key_s:
            self.move(Vector3(0,0,1))

        if Controls.key_space:
            self.move(Vector3(0,-1,0))
        if Controls.key_shift:
            self.move(Vector3(0,1,0))

        # if Controls.key_left:
        #     self.rotate(Vector3(0,-1,0))
        # if Controls.key_right:
        #     self.rotate(Vector3(0,1,0))
        # if Controls.key_up:
        #     self.rotate(Vector3(-1,0,0))
        # if Controls.key_down:
        #     self.rotate(Vector3(1,0,0))

        # Mouse movement
        self.rotate(Vector3(Controls.mouse_x, Controls.mouse_y, 0))

        if Controls.key_i:
            self.fov += 0.1
        if Controls.key_o:
            self.fov -= 0.1
        # ensure stays in the range (1, 100)
        self.fov = max(min(self.fov, 100), 1)