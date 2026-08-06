marks1 = int(input("Enter 1st sub marks : "))
marks2 = int(input("Enter 2nd sub marks : "))
marks3 = int(input("Enter 3rd sub marks : "))

# Check or total percentage
total_percentage = ((marks1 + marks2 + marks3)*100)/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed :", total_percentage)

else:
    print("You are failed :", total_percentage)