l = [1, 2, 3, 4, 5, 80, 67, 43, 45, 65, 25, 30, 75, 17, 20]
def divisible(n):
    if (n%5 == 0):
        return True
    return False

onlydivisible = filter(divisible, l)
print(list(onlydivisible))
