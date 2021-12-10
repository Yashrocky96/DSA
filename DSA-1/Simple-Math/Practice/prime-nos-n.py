"""
This will output the number of prime numbers to a given non negative
number (n)
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

def countPrimes(n):
	ans = 0
	for i in range(n):
		if isPrime(i):
			ans += 1
	return ans

if __name__ == '__main__':
	n = int(input())
	result = countPrimes(n)
	print(result)
