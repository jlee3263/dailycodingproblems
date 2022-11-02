"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""



def solve(s):

	# every "(" must mapped to a ")" 
	# therefore only 2 cases to consider 
	# - remove unmatching "(" 
	# - remove unmatching ")"


	stack = []
	remove = 0

	# loop once to count ")" to be remove
	for i in s:
		if i == "(":
			stack.append(i)
		else:
			if stack:
				_ = stack.pop(-1) # matching "(" for ")"
			else:
				remove += 1 # unmatched ")" to be removed

	# whatever "(" left in the stack are meant to be removed too
	return len(stack) + remove


print(solve("()())()")) # 1
print(solve(")(")) # 2
