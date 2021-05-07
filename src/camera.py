from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vector3 import *

import pygame
from pygame.locals import *

# this class is to manage the first person view of the renderer
# position and rotation are both Vector_3 objects, rotation is in degrees

# width and height means screen size
# speed defines movement speed and sensitivity defines rotation speed
class Camera:
    def __init__(self, position, rotation, width, height, fov, speed = 1, sensitivity = 1):
        self.position = position
        self.rotation = rotation
        self.width = width
        self.height = height
        self.fov = fov
        self.speed = speed
        self.sensitivity = sensitivity

        # variables to keep track of movement/etc.
        # pygame.key.get_pressed() and event.key == w,a,s,d,... had irregular
        # movement when you held them while using other keys so I'm using this method
        # I'll try to figure out a cleaner method later
        self.key_w = False
        self.key_a = False
        self.key_s = False
        self.key_d = False
        self.key_space = False
        self.key_shift = False

        self.key_left = False
        self.key_right = False
        self.key_up = False
        self.key_down = False

        self.key_i = False
        self.key_o = False
    
    # def set_position(self, position):
    #     self.position = position
    # def set_rotation(self, rotation):
    #     self.rotation = rotation
    
    # this function translates the camera's position *relative to it's rotation* by the position parameter
    # parameter is a Vector_3 that defines the direction to move to 
    def move(self, position):
        rotated_offset = position.rotate(self.rotation.to_radians()) * self.speed
        #self.position += rotated_offset

        # normally I would just do self.position += rotated_offset but since the x rotation (pitch) is negative when rotating upwards, the y
        # offset needs to be subtracted instead of added, so vertical movements aren't inverted when the camera is facing upwards/downwards 
        self.position.x += rotated_offset.x
        self.position.y -= rotated_offset.y
        self.position.z += rotated_offset.z
    
    # change rotation
    def rotate(self, rotation):
        self.rotation += rotation * self.sensitivity
    
    # position translation without respect to camera's rotation
    def absolute_move(self, position):
        self.position += position
    
    def __str__(self):
        return f'camera @ {self.position} facing {self.rotation % 360}'
    
    
    # handle input. *Must* be called once per main loop
    # deals with pygame events
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.key_w = True
                if event.key == pygame.K_a:
                    self.key_a = True
                if event.key == pygame.K_s:
                    self.key_s = True
                if event.key == pygame.K_d:
                    self.key_d = True
                if event.key == pygame.K_SPACE:
                    self.key_space = True
                if event.key == pygame.K_LSHIFT:
                    self.key_shift = True
                if event.key == pygame.K_LEFT:
                    self.key_left = True
                if event.key == pygame.K_RIGHT:
                    self.key_right = True
                if event.key == pygame.K_UP:
                    self.key_up = True
                if event.key == pygame.K_DOWN:
                    self.key_down = True
                if event.key == pygame.K_i:
                    self.key_i = True
                if event.key == pygame.K_o:
                    self.key_o = True
            
            #TODO find a better way to do this

            # key released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.key_w = False
                if event.key == pygame.K_a:
                    self.key_a = False
                if event.key == pygame.K_s:
                    self.key_s = False
                if event.key == pygame.K_d:
                    self.key_d = False
                if event.key == pygame.K_SPACE:
                    self.key_space = False
                if event.key == pygame.K_LSHIFT:
                    self.key_shift = False
                if event.key == pygame.K_LEFT:
                    self.key_left = False
                if event.key == pygame.K_RIGHT:
                    self.key_right = False
                if event.key == pygame.K_UP:
                    self.key_up = False
                if event.key == pygame.K_DOWN:
                    self.key_down = False
                if event.key == pygame.K_i:
                    self.key_i = False
                if event.key == pygame.K_o:
                    self.key_o = False
            
        # above 2 blocks of code dealt with variables, now to perform actions with these variables
        if self.key_a:
            self.move(Vector3(-1,0,0))
        if self.key_d:
            self.move(Vector3(1,0,0))
        if self.key_w:
            self.move(Vector3(0,0,-1))
        if self.key_s:
            self.move(Vector3(0,0,1))
        if self.key_space:
            self.move(Vector3(0,-1,0))
        if self.key_shift:
            self.move(Vector3(0,1,0))
        if self.key_left:
            self.rotate(Vector3(0,-1,0))
        if self.key_right:
            self.rotate(Vector3(0,1,0))
        if self.key_up:
            self.rotate(Vector3(-1,0,0))
        if self.key_down:
            self.rotate(Vector3(1,0,0))
        if self.key_i:
            self.fov += 0.01
        if self.key_o:
            self.fov -= 0.01

            # elif event.type == pygame.KEYDOWN:
            #     # position
            #     if event.key == pygame.K_a:
            #         self.move(Vector_3(-1, 0, 0))
            #     if event.key == pygame.K_d:
            #         self.move(Vector_3(1, 0, 0))
            #     if event.key == pygame.K_w:
            #         self.move(Vector_3(0, 0, -1))
            #     if event.key == pygame.K_s:
            #         self.move(Vector_3(0, 0, 1))
            #     if event.key == pygame.K_SPACE:
            #         self.move(Vector_3(0, -1, 0))
            #     if event.key == pygame.K_LSHIFT:
            #         self.move(Vector_3(0, 1, 0))

            #     # rotation
            #     if event.key == pygame.K_LEFT:
            #         self.rotate(Vector_3(0, -1, 0))
            #     if event.key == pygame.K_RIGHT:
            #         self.rotate(Vector_3(0, 1, 0))
            #     if event.key == pygame.K_UP:
            #         self.rotate(Vector_3(-1, 0, 0))
            #     if event.key == pygame.K_DOWN:
            #         self.rotate(Vector_3(1, 0, 0))
                
            #     # zoom
            #     if event.key == pygame.K_i:
            #         self.fov += 1
            #     if event.key == pygame.K_o:
            #         self.fov -= 1
                

            # # position
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_a]:
            #     self.move(Vector_3(-1,0,0))
            # if keys[pygame.K_d]:
            #     self.move(Vector_3(1,0,0))
            # if keys[pygame.K_w]:
            #     self.move(Vector_3(0,0,-1))
            # if keys[pygame.K_s]:
            #     self.move(Vector_3(0,0,1))
            # if keys[pygame.K_SPACE]:
            #     self.move(Vector_3(0,-1,0))
            # if keys[pygame.K_LSHIFT]:
            #     self.move(Vector_3(0,1,0))
            
            # # rotation
            # if keys[pygame.K_LEFT]:
            #     self.rotate(Vector_3(0,-1,0))
            # if keys[pygame.K_RIGHT]:
            #     self.rotate(Vector_3(0,1,0))
            # if keys[pygame.K_UP]:
            #     self.rotate(Vector_3(-1,0,0))
            # if keys[pygame.K_DOWN]:
            #     self.rotate(Vector_3(1,0,0))

            # # zooming
            # if keys[pygame.K_i]:
            #     print("zoom in")
            #     self.fov -= 1.0
            # if keys[pygame.K_o]:
            #     self.fov += 1.0
            #     print("zoom out")