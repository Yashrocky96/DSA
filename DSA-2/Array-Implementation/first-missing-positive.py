"""
Find the first missing positive number from a given array
"""

def firstMissingPositive(nums):
    n = len(nums)
    # Convert all negative and 0 numbers to largest prime integer value
    for i in range(n):
        if nums[i] < 1:
            nums[i] = 1e9 + 7
    # Convert all indexth values to -ve
    for i in range(n):
        try: 
            nums[abs(nums[i])] *= -1
        except:
            pass

    # loop to n and find the index value which isn't negative is our answer
    for i in range(1, n):
        if nums[i] > 0:
            return i
    return n+1

if __name__ == '__main__':
    n = int(input())
    nums = []
    if n > 0:
        nums = input().split()
        nums = [int(i) for i in nums]

    result = firstMissingPositive(nums)
    print(result)