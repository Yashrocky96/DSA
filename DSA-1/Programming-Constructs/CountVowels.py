"""
Counting vowels in a string
time complexity: O(n)
"""

def countVowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] in 'AaEeIiOoUu':
            count += 1
    return count

# NOTE: Please do not modify this function
def main():
    s = input()
    res = countVowels(s)
    print(res)


if __name__ == "__main_
