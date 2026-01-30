#12.Program to check whether a given number is a safe prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if is_prime(n) and is_prime((n - 1) // 2):
    print(n, "is a SAFE PRIME")
else:
    print(n, "is NOT a safe prime")