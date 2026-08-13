m1 = int(input("Enter your marks:"))
m2 = int(input("Enter your marks:"))
m3 = int(input("Enter your marks:"))
total_percentage = ((m1+m2+m3)*100/300)

if(total_percentage<=40 and m1<=33 and m2<=33 and m3<=33):
    print("You are passed! ", total_percentage)

else:
    print("You are failed!", total_percentage)
