class regular_polyhedron:
    def __init__ (self, vertex, face, side):
        self.vertex = vertex
        self.face = face
        self.side = side
    def get_edge(self):
        edge = self.vertex * ((self.vertex - 1)/2)
        return edge
    def get_dihedral_angle(self):
        dihedral_angel = self.face + self.vertex - (self.vertex * ((self.vertex - 1)/2))
        return dihedral_angel
    def get_side(self):
        return f'side of this regular polyhedron = {self.side}'

class cube(regular_polyhedron):
    def __init__(self, vertex, face, side):
        self.vertex = 8
        self.face = 6
        self.side = side
    def get_edge(self):
        edge = self.vertex * ((self.vertex - 1) / 2)
        return edge
    def get_area(self):
        area = 6*self.side**2
        return area
    def get_volume(self):
        volume = self.side**3
        return volume

class tetrahedron(regular_polyhedron):
    def __init__(self, vertex, face, side):
        self.vertex = 4
        self.face = 4
        self.side = side
    def get_edge(self):
        edge = self.vertex * ((self.vertex - 1) / 2)
        return edge
    def get_area(self):
        area = self.side**2 * 3**0.5
        return area
    def get_volume(self):
        volume = (2**0.5)/12 * self.side**3
        return volume

class octahedron(regular_polyhedron):
    def __init__(self, vertex, face, side):
        self.vertex = 6
        self.face = 8
        self.side = side
    def get_edge(self):
        edge = self.vertex * ((self.vertex - 1) / 2)
        return edge
    def get_area(self):
        area = 2*self.side**2 * 3**0.5
        return area
    def get_volume(self):
        volume = (self.side**3 * 2**0.5)/3
        return volume