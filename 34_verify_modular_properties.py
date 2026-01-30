# 34. Program to verify properties of modular arithmetic

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
m = int(input("Enter modulus m: "))

left = (a * (b + c)) % m
right = ((a * b) % m + (a * c) % m) % m

print("LHS =", left)
print("RHS =", right)

if left == right:
    print("Distributive property verified")
else:
    print("Property not satisfied")
