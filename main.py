import lib

E = [ [1,0,0], [-2,1,0], [0,0,1] ]
A = [ [2,1,1], [4,-6,0], [-2,7,2] ]

print(lib.pretty_print(A))

v = lib.Vector([1,2,3])
print str(v)

'''
try:
    print lib.dot_product([1,2], [3,4])

except ValueError as valerr:
    print valerr
    '''
