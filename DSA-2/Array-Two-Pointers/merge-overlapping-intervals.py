"""
Given intervals in a nested array format 
"""
def overlap(a1, a2):
    """
    This checks if the two intervals passed are overlapping or not
    """
    # print("a1 + a2: {} {}".format(a1, a2))
    if a1[1] >= a2[0]:
        return True
    else:
        return False

def mergeIntervals(nums):
    """
    This creates a stack, sorts the intervals based on starting points given
    For loop checks intervals and creates a new array of merged intervals
    This runs in O(N) time as we run the loop only once
    """
    stack = []
    if len(nums) > 0:
        nums.sort(key=lambda x: x[0])
        stack.append(nums[0])

    for i in nums:
        if overlap(stack[-1], i):
            buff = stack.pop()
            res = [min(buff[0], i[0]), max(buff[1], i[1])]
            stack.append(res)
        else:
            stack.append(i)

    return stack

if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        row = input().split()
        row = [int(i) for i in row]
        nums.append(row)
    result = mergeIntervals(nums)
    for interval in result:
        print(*interval)