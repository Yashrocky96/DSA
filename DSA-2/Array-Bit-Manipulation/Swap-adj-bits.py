"""
Swaps adjacent bits of a given number in O(1) time as
we are running the loop to a defined number of times
"""

def swap_all_odd_and_even_bits(n):
    for i in range(31, -1, -2):
        # Checks if i bit is > 0
        if n & (1 << i) > 0:
            a = 1
        else: a = 0

        # Checks if i-1 bit is > 0
        if n & (1 << (i-1)) > 0:
            b = 1
        else: b = 0
        
        # Check if a and b are different and then perform
        # XOR on different bits to swap them

        if (a != b):
            n = n ^ (1 << i)
            n = n ^ (1 << i-1)
    return n

        

def main():
    n = int(input())
    answer = swap_all_odd_and_even_bits(n)
    print(answer)

if __name__ == "__main__":
    main()