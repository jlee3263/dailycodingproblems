'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

def solve(arr):

	l = []

	arr.sort(key=lambda x: x[0])
	l.append(arr[0])

	for i in range(1, len(arr)):
		if arr[i][0] >= l[-1][1]:
			l.append(arr[i])

	return l


print(solve([(1, 3), (5, 8), (4, 10), (20, 25)]))