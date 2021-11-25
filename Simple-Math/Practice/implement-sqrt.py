"""
Explains the internal implementation of sqrt(x) function in math module
"""

def sqrtX(n):
    if n == 0 or n == 1:
        return n
    else:
        start = 0
        end = n
        while (start <= end):
            mid = int((start + end) / 2)
            if (mid*mid == n):
                return mid
            elif (mid*mid < n):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

if __name__ == '__main__':
    n = int(input())
    result = sqrtX(n)
    print(result)
