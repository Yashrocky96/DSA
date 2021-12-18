"""
Find if any subarray sum up to 0 exists in given arrays
"""

def subarraySumZero(n,arr):
	result = "No"
	prefix_sum = 0
	temp = {}

	for i in range(n):
		prefix_sum += arr[i]
		if prefix_sum == 0:
			return "Yes"
		elif prefix_sum in temp:
			return "Yes"
		else:
			temp[prefix_sum] = i
	return result

def main():
	test=int(input())
	for t in range (test): 
		n= int(input())
		arr = list(map(int,input().strip().split()))
		result=subarraySumZero(n,arr)
		print(result)
                
if __name__ == "__main__":
    main()