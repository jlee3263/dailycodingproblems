"""
https://twitter.com/mathisstillfun/status/1585327090454638592?s=20&t=f5s1PnzQMiXZTSQQfg6tOQ

A barcode is made up of alternate black and white stripes. 
The code always starts and ends with a black stripe.  <---- constraint
Each strip (black or not) has a width 1 or 2 and the total width of the barcode is 12. 
How many different barcodes are there if one reads from left to right?


start with black , alternate between black and white and end with black implies odd number of bars
2 types of bar: 1 or 2 units
Let x be number of 1 unit bar and y be number of 2 units bar

constraints
x + 2y = 12
x + y = 2k + 1 

possibilities
(x=2 , y=5) => valid
(x=4, y=4) => not valid as x+y = 2k
(x=6, y=3) => valid
(x=8, y=2) => not valid
(x=10, y=1) => valid


therefore 3 cases: 7C2 + 9C3 + 11C1 =  21 + 84 + 11 = 116

"""


# recursive -> O(2^n)
def solve(n):

	def helper(w, res):

		# the sequence had to be BWBW...B => implies there are odd number of bars

		if w == 0 and (res[-2:] == 'b1' or res[-2:] == 'b2'):
			return 1

		if w <= 0:
			return 0

		if 'w' in res[-2:] or not res:
			return helper(w-1, res + 'b1') + helper(w-2, res + 'b2')

		return helper(w-1, res + 'w1') + helper(w-2, res + 'w2')

	return helper(n, "")


# bottom up -> O(n)
def solve2(n):

	# 0 - black , 1 - white
	# let dp[i][n] = number of ways ending with colour i with width n
	# recurrent case
	# dp[1][n] = dp[0][n-2] + dp[0][n-1] 
	# dp[0][n] = dp[1][n-2] + dp[1][n-1]
	
	dp = [ [0 for _ in range(n+1)] for _ in range(2) ]

	# base cases
	dp[0][1] = 1 # b1
	dp[0][2] = 1 # b1b1 
	dp[1][2] = 1 # b1w1 special case to make the accumulation corrrect

	for col in range(3, n+1):
		dp[1][col] = dp[0][col-2] + dp[0][col-1] 
		dp[0][col] = dp[1][col-2] + dp[1][col-1] 

	return dp[0][-1]

print(solve(12)) 
print(solve2(12))





