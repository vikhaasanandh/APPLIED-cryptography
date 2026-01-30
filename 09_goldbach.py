#9.Program to verify Goldbach’s Conjecture for a given even number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter an even number greater than 2: "))

if n <= 2 or n % 2 != 0:
    print("Please enter a valid even number greater than 2")
else:
    print("Prime pairs whose sum is", n, ":")

    found = False
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(i, "+", n - i, "=", n)
            found = True

    if not found:
        print("Goldbach's conjecture failed for", n)