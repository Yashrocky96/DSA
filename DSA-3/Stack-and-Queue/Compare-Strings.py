"""
Processing strings and # to backspace the characters given and 
comparing strings to see if the result is correct
"""

def processing(S):
    q = []

    for i in range(len(S)):
        if S[i] != '#':
            q.append(S[i])
        elif len(q) != 0:
            q.pop()
    
    return "".join(q)


def backspaceStringCompare(s1, s2):
    s1 = processing(s1)
    s2 = processing(s2)

    if s1 == s2:
        return "true"
    else:
        return "false"

def main():
    t = int(input().strip())

    for i in range(t):
        s1 = input().strip()
        s2 = input().strip()

        isEqual = backspaceStringCompare(s1, s2)
        print(isEqual)

if __name__=="__main__":
    main()