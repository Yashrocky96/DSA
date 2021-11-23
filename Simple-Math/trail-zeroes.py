"""
Shows the trailing zeroes of a given number of a factorial
Using exponentiation to derive formula to solve it in log n base 5 time
"""

def findTrailingZeros(n):
    count = 0
    if n == 5:
        return 1
    i = 5
    while n/i > 1:
        count += n//i
        i *= 5
    return count

n = int(input())
result = findTrailingZeros(n)
print(result)
