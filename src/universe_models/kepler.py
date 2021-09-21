from celestial_bodies.celestial_body import Celestial_Body
from celestial_bodies.trajectories.stationary import Stationary
from celestial_bodies.trajectories.ellipse_approx import Ellipse_Mock

from vector3 import Vector3
# the kepler model is practically the modern model of the universe, including
# elliptical orbits. Note that the orbit patterns, sizes, etc are not accurate to reality.

sun = Celestial_Body(
    Stationary(
        Vector3(0,0,-10)
    ),
    7,
    (0.921, 0.592, 0),
    name="Sun"
)
mercury = Celestial_Body(
    Ellipse_Mock(
        sun,
        20,
        0.3,
        50000
    ),
    0.7,
    (0.772, 0.588, 0.403),
    name="Mercury"
)
venus = Celestial_Body(
    Ellipse_Mock(
        sun,
        30,
        0.3,
        60000
    ),
    0.8,
    (0.772, 0.588, 0.403),
    name="Venus"
)
earth = Celestial_Body(
    Ellipse_Mock(
        sun,
        40,
        0.3,
        70000
    ),
    1,
    (0.145, 0.243, 0.937),
    name="Earth"
)
moon = Celestial_Body(
    Ellipse_Mock(
        earth,
        2,
        0.3,
        4000
    ),
    0.3,
    (0.698, 0.749, 0.780),
    name="Theia"
)
mars = Celestial_Body(
    Ellipse_Mock(
        sun,
        50,
        0.3,
        80000
    ),
    1,
    (0.850, 0.286, 0.211),
    name="Mars"
)
jupiter = Celestial_Body(
    Ellipse_Mock(
        sun,
        60,
        0.3,
        90000
    ),
    3,
    (0.780, 0.447, 0.4),
    name="Jupiter"
)
saturn = Celestial_Body(
    Ellipse_Mock(
        sun,
        70,
        0.3,
        100000
    ),
    2,
    (0.780, 0.690, 0.4),
    name="Saturn"
)
uranus = Celestial_Body(
    Ellipse_Mock(
        sun,
        80,
        0.3,
        110000
    ),
    0.9,
    (0.133, 0.862, 0.866),
    name="Uranus"
)
neptune = Celestial_Body(
    Ellipse_Mock(
        sun,
        80,
        0.3,
        110000
    ),
    0.8,
    (0.047, 0.443, 0.713),
    name="Neptune"
)
pluto = Celestial_Body(
    Ellipse_Mock(
        sun,
        90,
        0.3,
        110000,
        tilt=3.14/4
    ),
    0.5,
    (0.047, 0.443, 0.713),
    name="Pluto"
)
kepler_model = [sun, mercury, mars, earth, moon, venus, jupiter, saturn, uranus, neptune]