# 49. Program to identify subgroups of a given group Zn

n = int(input("Enter modulus n: "))

for i in range(1, n + 1):
    if n % i == 0:
        print("Subgroup with step", i, ":", [j % n for j in range(0, n, i)])
