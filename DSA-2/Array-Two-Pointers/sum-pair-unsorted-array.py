"""
Find sum pair in unsorted array and return indices
"""

def twoSum(nums, target):
    buff = {}

    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    target = int(input())
    result = twoSum(nums, target)
    print(result[0],result[1])