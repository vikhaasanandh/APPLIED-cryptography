#10.Program to find the next prime number greater than a given number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

num = n + 1
while True:
    if is_prime(num):
        print("The next prime number after", n, "is:", num)
        break
    num += 1
