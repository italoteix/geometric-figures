from OpenGL.GL import *
from math import pi, sin, cos, tan


class Square:

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y + self.width])
        points_list.append([self.x, self.y + self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[2][0], self.points[2][1])
        glVertex2f(self.points[3][0], self.points[3][1])
        glEnd()


class Retangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y + self.height])
        points_list.append([self.x, self.y + self.height])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[2][0], self.points[2][1])
        glVertex2f(self.points[3][0], self.points[3][1])
        glEnd()


class Triangle:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y])
        points_list.append([self.x + self.width, self.y + self.width])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])
        glVertex2f(self.points[2][0], self.points[2][1])

        glEnd()


class Line:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y])
        points_list.append([self.x + self.width, self.y + self.width])
        return points_list

    def draw(self):
        glBegin(GL_LINES)
        glColor(1.0, 0.0, 0.0)
        glVertex2f(self.points[0][0], self.points[0][1])
        glVertex2f(self.points[1][0], self.points[1][1])

        glEnd()


class Circle:
    def __init__(self, x, y, raio, setores):
        self.x = x
        self.y = y
        self.raio = raio
        self.setores = setores
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        ang = pi * 2 / self.setores
        for i in range(0, self.setores):
            points_list.append(
                [self.x + (self.raio * cos(i * ang)), self.y + (self.raio * sin(i * ang))])
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        for i in range(0, self.setores):
            if(i == (self.setores - 1)):
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0], self.points[i][1])
                glVertex2f(self.points[0][0], self.points[0][1])
            else:
                glVertex2f(self.x, self.y)
                glVertex2f(self.points[i][0], self.points[i][1])
                glVertex2f(self.points[i + 1][0], self.points[i + 1][1])
        glEnd()
