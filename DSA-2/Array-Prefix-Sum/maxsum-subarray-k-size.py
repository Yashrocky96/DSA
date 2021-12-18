"""
Using sliding window pattern
"""

def maximumSubarraySumSizeK(arr,n,k):
    l, curr_sum, max_sum = 0, 0, -10e9

    # Loop to k and then slide the window
    for i in range(n):
        curr_sum += arr[i]

        if i >= k-1:
            # Store max sum to get the result
            max_sum = max(curr_sum, max_sum)
            curr_sum -= arr[l]
            l += 1
    return max_sum
   

def main():
    NK = list(map(int,input().strip().split()))
    nums = list(map(int,input().strip().split()))
    
    result = maximumSubarraySumSizeK(nums,NK[0],NK[1])
    print(result)

if __name__=="__main__":
    main()