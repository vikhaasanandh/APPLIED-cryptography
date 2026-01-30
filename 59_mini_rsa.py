# 59. Program to implement a mini RSA example

p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))
m = int(input("Enter message m: "))

n = p * q
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)
c = pow(m, e, n)
m2 = pow(c, d, n)

print("Encrypted:", c)
print("Decrypted:", m2)
