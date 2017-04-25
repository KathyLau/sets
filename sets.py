def union(a, b):
    return a + setdiff(b,a)

def intersect(a, b):
    return [x for x in a if x in b]

def setdiff(a, b):
    return [x for x in a if x not in b]
    
def symdiff(a, b):
    return setdiff(a, b) + setdiff(b, a)

def cartprod(a, b):
    return [(x, y) for x in a for y in b]
