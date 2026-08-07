word = "donkey"

with open("PythonPracticeSet/Ch9-PS/file.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word, "######")

with open("PythonPracticeSet/Ch9-PS/file.txt", "w") as f:
    f.write(contentnew)