def getPrimes(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


# def rev(vals: str) -> str:
#     return ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

reverse = lambda vals: ''.join([vals[len(vals)-1-idx] for idx, i in enumerate(vals)])

# find missing
'''
    arr1
    arr2 - vals from arr1 but a missing val

    input:  [2, 3, 4, 7, 9] | [2, 4, 7, 9]
    output: 3
'''

# def missing(arr1, arr2) -> int:
#     try:
#         return [i for i in arr1 if i not in arr2][0]
#     except:
#         return "Looks fine"
    # for idx, i in enumerate(arr1):

    #     if i not in arr2:
    #         return i
    #         break
    #     else:
    #         continue

missing = lambda arr1, arr2 : [i for i in arr1 if i not in arr2][0]
# print(missing([2, 3, 4, 7, 9], [2, 4, 7, 9]))



def mod_rev(arr):

    res = []
    for i in range(0, len(arr) // 2):
        res.append(arr[i])
        res.append(arr[len(arr)-i-1])
    return res


print(mod_rev([1,2,3,4,5,6,7,8,9]))