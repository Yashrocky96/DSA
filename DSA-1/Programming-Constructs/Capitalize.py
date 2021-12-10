def upper(c):
    #Returns converted uppercase value
    return chr(ord(c) - 32)

def capitalise(s):
    """
    Capitalize all words for a given paragraph.
    Implemented without using split() function
    Converted lower to uppercase by subtracting 32 from ASCII value
    """
    string = str()
    if s[0] != " " or s[0] != ".":
        string += upper(s[0])
    for i in range(1, len(s)):
        if s[i].isupper():
            string += s[i]
        elif s[i-1] == " " or s[i-1] == ".":
            string += upper(s[i])
        else:
            string += s[i]
    return string

# NOTE: Please do not modify this function
def main():
    s = input()
    res = capitalise(s)
    print(res)


if __name__ == "__main__":
    main()
