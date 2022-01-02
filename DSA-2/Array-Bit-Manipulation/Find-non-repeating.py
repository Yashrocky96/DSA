"""
Using XOR we get the XOR of two non repeating numbers
and by checking with leftmost set bit we separate all numbers
in the array and perform XOR so we get the two values
"""

def twoNonRepeatingNumbers(n,arr):
    res = 0
    # XOR all numbers in arr to get XOR for result array
    for i in range(n):
        res ^= arr[i]
    # Gets left most set bit of the result
    leftSet = res & ~(res - 1)
    
    # Dividng arrays by set and unset bits using left most set
    # will result in two non repeating numbers in O(n) time

    x, y = 0, 0
    for i in range(n):
        # Set bits
        if (arr[i] & leftSet) > 0:
            x ^= arr[i]
        # Unset bits at the left most position
        else:
            y ^= arr[i]
    # Self-explanatory code below
    ans = [x, y]
    ans.sort()
    return ans

def main():
    N = list(map(int,input().strip().split()))
    nums = list(map(int,input().strip().split()))
    
    result = twoNonRepeatingNumbers(N[0],nums)
    for i in range(0, len(result)):
        print(result[i], end =" ")

if __name__=="__main__":
    main()