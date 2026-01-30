# 20. Program to check co-primality using GCD

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, b) == 1:
    print(a, "and", b, "are Co-Prime")
else:
    print(a, "and", b, "are NOT Co-Prime")
