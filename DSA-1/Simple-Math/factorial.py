"""
Simple Factorial function
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = factorial(n)
    print(ans)


if __name__ == "__main__":
    main()
