# copernicus-renderer
Currently work in progress, but the final result would be a program that
renders and accurately displays planetary positions, trajectories from a planet-bound perspective.
![copernicus_renderer](https://user-images.githubusercontent.com/83618806/118250531-700f3300-b45b-11eb-9d84-4f11d6ac5797.png)

## Roadmap
* Main things
 * [x] Ability to select a celestial body and fix the camera's position and relative rotation to it, giving a perspective of the solar system from a specific coordinate of that body.
 * [ ] Planetary Rotation
 * [ ] Celestial bodies should display velocities, poles, as well as rotation
 * [ ] Text GUI (May need to swap out pygame first, unless GUI is in a separate window (TKINTER))
 * [ ] Separate `camera.py` into to different modules `camera.py` and `controls.py` for organization
* Better visuals
  * [ ] Ability to assign cubemap textures to celestial bodies
  * [ ] fix the broken detail culling
  * [ ] anti-aliasing
  * [ ] generic skybox
* Optimization
  * [ ] Memoization of trajectory paths to avoid need to recalculate precise position of every point of trajectory path each frame
   * [ ] Bezier curves for smoother curves and less memory needed for storing points?
  * [ ] Structure tree class to store celestial bodies for better organization and rendering performance.
   * [ ] With pyopengl's matrix stack and celestial bodies' body-orbiting-body-orbiting-body recursive nature, a tree structure that recursively groups the bodies can render objects recursively more efficiently than the current method
   * [ ] Replace pygame with a better, more lightweight(?) rendering front-end. Pygame causes issues with my KDE compositor anyways.

## Installation
I've only ever tested this on Linux but installation is simple and should work on any operating system.
### Dependancies
```
pip install pygame PyOpenGL PyOpenGL_accelerate
```
### Download Repository
```
git clone https://github.com/jtyrmn/copernicus-renderer.git
```
You can run the program by running python on `src/main.py`

## Usage
Currently, to control the camera use W,A,S,D to move around and the up,down,left,right keys to rotate the camera.
