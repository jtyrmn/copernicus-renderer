from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import pi, sqrt

import pygame
from pygame.locals import *

from vector3 import *

import sys

sphere = gluNewQuadric()
gluQuadricDrawStyle(sphere, GLU_LINE)

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

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


# see render.detail_level() for info on parameter detail
def draw_sphere(camera, radius, position, detail, color):
    # note that all of the matrix transformations are performed in reverse order due to PyOpenGl's matrix stack mechanic
    glPushMatrix()
    # color
    glColor3fv(color)

    # convert orthogonal scene to perspective
    # setting far end of the view frustrum to sys.float_info.max because this camera will need to 
    # render at extreme distances
    gluPerspective(camera.fov, camera.width/camera.height, 0.1, sys.float_info.max)
    
    # rotate object around camera to simulate camera's rotation
    glRotatef(camera.rotation.x, 1, 0, 0)
    glRotatef(camera.rotation.y, 0, 1, 0)
    glRotatef(camera.rotation.z, 0, 0, 1)

    # camera's position
    glTranslatef(-camera.position.x, -camera.position.y, -camera.position.z)
    # object's position
    glTranslatef(position.x, position.y, position.z)

    # rotate the sphere so that one of it's polar ends (not related to planets, just the 2 opposite ends of a UV sphere) 
    # faces the camera. This makes the sphere appear rounder and more consistent from a moving camera
    glRotatef(90, 1,0,0)
    # EDIT: this is somewhat difficult to implement, dunno how to do a lookat with vectors. So I'll leave as above for now

    gluSphere(sphere, radius, int(detail), int(detail))

    glPopMatrix()

# draw_vector can be used to draw lines in 3d space from origin to destination (both Vector3)
# color is a tuple
def draw_line(camera, origin, destination, color = (255,255,255), line_width = 1):
    point_a = (origin.x, origin.y, origin.z)
    point_b = (destination.x, destination.y, destination.z)

    glColor3fv(color)
    glLineWidth(line_width)

    # draw line from point_a to point_b
    glPushMatrix()

    # convert orthogonal scene to perspective
    # setting far end of the view frustrum to sys.float_info.max because this camera will need to 
    # render at extreme distances
    gluPerspective(camera.fov, camera.width/camera.height, 0.1, sys.float_info.max)

    # rotate object around camera to simulate camera's rotation
    glRotatef(camera.rotation.x, 1, 0, 0)
    glRotatef(camera.rotation.y, 0, 1, 0)
    glRotatef(camera.rotation.z, 0, 0, 1)

    # camera's position
    glTranslatef(-camera.position.x, -camera.position.y, -camera.position.z)
    
    # draw both points
    glBegin(GL_LINES)
    glVertex3fv(point_a)
    glVertex3fv(point_b)
    glEnd()

    glPopMatrix()

# this function is for determining the number of stacks, slices of a sphere, which should decrease as the 
# distance from the camera increases. Parameter distance should implement Vector3 .length() or .distance() function
# initial_level is the detail at 0 distance
# distance and camera fov should ideally be positive
# stretch represents the horizontal stretch of the returned function. In other words, the greater the stretch, the 
# less detail is removed as distance is increased
def detail_level(initial_level, stretch, distance):
    # detail level is inversely proportional to the square root of the distance
    return 0.25*initial_level/math.sqrt(distance/stretch + 1) + 4