"""
Good morning! Here's your coding interview problem for today.

This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, 
ignoring the remainder.
"""



def solve(dividend, divisor):

	quotient = 0
	while dividend > 0:
		if dividend - divisor >= 0:
			quotient += 1
		dividend -= divisor

	return quotient


print(solve(6,3)) # 2

print(solve(7,3)) # 2

print(solve(100,1)) # 100