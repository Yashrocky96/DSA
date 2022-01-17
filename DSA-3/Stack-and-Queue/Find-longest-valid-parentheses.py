"""
This functions gives the longest valid parenthese value
"""

def longestValidParentheses(s):
    # Base variable and condition
    res = 0
    stack = []
    # Base value of stack
    stack.append(-1)

    for i in range(len(s)):
        # insert index of open parentheses in stack
        if s[i] == '(':
            stack.append(i)
        else:
            # closing parentheses pop
            if len(stack) > 0:
                stack.pop()

            # store longest valid substring with top value of stack
            if len(stack) > 0:
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
    return res

def main():
    S = input()
    ans = longestValidParentheses(S)
    print(ans)

if __name__=="__main__":
    main()