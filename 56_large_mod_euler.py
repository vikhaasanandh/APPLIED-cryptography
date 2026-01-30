# 56. Program to simplify large modular exponentiation using Euler’s Theorem

a = int(input("Enter a: "))
k = int(input("Enter power k: "))
n = int(input("Enter n: "))

phi = sum(1 for i in range(1, n + 1) if __import__("math").gcd(i, n) == 1)

result = pow(a, k % phi, n)
print("Result =", result)
