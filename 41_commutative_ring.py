# 41. Program to check whether a ring is commutative

n = int(input("Enter modulus n: "))

is_commutative = True
for a in range(n):
    for b in range(n):
        if (a * b) % n != (b * a) % n:
            is_commutative = False

if is_commutative:
    print("Ring is commutative")
else:
    print("Ring is not commutative")
