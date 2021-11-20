"""
 Recursive method to find the greatest common divisor of two numbers
 Co-prime numbers function to get the number of co-primes a number has
 Co-prime is a number that has gcd 1 only
"""
def gcd(a, b):
    if (b == 0):
         return a
    return gcd(b, a%b)

def coprimeNumbers(n):
    result = 0
    for i in range(1, n+1):
        if gcd(i, n) == 1:
            result += 1
    return result


# NOTE: Please do not modify this function
def main():
    n = int(input().strip())

    countCoPrime = coprimeNumbers(n)
    print(countCoPrime)


if __name__ == "__main__":
    main()
