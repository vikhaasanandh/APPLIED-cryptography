# 55. Program to compare Fermat’s and Euler’s Theorems

a = int(input("Enter a: "))
n = int(input("Enter n: "))

phi = sum(1 for i in range(1, n + 1) if __import__("math").gcd(i, n) == 1)

print("Euler:", pow(a, phi, n))
print("Fermat (if n prime):", pow(a, n - 1, n))
