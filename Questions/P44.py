def c_to_f(c):
    return (c*1.8)+32

c = int(input("Enter Temperature in C:"))
f = c_to_f(c)
print(f"{round(f,2)}°F")


   
