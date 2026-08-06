def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter inch to convert in cms: "))
c = inch_to_cm(inch)
print(f"{c}cms")