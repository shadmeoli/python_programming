def getPrimes(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


# def rev(vals: str) -> str:
#     return ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

rev = lambda vals: ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

# find missing
'''
    arr1
    arr2 - vals from arr1 but a missing val

    input:  [2, 3, 4, 7, 9] | [2, 4, 7, 9]
    output: 3
'''

def missing(arr1, arr2) -> int:
    return [i for i in arr1 if i not in arr2][0]
    # for idx, i in enumerate(arr1):

    #     if i not in arr2:
    #         return i
    #         break
    #     else:
    #         continue


print(missing([2, 3, 4, 7, 9], [2, 4, 7, 9]))
