def getPrimes(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


# def rev(vals: str) -> str:
#     return ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

rev = lambda vals: ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

print(rev('king'))