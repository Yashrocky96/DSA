# LongestSubstringWithoutRepeatingCharacter Solution
def lengthOfLongestSubstring(s):
    # variables needed
    l, r, unique, max_len = 0, 0, set(), 0 

    # End pointer loop
    while r < len(s):
        # Add in set and move right or remove and move left
        if s[r] not in unique:
            unique.add(s[r])
            r += 1
        else:
            unique.remove(s[l])
            l += 1
            
        # At each iter save max_length
        max_len = max(len(unique), max_len)

    return max_len

if __name__ == '__main__':
    s = input()
    result = lengthOfLongestSubstring(s)
    print(result)