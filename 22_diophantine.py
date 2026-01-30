# 22. Program to solve Linear Diophantine Equation

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

g, x, y = extended_gcd(a, b)

if c % g != 0:
    print("No solution exists")
else:
    print("Solution exists")
    print("x =", x * (c // g))
    print("y =", y * (c // g))
