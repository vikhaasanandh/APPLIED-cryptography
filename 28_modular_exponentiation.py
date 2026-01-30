# 28. Program to perform modular exponentiation using fast exponentiation

a = int(input("Enter base a: "))
n = int(input("Enter power n: "))
m = int(input("Enter modulus m: "))

result = pow(a, n, m)
print("(", a, "^", n, ") mod", m, "=", result)
