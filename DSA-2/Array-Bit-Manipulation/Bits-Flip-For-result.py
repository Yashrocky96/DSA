"""
This is used to get the number of bits to be flipped to conver a to b
"""

def numberOfOneBits(n):
	count = 0
	while n:
		n &= (n-1)
		count += 1
		
	return count

def countConversionBits(a, b):
    # Counting number of bits in XOR of a & b gives the answer

    return numberOfOneBits(a ^ b)


def main():
    a, b = map(int, input().split())
    answer = countConversionBits(a, b)
    print(answer)

if __name__ == "__main__":
    main()