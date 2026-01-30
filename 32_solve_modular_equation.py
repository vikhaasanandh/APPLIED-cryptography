# 32. Program to solve simple modular equation ax ≡ b (mod m)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))

for x in range(m):
    if (a * x) % m == b % m:
        print("Solution x =", x)
        break
else:
    print("No solution")
