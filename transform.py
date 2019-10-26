from matrix import Matrix
from math import pi, cos, sin, tan


class Transform:
    def reflectX2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)

        z[1, 1] = 1
        z[2, 2] = -1

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def reflectY2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)

        z[1, 1] = -1
        z[2, 2] = 1

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def projectionX2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)

        z[1, 1] = 1
        z[2, 2] = 0

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def projectionY2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)

        z[1, 1] = 0
        z[2, 2] = 1

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def translate2D(self, point, x, y):
        xp, yp = point
        dom = Matrix(3, 1, [xp, yp, 1])
        z = Matrix(3, 3)

        z[1, 1] = 1
        z[2, 2] = 1
        z[1, 3] = x
        z[2, 3] = y
        z[3, 3] = 1

        dom = z.dot(dom)
        xp = dom[1, 1]
        yp = dom[2, 1]
        return [xp, yp]

    def shear(self, point, ang):
        ang = ang * pi / 180
        x, y = point
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)
        z[1, 2] = tan(ang)
        z[1, 1] = 1
        z[2, 2] = 1

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def rotate2D(self, point, ang):
        x, y = point
        ang = ang * pi / 180
        dom = Matrix(2, 1, [x, y])
        z = Matrix(2, 2)
        z[1, 1] = cos(ang)
        z[1, 2] = -sin(ang)
        z[2, 1] = sin(ang)
        z[2, 2] = cos(ang)

        dom = z.dot(dom)
        x = dom[1, 1]
        y = dom[2, 1]
        return [x, y]

    def scale(self, point, x, y):
        xp, yp = point
        dom = Matrix(2, 1, [xp, yp])
        z = Matrix(2, 2)
        z[1, 1] = x
        z[2, 2] = y

        dom = z.dot(dom)
        xp = dom[1, 1]
        yp = dom[2, 1]
        return [xp, yp]
