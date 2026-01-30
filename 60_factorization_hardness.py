# 60. Program to analyze hardness of prime factorization

n = int(input("Enter a large number n: "))

print("Trying to factorize...")

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("Factors:", i, "and", n // i)
        break
else:
    print("No small factors found. Hard to factorize.")
