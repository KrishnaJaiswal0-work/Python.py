marks = int(input("Enter your marks:"))

if(marks>=90 and marks<=100):
    print("Your grade is Ex, congrats!")
elif(marks>=80 and marks<=90):
    print("Your grade is A, congrats!")
elif(marks>=70 and marks<=80):
    print("Your grade is B, congrats!")
elif(marks>=60 and marks<=70):
    print("Your grade is C, Keep Going!")
elif(marks>=50 and marks<=60):
    print("Your grade is D, Work more!")
elif(marks<50):
    print("Your grade is F, Failed")