# 21. Program to compute LCM using GCD

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

lcm = (a * b) // math.gcd(a, b)

print("LCM of", a, "and", b, "is:", lcm)
