list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]

copy_list1 = list1.copy()
list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")
