"""
Given array defines lines that can hold water
mini line will store water, capacity is defined by area
from starting index to line or height we get the max area
"""


def maxArea(height):
    ans = 0
    l, r = 0, len(height) - 1
    while l < r:
        mini = min(height[l], height[r])
        ans = max(ans, mini*(r-l))

        if (height[l] < height[r]): l +=1
        else: r -= 1

    return ans
    
if __name__ == '__main__':
    n = int(input())
    height = input().split()
    height = [int(i) for i in height]
    result = maxArea(height)
    print(result)