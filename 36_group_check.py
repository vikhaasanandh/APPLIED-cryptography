# 36. Program to verify whether a given set forms a group under addition modulo n

n = int(input("Enter modulus n: "))
A = list(map(int, input("Enter elements of set: ").split()))

is_group = True

for a in A:
    for b in A:
        if (a + b) % n not in A:
            is_group = False

if is_group:
    print("The set forms a group under addition mod", n)
else:
    print("The set does NOT form a group")
