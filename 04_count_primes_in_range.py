#4.Program to count prime numbers within a given range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
count = 0
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
print("Number of prime numbers between", start, "and", end, "is:", count)