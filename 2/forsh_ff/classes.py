class RegularPolygon:
    def __init__(self, n):
        self.n = n

    def get_the_angle_of_a_regular_polygon(self):
        a = ((self.n - 2)*180)/self.n
        return a

    def get_count_angle(self):
        return self.n

    def __repr__(self):
        return f'RegularPolygon n = {self.n}'


class Quadrilateral(RegularPolygon):
    def __init__(self, a, b):
        self.n = 4
        self.a = a
        self.b = b

    def get_quadril_perimeter(self):
        return 2*(self.a + self.b)

    def get_quadril_area(self):
        return self.a*self.b

    def __repr__(self):
        return f'Quadrilateral a = {self.a} b = {self.b}'


class Square(Quadrilateral):
    def __init__(self, side):
        self.n = 4
        self.side = side

    def get_perimeter(self):
        return 4*self.side

    def get_square_area(self):
        return self.side**2

    def __repr__(self):
        return f'Square side = {self.side}'


class Triangle(RegularPolygon):
    def __init__(self, a, b, c):
        self.n = 3
        self.a = a
        self.b = b
        self.c = c

    def is_equilateral_triangle(self):
        if self.a == self.b and self.b == self.c:
            return True
        else:
            return False

    def is_isosceles_triangle(self):
        if self.is_equilateral_triangle():
            return True
        elif (self.a == self.b) or (self.b == self.c) or (self.c == self.a):
            return True
        else:
            return False

    def get_triangle_area(self):
        p = (self.a + self.b + self.c)/2
        s = (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5
        return s

    def get_triangle_perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f'Triangle a = {self.a} b = {self.b} c = {self.c}'
