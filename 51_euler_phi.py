# 51. Program to compute Euler’s Phi Function φ(n)

n = int(input("Enter n: "))
count = 0

for i in range(1, n + 1):
    if __import__("math").gcd(i, n) == 1:
        count += 1

print("φ(", n, ") =", count)
