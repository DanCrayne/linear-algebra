import lib

E = [ [1,0,0], [-2,1,0], [0,0,1] ]
A = [ [2,1,1], [4,-6,0], [-2,7,2] ]

print(lib.pretty_print(A))

v = lib.Vector([1,2,3])
print str(v)
print "||v|| is %f" % v.norm()
print "v/||v|| is %s" % str(v.normalized())
print "v has %d dimensions" % v.dimensions()

'''
try:
    print lib.dot_product([1,2], [3,4])

except ValueError as valerr:
    print valerr
    '''
