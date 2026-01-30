# 24. Program to compute the modular inverse using Extended Euclidean Algorithm

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a = int(input("Enter a: "))
m = int(input("Enter modulus m: "))

g, x, y = extended_gcd(a, m)

if g != 1:
    print("Modular inverse does NOT exist")
else:
    print("Modular inverse of", a, "mod", m, "is:", x % m)
