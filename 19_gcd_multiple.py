# 19. Program to compute GCD of multiple numbers

import math

nums = list(map(int, input("Enter numbers separated by space: ").split()))

g = nums[0]
for i in nums[1:]:
    g = math.gcd(g, i)

print("GCD of given numbers is:", g)
