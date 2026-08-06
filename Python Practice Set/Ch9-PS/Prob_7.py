with open("Python Practice Set/Ch9-PS/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python word is present. Line no: {lineno} ")
        break
    lineno += 1

else:
    print("No, python word is not present ")