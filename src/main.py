import render
from vector3 import Vector3
from camera import Camera

# from celestial_bodies.celestial_body import *
# from celestial_bodies.trajectories import stationary
from celestial_bodies.celestial_body import Celestial_Body
from celestial_bodies.trajectories.stationary import Stationary
from celestial_bodies.trajectories.circular import Circular
# TODO make these imports cleaner ^^^

from pygame.time import get_ticks

WIDTH, HEIGHT = 1000, 800

def main():
    # camera object
    camera = Camera(Vector3(0,0,0), Vector3(0,0,0), WIDTH, HEIGHT, 45, 0.005, 0.05)
    # create window
    screen = render.renderer_init(WIDTH, HEIGHT)

    # create sun
    sun = Celestial_Body(
        Stationary(
            Vector3(0,0,0)
        ),
        3,
        Vector3(1,0,0)
    )

    # create planet
    planet = Celestial_Body(
        Circular(
            sun,
            10,
            60000,
            0
        ),
        0.5,
        Vector3(0,1,1)
    )

    # create moon
    moon = Celestial_Body(
        Circular(
            planet,
            1,
            2000,
            0
        ),
        0.15,
        Vector3(1,1,1)
    )

    # main loop
    while True:
        # handle screen input. Needs to be called every frame or else pygame event buffer overfills
        camera.handle_input()
        
        # render everything here
        #render.draw_circle(camera, 1, Vector3(0, 0, 0))
        time = get_ticks() * 10
        sun.render(camera, time)
        planet.render(camera, time)
        moon.render(camera, time)

        # swap buffers to show what's rendered
        render.at_end_of_loop()

main()