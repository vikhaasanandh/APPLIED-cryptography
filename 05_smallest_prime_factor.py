#5.Program to find the smallest prime factor of a given number

n = int(input("Enter a number: "))

if n <= 1:
    print("Smallest prime factor does not exist for", n)
else:
    for i in range(2, n + 1):
        if n % i == 0:
            print("Smallest prime factor of", n, "is:", i)
            break