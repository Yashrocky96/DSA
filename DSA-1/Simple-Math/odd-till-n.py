"""
Gives all odd numbers in a line upto a given number
"""

def oddNumbers(n):
    result = []
    for i in range(1, n+1, 2):
        result.append(i)
    return result

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = oddNumbers(n)
    print(*ans)


if __name__ == "__main__":
    main()
