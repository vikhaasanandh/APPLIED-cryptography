# 44. Program to implement group operations modulo n

a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter modulus n: "))

print("Addition:", (a + b) % n)
print("Subtraction:", (a - b) % n)
print("Multiplication:", (a * b) % n)
