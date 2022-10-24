'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def solve(arr):

	gmax = 1
	dp = [1 for _ in range(len(arr))]

	for i in range(0, len(arr)):
		for j in range(0, i):
			if arr[i] > arr[j]:
				maybe = dp[j] + 1
				dp[i] = max(maybe, dp[i])
				gmax = max(gmax, dp[i])

	return gmax

print(solve([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(solve([14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(solve([10, 22, 9, 33, 21, 50, 41, 60]))