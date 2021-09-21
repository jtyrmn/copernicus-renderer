'''
    This file deals with computation functions such as attaching to a planet, etc
'''

from math import cos, inf, sin, sqrt

from pygame import Vector3
from celestial_bodies.celestial_body import Celestial_Body

class Logic:
    # Returns the celestial body the camera is currently facing, elsewise null if faced
    @staticmethod
    def select_body(camera, bodies, time) -> Celestial_Body:
        '''
        This function uses mathematical optimization. A line or linear function f(t) = {x,y,z}, where t is 
        an arbritary value, that represents the camera's raycast is drawn and the closest point on it's 
        line to every planet is compared. The planet that is closest to f(t)'s closest point is selected, 
        that is if f(t) actually intersects it.
        '''

        if not len(bodies):
            return None
        
        rotation = camera.rotation.to_radians()
        m_x = cos(rotation.x) * cos(rotation.y)
        m_y = -sin(rotation.x)
        m_z = sin(rotation.x) * cos(rotation.y)

        selected = None
        selected_distance = inf
        for body in bodies:
            # x(t) = m_x * t + b_x, y(t) = m_y * t + b_y, z(t) = m_y * t + b_z
            # localize everything so that the planet is at (0,0,0) and we are trying to minimize sqrt(x(t)^2 + y(t)^2 + z(t)^2)
            # which is just the distance from f(t) to (0,0,0)

            body_position = body.position_at(time)
            b_x = camera.position.x - body_position.x
            b_y = camera.position.y - body_position.y
            b_z = camera.position.z - body_position.z

            # find the value of t that minimizes sqrt(x(t)^2 + y(t)^2 + z(t)^2), to do so you get this formula:
            t = (-m_x*b_x - m_y*b_y - m_z*b_z)/(m_x**2 + m_y**2 + m_z**2)

            minimum_distance = sqrt((m_x*t + b_x)**2 + (m_y*t + b_y)**2 + (m_z*t + b_z)**2)

            print(f"{body} with distance {minimum_distance}")

            # if minimum_distance is the smallest so far, this is the closest body
            if minimum_distance < selected_distance:
                selected = body
                selected_distance = minimum_distance
        
        # Finally, return body unless it wasn't selected
        return (selected if selected_distance >= selected.radius else None)