"""
Given a number this finds the next number greater to it
"""


def nextGreaterElementWithSameSetOfDigits(n):
    res = -1
    n = list(map(lambda x: int(x), list(str(n))))

    # Finding small digit to for solution
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            break

    # That is all numbers are in descending, Not possible
    if i == 1 and n[i] <= n[i-1]:
        return res

    # Found the right most
    x = n[i-1]
    smallest = i

    # Finding the next smallest digit in the number
    for j in range(i+1, len(n)):
        if n[j] > x and n[j] < n[smallest]:
            smallest = j

    # Swapping the digits
    n[smallest],n[i-1] = n[i-1], n[smallest]

    # Converting string to int
    X = 0
    for j in range(i):
        X = X * 10 + n[j]
    # Instead of sorting, reversing after i-1 digits
    n = sorted(n[i:])

    # Remaining digits conversion
    for j in range(len(n)):
        X = X * 10 + n[j]

    return X

def main():
    n = int(input())
    print(nextGreaterElementWithSameSetOfDigits(n))

if __name__=="__main__":
    main()