'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
'''


def solve2(m):

	characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's', 't','u','v','w','x','y','z']
	numbers = { characters[i]: i for i in range(len(characters)) }

	rows = len(m)
	cols = len(m[0])
	d = 0 
	for c in range(0, cols):
		for r in range(1, rows):
			curr = m[r][c] 
			prev = m[r-1][c]
			if numbers[curr] < numbers[prev]:
				d+=1 
				continue

	return d


def solve(m):

	rows = len(m)
	cols = len(m[0])
	d = 0 
	for c in range(0, cols):
		for r in range(1, rows):
			curr = m[r][c] 
			prev = m[r-1][c]
			if curr < prev: # p3 can comapre letters directly wrt to their alphabetical order
				d+=1 
				continue

	return d


print(solve(["cba", "daf", "ghi"]))
print(solve(["abcdef"]))
print(solve(["zyx", "wvu", "tsr"]))




