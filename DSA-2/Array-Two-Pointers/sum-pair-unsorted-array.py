"""
Find sum pair in unsorted array and return indices
"""

def twoSum(nums, target):
    d = {}

    for i, e in enumerate(nums): 
        # check if pair (e, target - e) exists
        # if the difference is seen before, print the pair
        if target - e in d:
            return [d.get(target - e), i]

        # store index of the current element in the dictionary
        d[e] = i

if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    target = int(input())
    result = twoSum(nums, target)
    print(result[0],result[1])