# 26. Program to perform modular addition

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

result = (a + b) % m
print("(", a, "+", b, ") mod", m, "=", result)
