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
    line = Line([1, 0], [0, 3])
    circle = Circle(0, 0, 1, 8)

    cube = Cube(1, 1, 1, 1)
    parallelepiped = Parallelepiped(1, 1, 1, 1, 1, 2)
    piramid = Piramid(0, 1, 0, 1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # square.draw()
        # rectangle.draw()
        # triangle.draw()
        # line.draw()
        # circle.draw()

        # cube.draw()
        # parallelepiped.draw()
        piramid.draw()

        pygame.display.flip()
        pygame.time.wait(10)
