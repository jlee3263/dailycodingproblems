"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""


def solve(x, y, b):

	# if b == 1 -> x
	# if b == 0 -> y

	# convert to truth table -> 2^3 rows 
	# 1,0,1 -> 1
	# 1,1,1 -> 1
	# 0,0,1 -> 0
	# 0,1,1 -> 0
	# there is symmetry so we can just consider above 4

	# suppose we fix b = 1 and ignore y
	# x:1 * 1 => 1 , x:0 * 1 => 0 which is what we want 
	# suppose we fix b = 0 and ignore x => same pattern 
	# somehow involving x*b and y*b 
	# x=1, y=1, b=1 -> x*b | y*b = 1 => ok 
	# x=1, y=0, b=1 -> x*b | y*b = 1 => ok 
	# x=0, y=1, b=1 -> x*b | y*b = 1 => not ok => somehow need to zeroize y*b => y*(1-b) 
	# x=0, y=1, b=1 -> x*b | y*(1-b) = 0 => ok
	# x=0, y=0, b=1 -> x*b | y*(1-b) = 0 => ok

	# x=1, y=1, b=0 -> x*b | y*(1-b) = 1 => ok => 1-b here
	# x=1, y=0, b=0 -> x*b | y*(1-b) = 0=> ok 
	# x=0, y=1, b=0 -> x*b | y*(1-b) = 1 => ok
	# x=0, y=0, b=0 -> x*b | y*(1-b) = 0 => ok

	return x*b | y*(1-b)


print(solve(32,64,1)) # 32
print(solve(32,64,0)) # 64
print(solve(-32,64,1)) # -32
print(solve(32,-64,0)) # -64