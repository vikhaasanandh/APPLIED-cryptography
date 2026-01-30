# 54. Program to verify Fermat’s Little Theorem

a = int(input("Enter a: "))
p = int(input("Enter a prime number p: "))

print("a^(p-1) mod p =", pow(a, p - 1, p))
