"""
Compressing strings to save space when dealing with
repeated subsequent alphabets (a-zA-z) in a string
"""

def compress(s):
    result = str()
    i = 0
    # We use one counter and two loops for T.C: O(n)
    while i < (len(s) - 1):
        count = 1
        while i < (len(s) - 1) and s[i] == s[i+1]:
                count += 1
                i += 1
        result += s[i] + str(count)
        i += 1

    """
    Checks edge cases and returns original string
    if string cannot be compressed
    """
    if len(result) == len(s):
        return s
    elif len(result) < len(s):
        for i in range(1, len(result), 2):
            if result[i] == 1:
                pass
            else:
                return result
    return s

s = input().strip()
result = compress(s)
print(result)
