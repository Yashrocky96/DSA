"""
Using bit operators we reverse binary representation
instead of converting to string and performing reverse
"""

def reverseBits(n):
    res = 0
    for _ in range(32):
        # Left shift result
        res <<= 1
        # Check if last digit is set and toggle res last bit
        if (n & 1) == 1:
            res ^= 1
        # Remove last bit
        n >>= 1
    return res
        

def main():
    T = int(input())
    for test in range(T):
        n = int(input())
        result = reverseBits(n)
        print(result)

if __name__=="__main__":
    main()