import render
from vector3 import Vector3
from camera import Camera

import universe_models.tychonic
import universe_models.kepler

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pygame

WIDTH, HEIGHT = 1000, 800

def main():
    # camera object
    camera = Camera(Vector3(0,0,0), Vector3(0,0,0), WIDTH, HEIGHT, 45, 0.01, 0.1)
    # create window
    screen = render.renderer_init(WIDTH, HEIGHT)

    # main loop
    while True:
        # handle screen input. Needs to be called every frame or else pygame event buffer overfills
        camera.handle_input()
        
        # render everything here
        #render.draw_circle(camera, 1, Vector3(0, 0, 0))
        time = pygame.time.get_ticks() * 2
        
        # Tychonic model of universe, see universe_models for more info
        for body in universe_models.kepler.kepler_model:
            body.render(camera, time)
            # Note that render_trajectory is quite expensive to run atm, it has to calculate the 
            # position for every past/previous position when it should be memoized (on my TODO list)
            body.render_trajectory(camera, time-3000, time+3000, 400)

        # swap buffers to show what's rendered
        render.at_end_of_loop()
        camera.at_end_of_loop(time)

main()