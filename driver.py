import wireframe
import viewer
from colors import *

WIDTH = 700
HEIGHT = 600

CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

print("Creating cubes...")
cube_nodes = [(x,y,z) for x in (CENTER_X-200, CENTER_X-100) \
                      for y in (CENTER_Y-50, CENTER_Y+50) \
                      for z in (-50, 50)]

cube_faces = [(0,2,6,WINE), (0,6,4,WINE), \
              (7,3,1,WINE), (1,5,7,WINE), \
              (4,6,7,AUSTIN), (7,5,4,AUSTIN), \
              (0,1,2,AUSTIN), (3,2,1,AUSTIN), \
              (0,4,1,SALMON), (1,4,5,SALMON), \
              (2,3,7,SALMON), (2,7,6,SALMON)]

cube1 = wireframe.Wireframe(cube_nodes, cube_faces)
cube1.rotate_y(0.785398)
cube1.rotate_x(-0.523599)

cube_nodes = [(x,y,z) for x in (CENTER_X+100, CENTER_X+200) \
                      for y in (CENTER_Y-50, CENTER_Y+50) \
                      for z in (-50, 50)]

cube_faces = [(0,2,6,SEA), (0,6,4,SEA), \
              (7,3,1,SEA), (1,5,7,SEA), \
              (4,6,7,LIME), (7,5,4,LIME), \
              (0,1,2,LIME), (3,2,1,LIME), \
              (0,4,1,OLIVE), (1,4,5,OLIVE), \
              (2,3,7,OLIVE), (2,7,6,OLIVE)]

cube2 = wireframe.Wireframe(cube_nodes, cube_faces)
print("Created cubes!\n")

print("Creating viewer...")
viewer = viewer.Viewer(WIDTH, HEIGHT)
viewer.add_wireframe(cube1)
viewer.add_wireframe(cube2)
print("Created viewer!\n")

print("Running...")
viewer.run()
print("Done!")