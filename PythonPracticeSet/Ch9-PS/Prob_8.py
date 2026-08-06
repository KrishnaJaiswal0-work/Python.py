with open("Python Practice Set/Ch9-PS/this.txt") as f:
    content = f.read()

with open("Python Practice Set/Ch9-PS/this_copy.txt", "w") as f:
    f.write(content)