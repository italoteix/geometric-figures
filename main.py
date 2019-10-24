import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

if __name__ == "__main__":
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslate(0.0, 0.0, -5)

    square = Circle(0, 0, 0.5, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        square.draw()
        pygame.display.flip()
        pygame.time.wait(10)
