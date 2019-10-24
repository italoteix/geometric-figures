import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sqrt


class Cube:
    def __init__(self, x, y, z, width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y + self.width, self.z])
        points_list.append([self.x + self.width, self.y + self.width, self.z])
        points_list.append([self.x + self.width, self.y, self.z])
        points_list.append([self.x, self.y, self.z + self.width])
        points_list.append([self.x, self.y + self.width, self.z + self.width])
        points_list.append([self.x + self.width, self.y +
                            self.width, self.z + self.width])
        points_list.append([self.x + self.width, self.y, self.z + self.width])

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(1, 3):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
            glVertex3f(self.points[i + 1][0],
                       self.points[i + 1][1], self.points[i + 1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glEnd()


class Parallelepiped:
    def __init__(self, x, y, z, width, height, length):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y + self.height, self.z])
        points_list.append(
            [self.x + self.length, self.y + self.height, self.z])
        points_list.append([self.x + self.length, self.y, self.z])
        points_list.append([self.x, self.y, self.z + self.width])
        points_list.append([self.x, self.y + self.height, self.z + self.width])
        points_list.append([self.x + self.length, self.y +
                            self.height, self.z + self.width])
        points_list.append([self.x + self.length, self.y, self.z + self.width])

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(1, 3):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
            glVertex3f(self.points[i + 1][0],
                       self.points[i + 1][1], self.points[i + 1][2])
        for i in range(3, 5):
            glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
            glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])
            glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[5][0], self.points[5][1], self.points[5][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[6][0], self.points[6][1], self.points[6][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[7][0], self.points[7][1], self.points[7][2])

        glEnd()


class Piramid:
    def __init__(self, x, y, z, width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        h = self.width * sqrt(2) / 2
        sd = sqrt(self.width) / 2
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x - sd, self.y - h, self.z + self.width/2])
        points_list.append([self.x - sd, self.y - h, self.z - self.width/2])
        points_list.append([self.x + sd, self.y - h, self.z + self.width/2])
        points_list.append([self.x + sd, self.y - h, self.z - self.width/2])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0, 1.0, 0.0)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])

        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])

        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])

        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()
