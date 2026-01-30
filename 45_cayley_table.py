# 45. Program to construct Cayley table for addition modulo n

n = int(input("Enter modulus n: "))

for i in range(n):
    for j in range(n):
        print((i + j) % n, end=" ")
    print()
