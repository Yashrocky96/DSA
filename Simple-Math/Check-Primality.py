"""
For given n number we find if the number is a prime number or not.
here check condition checks on square of the number so time complexity
become sqrt(number)
"""

def isPrime(n):
    # Checks if n is a prime number or not in log n time complexity
    if n <= 1:
        return False
    else:
        p = 2
        while p*p <= n:
            if (n % p) == 0: return False
            else: p += 1

    return True

def checkPrime(t, nums):
    result = []

    for i in range(t):
        result.append(isPrime(nums[i]))
    return result

# NOTE: Please do not modify this function
def main():
    t = int(input())
    nums = []
    for i in range(0,t):
        n = int(input())
        nums.append(n)
    ans = checkPrime(t,nums)

    for i in ans:
        if(i == False):
            print("false")
        else:
            print("true")


if __name__=="__main__":
    main()
