# 31. Program to check the congruence of two integers modulo n

a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter modulus n: "))

if (a - b) % n == 0:
    print(a, "is congruent to", b, "mod", n)
else:
    print(a, "is NOT congruent to", b, "mod", n)
