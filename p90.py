"""

Good morning! Here's your coding interview problem for today.

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

"""

import random

def solve(n, l):

	shuffle_list = [ i for i in range(0, n) if i not in l]

	random.shuffle(shuffle_list)
	return shuffle_list[0]


print(solve(100, [ i for i in range(10, 100)])) # output between [0,9]

print(solve(100, [ i for i in range(0, 100) if i%2 == 0 ])) # output only odd number from [0,100]


