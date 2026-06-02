# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# c = int(input("Enter c :"))

# if(a>b and a>c):
#     print("a is greatest")
# elif(b>c):
#     print("b iss greatest")
# else:
#     print("c is greatest")    

# print("Apna kaam jaldi kar")


A = int(input("Enter A :"))
B = int(input("Enter B :"))
C = int(input("Enter C :"))
D = int(input("Enter D :"))

if(A>=B and A>=C and A>=D):
    print("First number is greatest : ", A)
elif(B>=C and B>=D):
    print("Second number is greatest : ", B)
elif(C>=D):
    print("Third number is greatest : ", C)
else:
    print("Fourth number is greatest : ", D)
 