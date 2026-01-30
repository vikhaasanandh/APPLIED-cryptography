# 33. Program to implement arithmetic operations in Zn

a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter modulus n: "))

print("Addition:", (a + b) % n)
print("Subtraction:", (a - b) % n)
print("Multiplication:", (a * b) % n)
