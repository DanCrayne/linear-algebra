import copy

class Matrix:
    """ Represents a n*m matrix.

    Attributes:
        contents (array of arrays of numbers): the matrix contents
        as an array of arrays. Each top-level array contains an array of 
        numbers, and so the top-level corresponds to the rows of the array
        whereas the contained arrays are the column contents.
    """

    contents = [[]]

    def __init__(self, contents):
        """ Builds a matrix instance.

            Args:
               contents (array of arrays of numbers): the matrix contents
        """

        self.contents = contents


    def __str__(self):
        """ Converts the matrix to a pretty string for viewing.""" 
        cell_width = self.max_cell_width() + 1
        matrix_width = len(self.contents[0]) * cell_width - 1

        matrix_str = ''
        matrix_str += '+- {0:>{width}}'.format('-+', width=matrix_width)

        for row in self.contents:
            matrix_str += '\n|'

            for col in row:
                matrix_str += '{0:^{width}}'.format(col, width=cell_width)

            matrix_str += '|'

        matrix_str += '\n+- {0:>{width}}'.format('-+', width=matrix_width)

        return matrix_str


    def max_cell_width(self):
        largest_str_len = 0

        for row in self.contents:
            for col in row:
                if len(str(col)) > largest_str_len:
                    largest_str_len = len(str(col))

        return largest_str_len

    def num_rows(self):
        return len(self.contents)

    def num_cols(self):
        return len(self.contents[0])

    def transposed(self):
        """ Creates a transposed version of this matrix.

            Returns:
                A new matrix which is the transpose of this matrix.
        """

        m_copy = copy.deepcopy(self)

        for i in range(0, self.num_rows()):
            for j in range(0, self.num_cols()):
                m_copy.contents[j][i] = self.contents[i][j]

        return m_copy
