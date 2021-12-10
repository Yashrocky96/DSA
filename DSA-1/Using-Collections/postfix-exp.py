"""
using deque we solve this stack behaviour of postfixExpression
iterate through string append numbers in LIFO format and evaluate when
encountered an operator
"""


from collections import deque

def postfixExpression(expression):
    expression = expression.split()

    stack = deque()

    for ch in expression:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            y = stack.pop()
            x = stack.pop()

            if ch == "+":
                stack.append(x + y)
            elif ch == "-":
                stack.append(x - y)
            elif ch == "*":
                stack.append(x * y)
    return stack.pop()


# NOTE: Please do not modify this function
def main():
    expression = input().strip()
    print(postfixExpression(expression))

if __name__=="__main__":
    main()
