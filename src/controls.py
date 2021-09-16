import pygame
from pygame import mouse
from pygame.constants import MOUSEMOTION
from vector3 import Vector3
import sys
from copy import copy

# This module deals with all the keybindings and up down left right etc controls for the 
# camera.py class. It exists so that I can move most of the repetitive code out of camera.py, and 
# so that other classes other than camera.py can access input

class Controls:
    # To use this class, you can directly read from these boolean values whether a key is currently being pressed 
    # or not. Just make sure handle_input is called frequently somewhere in the program
    key_w = False
    key_a = False
    key_s = False
    key_d = False
    key_space = False
    key_shift = False
    key_left = False
    key_right = False
    key_up = False
    key_down = False
    key_i = False
    key_o = False
    key_e = False

    # For mouse movement
    mouse_x = 0
    mouse_y = 0

    # Call this function at the beginning of the program for mouse inputs to work
    @staticmethod
    def controls_init():
        pygame.mouse.set_visible(False)
        #pygame.event.set_grab(True)

    # Has to be called once every loop (by camera.py)
    @staticmethod
    def handle_input():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # mouse movement
            if event.type == MOUSEMOTION:
                y, x = pygame.mouse.get_pos()
                #print(f"x: {x} y: {y}")
                Controls.mouse_x, Controls.mouse_y = x - 100, -(y - 100)
                pygame.mouse.set_pos((100, 100))

            # key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Controls.key_w = True
                elif event.key == pygame.K_a:
                    Controls.key_a = True
                elif event.key == pygame.K_s:
                    Controls.key_s = True
                elif event.key == pygame.K_d:
                    Controls.key_d = True
                elif event.key == pygame.K_SPACE:
                    Controls.key_space = True
                elif event.key == pygame.K_LSHIFT:
                    Controls.key_shift = True
                elif event.key == pygame.K_LEFT:
                    Controls.key_left = True
                elif event.key == pygame.K_RIGHT:
                    Controls.key_right = True
                elif event.key == pygame.K_UP:
                    Controls.key_up = True
                elif event.key == pygame.K_DOWN:
                    Controls.key_down = True
                elif event.key == pygame.K_i:
                    Controls.key_i = True
                elif event.key == pygame.K_o:
                    Controls.key_o = True
                elif event.key == pygame.K_e:
                    Controls.key_e = True

            # key released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    Controls.key_w = False
                elif event.key == pygame.K_a:
                    Controls.key_a = False
                elif event.key == pygame.K_s:
                    Controls.key_s = False
                elif event.key == pygame.K_d:
                    Controls.key_d = False
                elif event.key == pygame.K_SPACE:
                    Controls.key_space = False
                elif event.key == pygame.K_LSHIFT:
                    Controls.key_shift = False
                elif event.key == pygame.K_LEFT:
                    Controls.key_left = False
                elif event.key == pygame.K_RIGHT:
                    Controls.key_right = False
                elif event.key == pygame.K_UP:
                    Controls.key_up = False
                elif event.key == pygame.K_DOWN:
                    Controls.key_down = False
                elif event.key == pygame.K_i:
                    Controls.key_i = False
                elif event.key == pygame.K_o:
                    Controls.key_o = False
                elif event.key == pygame.K_e:
                    Controls.key_e = False
