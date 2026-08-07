with open("PythonPracticeSet/Ch9-PS/this.txt") as f:
    content1 = f.read()

with open("PythonPracticeSet/Ch9-PS/this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes files are identical")
else:
    print("no files are not identical")