from celestial_bodies.celestial_body import Celestial_Body

# In the Ptolematic model of the universe, the sun and all non-earth planets orbit around earth in epicycles, meaning 
# they orbit around a orbiting point on a larger orbit (the deferent I think). This class is a celestial "body" that
# represents the center of an epicycle, whereas it's orbiting "moon" follows an epicyclic path.

class Epicycle_Center(Celestial_Body):
    def __init__(self, trajectory):
        self.trajectory = trajectory
    
    def render(self, camera, time):
        pass