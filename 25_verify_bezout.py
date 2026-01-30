# 25. Program to verify Bézout’s Identity

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a = int(input("Enter a: "))
b = int(input("Enter b: "))

g, x, y = extended_gcd(a, b)

print("GCD =", g)
print("x =", x)
print("y =", y)
print("a*x + b*y =", a*x + b*y)

if a*x + b*y == g:
    print("Bézout's Identity is VERIFIED")
else:
    print("Bézout's Identity is NOT satisfied")
