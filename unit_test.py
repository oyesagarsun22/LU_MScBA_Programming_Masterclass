def A(x,y):
    return x+y

def B(x,y):
    return x-y

def C(x,y):
    return A(x,y)+B(x,y)

assert A(2,3) ==5, "A(2,3) should be 5"
assert B(2,3) == -1
assert C(2,3) == 4