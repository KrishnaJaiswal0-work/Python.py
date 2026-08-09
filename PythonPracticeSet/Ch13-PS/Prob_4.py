from functools import reduce
l = [1, 2, 3, 4, 5, 80, 67, 43, 45, 65, 25, 30, 75, 17, 20]

def greater(a, b):
    if (a>b):
        return a
    return b 

print(reduce(greater, l))