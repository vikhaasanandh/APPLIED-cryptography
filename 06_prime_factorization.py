#6.Program to perform prime factorization of a given integer

n = int(input("Enter a number: "))
temp = n
print("Prime factors of", n, "are:")
i = 2
while i <= temp:
    while temp % i == 0:
        print(i, end=" ")
        temp = temp // i
    i += 1
