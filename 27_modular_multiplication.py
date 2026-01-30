# 27. Program to perform modular multiplication

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

result = (a * b) % m
print("(", a, "*", b, ") mod", m, "=", result)
