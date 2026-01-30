#8.Program to generate all co-prime pairs up to a given number

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n = int(input("Enter the limit: "))
print("Co-prime pairs up to", n, "are:")
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if gcd(i, j) == 1:
            print("(", i, ",", j, ")", end="  ")