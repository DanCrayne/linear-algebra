import math

class Vector:
    """Represents a 1*m matrix (single column or row); this is known
       as a column or row vector.

       Attributes:
         components (array of numbers): the vector components
    """

    components = []

    def __init__(self, components = []):
        """Builds a vector instance.

            Args:
                components (array of numbers): the vector's components
        """
        self.components = components

    def __str__(self):
        """Converts the vector to a string for viewing.""" 
        return '[ ' + ', '.join([str(x) for x in self.components]) + ' ]'

    def dimensions(self):
        """Count of the vector's dimensions (number of components)."""
        return len(self.components)

    def norm(self):
        """A floating point approximation of the vector's norm (length)."""
        sum_of_squares = 0

        for x in self.components:
            sum_of_squares += x**2
        
        return math.sqrt(sum_of_squares)

    def normalized(self):
        """Returns the normalized form of this vector. This means a vector 
           that is pointed in the same direction, but has length 1 
           (i.e. unit vector).
        """
        return
