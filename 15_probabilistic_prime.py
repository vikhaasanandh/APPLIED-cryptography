#15.Basic probabilistic prime test using Fermat's Theorem
import random
def power(a, n, p):
    res = 1
    a = a % p
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % p
        n = n // 2
        a = (a * a) % p
    return res
def is_probable_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power(a, n - 1, n) != 1:
            return False
    return True
n = int(input("Enter a number: "))
if is_probable_prime(n):
    print(n, "is probably a PRIME number")
else:
    print(n, "is COMPOSITE")