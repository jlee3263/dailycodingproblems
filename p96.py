"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def solve(l):
	all_res = []
	def helper(choices, res):
		if not choices:
			all_res.append(list(res)) 

		for index, choice in enumerate(choices):
			res.append(choice)
			helper(choices[0:index] + choices[index+1:], res)
			_ = res.pop(-1)


	helper(l, [])
	return all_res


print(solve(([1,2,3])))

