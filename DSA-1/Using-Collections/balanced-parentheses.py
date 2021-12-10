"""
Checks if the parentheses opens and closes in the correct order
"""

from collections import deque

stack = deque()

# Implement your solution here
def isValid(s):
	if not s:
		return "true"

	balance = {
		"}": "{",
		")": "(",
		"]": "["
	}

	for i in s:
		if i in balance.values():
			stack.append(i)
		elif stack:
			if balance[i] == stack[-1]:
				stack.pop()
			else:
				return "false"
		else:
			return "false"

	if stack:
		return "false"
	else:
		return "true"

if __name__ == '__main__':
	s = input().strip()
	result = isValid(s)
	print(result)
