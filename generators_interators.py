'''
    Learning iters and generators
'''
import random

def squares(nums):
    for num in nums:
        yield num+random.randint(1, 100)


numbers: list[int] = [
    13, 2, 61, 32, 5, 7, 24, 60
    ]


vals = squares(numbers)

nums = [val for val in vals]
print(nums)


# reccussinve