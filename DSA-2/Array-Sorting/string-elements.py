"""
Using comparators in python is a task
Albeit a simple one
"""

def numSort(n, nums):
    nums.sort(key = int)
    return nums

def main():
    n = int(input())
    nums = input().split()
    result = numSort(n, nums)
    print(*result)

if __name__=="__main__":
    main()