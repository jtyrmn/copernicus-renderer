from celestial_bodies.celestial_body import Celestial_Body
from celestial_bodies.trajectories.circular import Circular
from celestial_bodies.trajectories.stationary import Stationary

from vector3 import Vector3
# I really need to figure out packages and __init__.py to make these imports easier

# This is (not including precise details) Tycho Brahe's Tychonic model of the universe, which places the Earth at the center of the
# universe. The Earth is orbited by the moon and the sun, and the sun is orbited by every other planet
earth = Celestial_Body(
    Stationary(
        Vector3(0,0,0)
    ),
    1,
    (0, 83/255, 255/255),
    name="Earth"
)
moon = Celestial_Body(
    Circular(
        earth,
        3,
        3000,
        0
    ),
    0.3,
    (200/255, 204/255, 209/255),
    name="Moon"
)
sun = Celestial_Body(
    Circular(
        earth,
        20,
        24000,
        0
    ),
    3,
    (253/255, 209/255, 0),
    name="Sun"
)
mercury = Celestial_Body(
    Circular(
        sun,
        7,
        6000,
        0
    ),
    1,
    (255/255, 157/255, 128/255),
    name="Mercury"
)
venus = Celestial_Body(
    Circular(
        sun,
        7,
        7300,
        0
    ),
    1,
    (255/255, 157/255, 128/255),
    name="Venus"
)
mars = Celestial_Body(
    Circular(
        sun,
        30,
        9000,
        0
    ),
    1,
    (255/255, 104/255, 61/255),
    name="Mars"
)
jupiter = Celestial_Body(
    Circular(
        sun,
        36,
        11000,
        0
    ),
    3,
    (218/255, 163/255, 102/255),
    name="Jupiter"
)
saturn = Celestial_Body(
    Circular(
        sun,
        42,
        12000,
        0
    ),
    2,
    (222/255, 185/255, 139/255),
    name="Saturn"
)

tychonic_model = [earth, moon, sun, mercury, venus, mars, jupiter, saturn]