# 35. Program to demonstrate overflow-safe arithmetic using modulo

a = int(input("Enter a large number a: "))
b = int(input("Enter a large number b: "))
m = int(input("Enter modulus m: "))

normal = a * b
safe = (a % m) * (b % m) % m

print("Normal multiplication:", normal)
print("Overflow-safe modulo result:", safe)
