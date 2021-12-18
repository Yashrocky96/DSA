"""
Max sum subarray from given subarray, also takes care of negative values
"""

def contigiousSequence(arr):
    curr_sum = 0
    max_sum = -10e9-1
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if (max_sum < curr_sum):
            max_sum = curr_sum
 
        if curr_sum < 0:
            curr_sum = 0 
                
    return max_sum


n = int(input())
arr = list(map(int, input().strip().split()))
result = contigiousSequence(arr)
print(result)