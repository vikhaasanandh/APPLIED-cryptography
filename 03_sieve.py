#3. Program to implement Sieve of Eratosthenes for prime number generation 
n = int(input("Enter the limit: "))
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False
print("Prime numbers up to", n, "are:")
for i in range(2, n + 1):
    if prime[i]:
        print(i, end=" ")