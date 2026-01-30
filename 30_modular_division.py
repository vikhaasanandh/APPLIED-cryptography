# 30. Program to perform modular division using modular inverse

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

g, x, y = extended_gcd(b, m)

if g != 1:
    print("Division not possible")
else:
    inv = x % m
    print("Result =", (a * inv) % m)
