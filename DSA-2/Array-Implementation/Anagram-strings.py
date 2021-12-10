"""
GIven two strings check if both of them are anagrams of each other
Anagram - means words in real dictionary but for problem's sake
Ingore anagrams real meaning
"""

from collections import Counter

def validAnagram(s, t):
    check = Counter(s)
    check2 = Counter(t)
    if check == check2:
        return True
    else:
        return False

if __name__ == '__main__':
    s = input()
    t = input()
    if validAnagram(s, t):
        print('true')
    else:
        print('false')