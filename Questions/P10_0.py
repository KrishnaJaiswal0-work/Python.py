str = "you are  very bad  worker in house"
count = 0
for i in range(len(str)-1):

    if(str[i:i+2]=="  "):
        print("Extra space! ")
        count += 1
        print(count)


# text = "you are  very bad  worker in house"

# if "  " in text:
#     print("Extra space found!")
# else:
#     print("No extra spaces.")
