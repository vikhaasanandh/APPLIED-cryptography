# 1. Program to check whether a given number is a prime number or not 
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is NOT a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a PRIME number")
    else:
        print(n, "is NOT a prime number")
