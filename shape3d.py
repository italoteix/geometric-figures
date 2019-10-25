from OpenGL.GL import *
from math import sqrt


class Cube:
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # width: Size dimension
    def __init__(self, x, y, z, width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append([self.x, self.y - self.width, self.z])
        points_list.append([self.x + self.width, self.y - self.width, self.z])
        points_list.append([self.x + self.width, self.y, self.z])
        points_list.append([self.x, self.y, self.z - self.width])
        points_list.append([self.x, self.y - self.width, self.z - self.width])
        points_list.append([self.x + self.width, self.y -
                            self.width, self.z - self.width])
        points_list.append([self.x + self.width, self.y, self.z - self.width])
        return points_list

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
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # width height, length: Parallelepiped dimensions
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
        points_list.append([self.x, self.y - self.height, self.z])
        points_list.append(
            [self.x + self.length, self.y - self.height, self.z])
        points_list.append([self.x + self.length, self.y, self.z])
        points_list.append([self.x, self.y, self.z - self.width])
        points_list.append([self.x, self.y - self.height, self.z - self.width])
        points_list.append([self.x + self.length, self.y -
                            self.height, self.z - self.width])
        points_list.append([self.x + self.length, self.y, self.z - self.width])
        return points_list

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
    # Params:
        # x, y, z: Front-upper-left vertex coordinate
        # height: Distance to top vertex to base
        # width, length: Base's dimensions
    def __init__(self, x, y, z, height, width, length):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.width = width
        self.length = length
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.x, self.y, self.z])
        points_list.append(
            [self.x - self.length / 2, self.y - self.height, self.z + self.width / 2])
        points_list.append(
            [self.x - self.length / 2, self.y - self.height, self.z - self.width / 2])
        points_list.append(
            [self.x + self.length / 2, self.y - self.height, self.z + self.width / 2])
        points_list.append(
            [self.x + self.length / 2, self.y - self.height, self.z - self.width / 2])
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


class Line3d:
    # Params:
        # origin: Beginning point coordinates passed as a array [x, y, z]
        # end: Final point coordinates passed as a array [x, y, z]
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.points = self._create_points()

    def _create_points(self):
        points_list = []
        points_list.append([self.origin[0], self.origin[1], self.origin[2]])
        points_list.append([self.end[0], self.end[1], self.end[2]])
        return points_list

    def draw(self):
        glBegin(GL_LINES)
        glColor(1.0, 0.0, 0.0)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])

        glEnd()
    pass


class Sphere:
    pass
