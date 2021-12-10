"""
This program finds number of numberOfPrimesInARange
"""

def isPrime(n):
    if n <= 1:
        return False
    else:
        p = 2
        while p*p <= n:
            if (n % p) == 0: return False
            else: p += 1
    return True

def numberOfPrimesInARange(l, r):
    count = 0
    for i in range(l, r+1):
        if isPrime(i):
            count += 1
    return count

# NOTE: Please do not modify this function
def main():
    rangeInput = input().split(' ')
    l = int(rangeInput[0])
    r = int(rangeInput[1])
    ans = numberOfPrimesInARange(l, r)
    print(ans)


if __name__ == "__main__":
    main()
