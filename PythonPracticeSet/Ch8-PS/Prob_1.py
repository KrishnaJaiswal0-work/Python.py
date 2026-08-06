def num(a, b, c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c

a = 64
b = 52
c = 96

print(num(a, b, c))