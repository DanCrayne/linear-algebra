def dot_product(v1, v2):
    """Compute the dot product of two vectors
input:  v1, v2 are the vectors, represented by equal length one dimensional 
         arrays of numbers
 output: a number representing the dot product
    """
    if len(v1) != len(v2):
        raise ValueError("Cannot compute dot product: vector lengths are not equal")

    dot_prod = 0
    vector_size = len(v1) 

    for i in range(0, vector_size-1):
        dot_prod += v1[i] * v2[i]

    return dot_prod


# projects vector a onto vector b
def project(a, b):
    return
