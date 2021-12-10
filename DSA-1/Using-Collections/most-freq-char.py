"""
Finds the character that occurs the most includes space, special chars
a-z and A-Z
"""

def mostFrequent(s):
    # Gets the frequency of all characters
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    # calculates max frequency of char from the freq dictionary
    max_char = 0
    max_freq = 0
    for i in freq:
        if freq[i] > max_freq:
            max_char = i
            max_freq = freq[i]
        elif freq[i] == max_freq:
            if ord(i) > ord(max_char):
                max_char = i

    # checks if same max frequency and then compare for lower ascii value
    for i in freq:
        if freq[i] == freq[max_char]:
            if ord(i) < ord(max_char):
                max_char = i
                
    return [max_char, freq[max_char]]


# NOTE: Please do not modify this function
def main():
    s = input()
    res = mostFrequent(s)
    print(*res)


if __name__ == "__main__":
    main()
