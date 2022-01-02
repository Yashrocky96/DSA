"""
given n distinct numbers there'll be one missing number
solved using n natural numbers and sets
"""

import math

def singleMissingNumber(N,A):
    natural = set(range(N+1))
    A = set(A)
    for ans in (natural - A):
        return ans
    

def main():
    N = list(map(int,input().strip().split()))
    nums = list(map(int,input().strip().split()))
    
    result = singleMissingNumber(N[0],nums)
    print(math.trunc(result))

if __name__=="__main__":
    main()