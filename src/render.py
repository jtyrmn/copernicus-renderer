from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pygame
from pygame.locals import *

from vector3 import *

import sys

sphere = gluNewQuadric()
gluQuadricDrawStyle(sphere, GLU_LINE)

# call this function at the start of program when you need to use pygame
def renderer_init(width, height):
    # pygame initialization
    pygame.init()
    window = pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("SPAAAAAAAAAAAAAAAAAAAAAACE")
    pygame.key.set_repeat(1, 10)    # allows buttons to be held
    return window

# simple function to swap buffer. *must* call at end of every main loop
# Just so I can keep all the pygame stuff in this file instead of __main__.py
def at_end_of_loop():
    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


def draw_sphere(camera, radius, position):
    # note that all of the matrix transformations are performed in reverse order due to PyOpenGl's matrix stack mechanic
    glPushMatrix()

    # rotate the sphere
    # convert orthogonal scene to perspective
    # setting far end of the view frustrum to sys.float_info.max because this camera will need to 
    # render at extreme distances
    gluPerspective(camera.fov, camera.width/camera.height, 0.1, sys.float_info.max)
    
    # camera's rotation
    # glRotatef(camera.rotation.x * camera.sensitivity, 1, 0, 0)
    # glRotatef(camera.rotation.y * camera.sensitivity, 0, 1, 0)
    # glRotatef(camera.rotation.z * camera.sensitivity, 0, 0, 1)
    glRotatef(camera.rotation.x, 1, 0, 0)
    glRotatef(camera.rotation.y, 0, 1, 0)
    glRotatef(camera.rotation.z, 0, 0, 1)

    # camera's position
    glTranslatef(-camera.position.x, -camera.position.y, -camera.position.z)

    # object's position
    glTranslatef(position.x, position.y, position.z)

    gluSphere(sphere, radius, 10, 10)

    glPopMatrix()