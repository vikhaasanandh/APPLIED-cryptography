# 53. Program to verify Euler’s Theorem

a = int(input("Enter a: "))
n = int(input("Enter n: "))

phi = sum(1 for i in range(1, n + 1) if __import__("math").gcd(i, n) == 1)

print("a^φ(n) mod n =", pow(a, phi, n))
