# 43. Program to verify that Zp forms a field for prime p

import math
p = int(input("Enter a prime number p: "))

if all(math.gcd(i, p) == 1 for i in range(1, p)):
    print("Zp is a field")
else:
    print("Zp is NOT a field")
