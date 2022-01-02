"""
Using Binary search we find nth root of a given number
"""

def power(a, b):
    product = 1
    x = a
    while b > 0:
        if b % 2 == 1:
            product *= x
            if product > 10**9:
                return product
        b //= 2
        x **= 2
    return product

def nthRoot(x, n):
    low, high = 0, x
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        midPowerN = power(mid, n)
        if midPowerN <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def main():
    test = int(input())
    output = ""
    for t in range(test):
        x, n = list(map(int, input().split()))
        result = nthRoot(x, n)
        output += str(result) + "\n"
    print(output)

if __name__=="__main__":
    main()