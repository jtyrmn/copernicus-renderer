import Render
from Vector_3 import Vector_3
from Camera import Camera

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH, HEIGHT = 1000, 800

def main():
    # camera object
    camera = Camera(Vector_3(0,0,0), Vector_3(0,0,0), WIDTH, HEIGHT, 45, 0.005, 0.05)
    #create window
    screen = Render.renderer_init(WIDTH, HEIGHT)

    # main loop
    while True:
        # handle screen input. Needs to be called every frame or else pygame event buffer overfills
        camera.handle_input()
        
        # render everything here
        Render.draw_circle(camera, 1, Vector_3(0, 0, 0))

        # swap buffers to show what's rendered
        Render.at_end_of_loop()

main()