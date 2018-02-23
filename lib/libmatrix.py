from libvector import *

# returns the matrix resulting from matrix multiplication of two matrices A & B,
# where A is a [m by n] matrix and B is a [n by p] matrix;
# returns [] if multiplication is not possible
def multiply_matrices(A, B):
    # the number of columns of A must equal the number of rows of B
    # else, we return an empty array
    if (len(A[0]) != len(B)):
        print("Can't multiply matrices: the column count of A is not equal to the row count of B.")
        return []

    C = []
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    '''
    We multiply two matrices A and B by walking through the first _row_ of A and
    multiplying each element by the corresponding elements in the first 
    _column_ of B, and then summing the terms.

    So, given the following matrices:

         A       B
       1 0 2   2 1 0
       2 0 1   0 3 1
       2 1 3   2 0 1

    we get the product matrix C as follows:
       
        C_11 = (A_11 * B_11) + (A_12 * B_21) + (A_13 * B_31) = 6
        C_12 = (A_11 * B_12) + (A_12 * B_22) + (A_13 * B_32) = 1
        C_13 = (A_11 * B_13) + (A_12 * B_23) + (A_13 * B_33) = 2

        C_21 = (A_21 * B_11) + (A_22 * B_21) + (A_23 * B_31) = 6
        C_22 = (A_21 * B_12) + (A_22 * B_22) + (A_23 * B_32) = 2
        C_23 = (A_21 * B_13) + (A_22 * B_23) + (A_23 * B_33) = 1

        C_31 = (A_31 * B_11) + (A_32 * B_21) + (A_33 * B_31) = 10
        C_32 = (A_31 * B_12) + (A_32 * B_22) + (A_33 * B_32) = 5
        C_33 = (A_31 * B_13) + (A_32 * B_23) + (A_33 * B_33) = 4

          C
        6 1 2
        6 2 1
       10 5 4
    '''
    for i in range(0, m):
        new_row = []
        for j in range(0, p):
            sum = 0

            for k in range(0, n):
                sum += A[i][k] * B[k][j]

            new_row.append(sum)

        C.append(new_row)

    return C


def qr_decomposition(A):
    Q = []
    R = []
    return (Q,R)


# pretty prints a two-dimensional matrix (array) to the console
def pretty_print(matrix):
    cell_width = max_cell_width(matrix) + 1
    matrix_width = len(matrix[0]) * cell_width + 3

    print '+- {0:>{width}}'.format('-+', width=matrix_width)

    for row in matrix:
        print('|'),

        for col in row:
            print '{0:^{width}}'.format(col, width=cell_width),

        print('|')

    print '+- {0:>{width}}'.format('-+', width=matrix_width)


def max_cell_width(matrix):
    largest_str_len = 0

    for row in matrix:
        for col in row:
            if len(str(col)) > largest_str_len:
                largest_str_len = len(str(col))

    return largest_str_len
