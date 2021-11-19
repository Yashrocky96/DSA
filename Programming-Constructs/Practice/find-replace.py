"""
Given a character to replace with another given character
Converted string to list and back to string for this problem 
"""

def find_replace(s, pat1, pat2):
    string = list(s)
    for i in range(len(string)):
        if string[i] == pat1:
            string[i] = pat2
    return "".join(string)


def main():
    s = input()
    print(find_replace(s, ' ', '%20'))

if __name__ == '__main__':
   main()
