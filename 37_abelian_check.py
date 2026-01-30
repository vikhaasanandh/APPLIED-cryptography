# 37. Program to verify whether a given group is Abelian

n = int(input("Enter modulus n: "))
A = list(map(int, input("Enter elements of set: ").split()))

is_abelian = True

for a in A:
    for b in A:
        if (a + b) % n != (b + a) % n:
            is_abelian = False

if is_abelian:
    print("The group is Abelian")
else:
    print("The group is NOT Abelian")
