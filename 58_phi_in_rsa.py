# 58. Program to demonstrate role of Euler’s Phi in RSA

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("φ(n) =", phi)
