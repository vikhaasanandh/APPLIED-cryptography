# 16. Program to compute GCD using the Euclidean Algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

print("GCD of", a, "and", b, "is:", x)
