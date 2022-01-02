"""
This is a simple approach
"""

# def numberOfOneBits(n):
# 	count = 0
# 	# Checking all bits are 1 or not and adding count
# 	for i in range(31, -1, -1):
# 		# Using left shift and bit masking
# 		if n & (1 << i) > 0:
# 			count += 1

# 	return count

"""
This is the optimatl approach
"""

def numberOfOneBits(n):
	count = 0
	while n:
		n &= (n-1)
		count += 1
		
	return count

def main():
	n = int(input())
	result = numberOfOneBits(n)
	print(result)

if __name__=="__main__":
	main()