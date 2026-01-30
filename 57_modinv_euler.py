# 57. Program to compute modular inverse using Euler’s Theorem

a = int(input("Enter a: "))
n = int(input("Enter n: "))

phi = sum(1 for i in range(1, n + 1) if __import__("math").gcd(i, n) == 1)

inv = pow(a, phi - 1, n)
print("Modular inverse =", inv)
