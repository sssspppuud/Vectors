# Vector Package
Simple python package, lets you create vectors and perform simple operations.

## Vector Class Methods
### __init__(self, *components)
- Creates a vector instance with the provided components.

### __str__(self)
- Returns a string representation of the vector.

### getLength(self)
- Returns the length (magnitude) of the vector.

### getLengthSquared(self)
- Returns the squared length of the vector.

### __add__(self, other)
- Returns the sum of two vectors.

### __sub__(self, other)
- Returns the difference between two vectors.

### __mul__(self, scalar)
- Multiplies the vector by a scalar.

### dot(self, other)
- Calculates the dot product of two vectors.

### cross(self, other)
- Calculates the cross product of two 3-dimensional vectors.

### getUnitVector(self)
- Returns the unit vector of the vector.

### getCosAngle(self, other)
- Calculates the cosine of the angle between two vectors.