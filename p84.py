"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def solve(arr):
    
    # let dp[i][j] to be the number of island seened so far till arr[i][j]
    # dp[i][j+1] = dp[i][j] + 1 if 4 cells in upper left, upper, upper right and left surrounding arr[i][j+1] == 0 and arr[i][j+1] == 1
    # dp[i][j+1] = dp[i][j] if any of the 4 cells in upper left, upper, upper right and left surrounding arr[i][j+1] == 1

    dp = [ [ 0 for _ in range(len(arr[0]))] for _ in range(len(arr)) ]

    dp[0][0] = arr[0][0]
    # special case of n * 1 matrix
    if len(arr[0]) == 1:
    	for r in range(1, len(dp)):
    		if arr[r][0] == 0:
    			dp[r][0] = dp[r-1][0]
    		elif arr[r][0] == 1 and arr[r-1][0] == 1:
    			dp[r][0] = dp[r-1][0]
    		else:
    			dp[r][0] = dp[r-1][0] + 1

    	return dp[-1][-1]

    # process first row seperately
    for c in range(1,len(dp[0])):
    	if arr[0][c] == 1 and arr[0][c-1] == 0: # begining of a new island
    		dp[0][c] = dp[0][c-1] + 1
    	else: # is part of a previous island we encounter before
    		dp[0][c] = dp[0][c-1] 

    for r in range(1, len(dp)):
    	for c in range(len(dp[r])):
    		if arr[r][c] == 1:
    			if c == 0:
    				# at starting edge, check upper right and directly above for continuous island
    				if arr[r-1][c] == 1 or arr[r-1][c+1] == 1: 
    					dp[r][c] = dp[r-1][-1] 
    			
    				else: # mark the start of a new island encounter
    					dp[r][c] = dp[r-1][-1] + 1

    			elif c == len(dp[r]) - 1:
    				# at ending edge, check upper left and directly above and prev col for continuous island
    				if arr[r-1][c] == 1 or arr[r-1][c-1] == 1 or arr[r][c-1] == 1:
    					dp[r][c] = dp[r][c-1]

    				else: # mark the start of a new island encounter
    					dp[r][c] = dp[r][c-1] + 1

    			else:
    				# check 4 cells 
    				if arr[r-1][c-1] == 1 or arr[r-1][c] == 1 or arr[r-1][c+1] == 1 or arr[r][c-1] == 1:
    					dp[r][c] = dp[r][c-1]
    				else:
    					dp[r][c] = dp[r][c-1] + 1
    		else:
    			if c == 0:
    				dp[r][c] = dp[r-1][-1]
    			else:
    				dp[r][c] = dp[r][c-1]

    return dp[-1][-1]

arr1 = [
	[1,0,0,0,0],
	[0,0,1,1,0],
	[0,1,1,0,0],
	[0,0,0,0,0],
	[1,1,0,0,1],
	[1,1,0,0,1]
]

print(solve(arr1)) # 4 

arr2 = [
	[0,1,0,0,0],
	[1,0,0,0,0],
	[0,0,1,0,0],
	[0,0,0,0,0],
	[1,1,0,0,1],
	[1,1,0,0,1]
]
print(solve(arr2)) # 4

arr3 = [
	[0],
	[1],
	[0],
	[0],
	[1],
	[1]
]
print(solve(arr3)) # 2



