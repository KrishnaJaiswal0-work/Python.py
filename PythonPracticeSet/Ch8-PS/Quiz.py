# def greet():
#     name = input("Enter your name :")
#     print("Good Day", name)

# greet()

# Function Example

def greet(name, end):
    print("Good Day", name)
    print(end)
    return "Thala for a reason "

a = greet("krishna", "Thank you")
greet("parth", "Thank you")
print(a)


# def greet(name, end="Thank you"):
#     print(f"Good Day, {name}")
#     print(end)

# greet("suyesh", "Thanks")

# Recursion Example

# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter a number :"))
# print(f"The factorial of thid number is : {factorial(n)}")