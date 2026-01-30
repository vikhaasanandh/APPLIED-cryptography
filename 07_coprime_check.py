#7.Program to check whether two numbers are co-prime

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x = a
y = b
while y != 0:
    x, y = y, x % y
if x == 1:
    print(a, "and", b, "are Co-Prime numbers")
else:
    print(a, "and", b, "are NOT Co-Prime numbers")