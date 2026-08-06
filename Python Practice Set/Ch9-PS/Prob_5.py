words = ["donkey", "bad", "gande", "rascal"]

with open("Python Practice Set/Ch9-PS/file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Python Practice Set/Ch9-PS/file.txt", "w") as f:
    f.write(content)