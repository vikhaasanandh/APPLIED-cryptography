# 42. Program to verify whether a given structure forms a field

import math
n = int(input("Enter modulus n: "))

if all(math.gcd(i, n) == 1 for i in range(1, n)):
    print("Zn is a field")
else:
    print("Zn is NOT a field")
