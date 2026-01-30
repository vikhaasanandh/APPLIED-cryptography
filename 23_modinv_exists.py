# 23. Program to check whether a modular inverse exists

import math

a = int(input("Enter a: "))
m = int(input("Enter modulus m: "))

if math.gcd(a, m) == 1:
    print("Modular inverse exists")
else:
    print("Modular inverse does NOT exist")
