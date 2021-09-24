from copy import copy, deepcopy
from math import cos, sin
import render
from vector3 import Vector3
from camera import Camera
from controls import Controls
from logic import Logic

import universe_models.tychonic
import universe_models.kepler

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pygame

WIDTH, HEIGHT = 1000, 800

def main():
    # camera object
    camera = Camera(Vector3(0,0,0), Vector3(0,0,0), WIDTH, HEIGHT, 45, 0.02, 0.02)
    # create window
    screen = render.renderer_init(WIDTH, HEIGHT)
    Controls.controls_init()

    v_direction = Vector3(0,0,-1)
    v_position = Vector3(0,0,0)

    # Currently selected planet/celestial body
    selected_body = None

    # main loop
    while True:
        # handle screen input. Needs to be called every frame or else pygame event buffer overfills
        camera.handle_input()
        
        # render everything here
        #render.draw_circle(camera, 1, Vector3(0, 0, 0))
        time = int(pygame.time.get_ticks())
        
        # Tychonic model of universe, see universe_models for more info
        for body in universe_models.kepler.kepler_model:
            body.render(camera, time)
            # Note that render_trajectory is quite expensive to run atm, it has to calculate the 
            # position for every past/previous position when it should be memoized (on my TODO list)
            body.render_trajectory(camera, time-3000, time+3000, 400)

        if Controls.key_e:
            body = Logic.select_body(camera, universe_models.kepler.kepler_model, time)
            if body != None:
                selected_body = body
                print(f"selected body with name {body}")
            else:
                print("no selected body")

        # X Y Z widget at center of screen
        render.draw_widget(camera)
        
        # swap buffers
        render.at_end_of_loop()
        camera.at_end_of_loop(time)
main()