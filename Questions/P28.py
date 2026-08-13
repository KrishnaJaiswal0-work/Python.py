p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

comment = input("Enter your comment:")

if((p1.lower() in comment) or (p2.lower() in comment) or (p3.lower() in comment) or (p4.lower() in comment)):
    print("This comment is spam")
else:
    print("This comment is safe")