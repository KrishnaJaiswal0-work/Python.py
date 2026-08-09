try:
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    c = a/b 
    print(f"A divides by B {c}")
except ZeroDivisionError as e:
    print(f"This division is not possible as b is {b} so this is infinite")