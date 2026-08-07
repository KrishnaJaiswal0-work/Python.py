f = open("PythonPracticeSet/Ch9-PS/poem.txt")
content = f.read()
if("twinkle" in content):
    print("The Word twinkle is present in content")
else:
    print("The Word twinkle is not present in content")
f.close()