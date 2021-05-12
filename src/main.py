import render
from vector3 import Vector3
from camera import Camera

# from celestial_bodies.celestial_body import *
# from celestial_bodies.trajectories import stationary
from celestial_bodies.celestial_body import Celestial_Body
from celestial_bodies.trajectories.stationary import Stationary
from celestial_bodies.trajectories.circular import Circular
from celestial_bodies.trajectories.ellipse_approx import Ellipse_Mock
# TODO make these imports cleaner ^^^

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

    # create sun
    sun = Celestial_Body(
        Stationary(
            Vector3(0,0,-5)
        ),
        3,
        (255,0,0)
    )

    # create planet
    planet = Celestial_Body(
        Circular(
            sun,
            10,
            10000,
            0
        ),
        0.5,
        (0,200,255)
    )

    # create moon
    moon = Celestial_Body(
        Circular(
            planet,
            1,
            1500,
            0
        ),
        0.15,
        (200,200,200)
    )

    # new planet to test ellipse_mock
    pluto = Celestial_Body(
        Ellipse_Mock(
            sun,
            20,
            0.5,
            20000,
            3000,
            3.1416/2
        ),
        0.4,
        (100,100,255)
    )

    # main loop
    while True:
        # handle screen input. Needs to be called every frame or else pygame event buffer overfills
        camera.handle_input()
        
        # render everything here
        #render.draw_circle(camera, 1, Vector3(0, 0, 0))
        time = pygame.time.get_ticks()
        sun.render(camera, time)
        planet.render(camera, time)
        moon.render(camera, time)
        pluto.render(camera, time)

        #testing trajectory render
        planet.render_trajectory(camera, time - 1000, time + 1000, 100)
        moon.render_trajectory(camera, time - 1000, time + 1000, 75)
        #print(camera)

        # swap buffers to show what's rendered
        render.at_end_of_loop()
        camera.at_end_of_loop(time)

main()