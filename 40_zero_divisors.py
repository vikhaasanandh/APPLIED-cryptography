# 40. Program to identify zero divisors in a ring Zn

n = int(input("Enter modulus n: "))

for a in range(1, n):
    for b in range(1, n):
        if (a * b) % n == 0:
            print("Zero divisors:", a, "and", b)
