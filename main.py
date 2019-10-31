import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from shape2d import *
from shape3d import *

if __name__ == "__main__":
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(80, display[0]/display[1], 0.1, 50.0)
    glTranslate(0.0, 0.0, -5)

    square = Square(1, 1, 1)
    rectangle = Rectangle(1, 1, 2, 1)
    triangle = Triangle([1, 0], [0, 0], [0, 1])
    line = Line([1, 0], [3, 0])
    circle = Circle(0, 0, 1, 8)

    cube = Cube(1, 1, 1, 1)
    parallelepiped = Parallelepiped(1, 1, 1, 1, 1, 2)
    piramid = Piramid(0, 1, 0, 1, 1, 1.5)
    line3d = Line3d([0, 1, 1], [2, 2, 2])
    sphere = Sphere(0, 0, 0, 1, 10, 10)

    # square.projectionX2D()
    # square.projectionY2D()
    # square.reflectX2D()
    # square.reflectY2D()
    # square.rotate2D(45)
    # square.shear(45)
    # square.translate2D(1, -1)
    # square.scale(1, 1)
    line.projectionY2D()

    # point light from the left, top, front
    # glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
    # glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotate(1, 2, 3, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # glEnable(GL_LIGHTING)
        # glEnable(GL_LIGHT0)
        # glEnable(GL_COLOR_MATERIAL)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        # square.draw()
        # rectangle.draw()
        # triangle.draw()
        line.draw()
        # circle.draw()

        # cube.draw()
        # parallelepiped.draw()
        # piramid.draw()
        # line3d.draw()
        # sphere.draw()

        # glDisable(GL_LIGHT0)
        # glDisable(GL_LIGHTING)
        # glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        pygame.time.wait(10)
