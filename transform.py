from matrix import Matrix


class Transform:
    def reflex2D(self):
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)

            z[1, 1] = 1
            z[2, 2] = -1

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def refley2D(self):
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)

            z[1, 1] = -1
            z[2, 2] = 1

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def projx2D(self):
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)

            z[1, 1] = 1
            z[2, 2] = 0

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def projy2D(self):
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)

            z[1, 1] = 0
            z[2, 2] = 1

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def transla2D(self, x, y):
        for i in range(0, self.points.lenght):
            dom = Matrix(3, 1, [self.points[i][0], self.points[i][1], 1])
            z = Matrix(3, 3)

            z[1, 1] = 1
            z[2, 2] = 1
            z[1, 3] = x
            z[2, 3] = y
            z[3, 3] = 1

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def cisalhamento(self, ang):
        ang = ang * 180 / pi
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)
            z[1, 2] = tan(ang)
            z[1, 1] = 1
            z[2, 2] = 1

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points

    def rotate2D(self, ang):
        ang = ang * 180 / pi
        for i in range(0, self.points.lenght):
            dom = Matrix(2, 1, [self.points[i][0], self.points[i][1]])
            z = Matrix(2, 2)
            z[1, 1] = cos(ang)
            z[1, 2] = -sin(ang)
            z[2, 1] = sin(ang)
            z[2, 2] = cos(ang)

            dom = z.dot(dom)
            self.points[i][0] = dom[1, 1]
            self.points[i][1] = dom[2, 1]
        return points
