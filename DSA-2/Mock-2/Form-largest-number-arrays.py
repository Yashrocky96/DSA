"""
Using arrays form largest number by arranging the given numbers in that order
Here we used comparator function from functools module
to sort the strings in that order.
"""
import functools

def comp(x,y):
    str1 = str(x)+str(y)
    str2 = str(y)+str(x)
    if str1>str2:
        return -1
    else: return 1
    
def largestNumber(nums):
    nums.sort(key=functools.cmp_to_key(comp))
    nums = int("".join(map(str, nums)))
    
    return nums
    
if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    result = largestNumber(nums)
    print(result)