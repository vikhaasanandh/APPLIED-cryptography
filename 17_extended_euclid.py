# 17. Program to implement the Extended Euclidean Algorithm

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
