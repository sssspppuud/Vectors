class Vector(object):
    def __init__(self, *components):
        self.components = list([float(component) for component in components])
        self.dimensions = len(components)
        self.length_squared = sum(
            [component**2 for component in self.components])

    def __str__(self):
        out = ''
        for component in self.components:
            out += str(component)+' '
        return out

    def getLength(self):
        return self.length**0.5

    def getLengthSquared(self):
        return self.length

    def __add__(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same dimensions.")
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type, must be a vector.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same dimensions.")
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type, must be a vector.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        if not isinstance(scalar, float) and not isinstance(scalar, int):
            raise ValueError("Scalar must be an integer or a float.")
        return Vector(*[component*scalar for component in self.components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def dot(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same dimensions.")
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type, must be a vector.")
        return sum([a * b for a, b in zip(self.components, other.components)])

    def cross(self, other):
        if self.dimensions != 3 or other.dimensions != 3:
            raise ValueError(
                "Cross product is only defined for 3-dimensional vectors.")
        return Vector(
            self.components[1] * other.components[2] -
            self.components[2] * other.components[1],
            self.components[2] * other.components[0] -
            self.components[0] * other.components[2],
            self.components[0] * other.components[1] -
            self.components[1] * other.components[0]
        )

    def getUnitVector(self):
        if all(self.components==0):
            raise ValueError("Cannot normalize vector with length 0.")
        return Vector(*[component*(1/self.length_squared**0.5) for component in self.components])

    def getCosAngle(self, other):
        '''Returns value of cos(theta), where theta is the angle between the vectors'''
        return self.dot(other)/((self.length_squared**0.5)*(other.length_squared**0.5))

