"""
Using stack idealogy to solve this program
"""

def removeAdjacentDuplicates(s):
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)

def main():
    s = input().strip()

    finalString = removeAdjacentDuplicates(s)
    print(finalString)

if __name__=="__main__":
    main()