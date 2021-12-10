"""
Calculates a exponential number modulo by (1e9+7) that is 10^9 + 7
10^9 + 7 is a prime number: Generally used in competitive programming
To define limits for programming languages like C, C++, Java, etc.
"""

def modularExponentiation(num, power):
    mod = int(1e9 + 7)
    num = num**power
    num = num%mod
    return num

# NOTE: Please do not modify this function
def main():
    num, power = map(int, input().split(' '))
    ans = modularExponentiation(num, power)
    print(ans)


if __name__ == "__main__":
    main()
