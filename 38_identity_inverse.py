# 38. Program to find identity and inverse elements in a group

n = int(input("Enter modulus n: "))
A = list(map(int, input("Enter elements of set: ").split()))

for e in A:
    if all((e + a) % n == a for a in A):
        print("Identity element is:", e)

for a in A:
    for b in A:
        if (a + b) % n == 0:
            print("Inverse of", a, "is", b)
