"""
Calculates number of factors of a number and their sum
"""

def numberOfDivisorsAndSum(n):
    factors = set()
    i = 1
    while (i**2) <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
        i += 1
    out = [len(factors), sum(factors)]
    return out

# NOTE: Please do not modify this function
def main():
    n = int(input())
    list=numberOfDivisorsAndSum(n)
    print(*list)

if __name__=="__main__":
    main()
