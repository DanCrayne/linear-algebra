import math
import copy

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
        """Count of the vector's dimensions (number of components).

           Returns:
                A number representing the vector's length.
        """

        return len(self.components)

    def norm(self):
        """Get's this vector's norm (length - often denoted ||v||).
           
           Returns:
                A floating point approximation of the vector's norm.
        """

        sum_of_squares = 0

        for x in self.components:
            sum_of_squares += x**2
        
        return math.sqrt(sum_of_squares)

    def normalized(self):
        """Computes the normalized form of a vector; that is, a vector
           which has the same direction, but length 1 (i.e. unit vector).

           Returns:
                A new vector which is normalized for this vector.
        """

        v_copy = copy.deepcopy(self)
        v_norm = v_copy.norm()

        for i in range(0, v_copy.dimensions()):
            v_copy.components[i] = v_copy.components[i] / v_norm

        return v_copy
