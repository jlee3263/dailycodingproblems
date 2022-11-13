"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. 
If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].


Can you perform the operation without allocating extra memory (disregarding the input memory)? ==> No idea how to do in O(1) space

"""



def solve(l):

	# straight forward cases
	# if the digits are descending -> reverse the list 
	# if the digits are acending -> swap last 2 digits

	compare = list(l)
	compare.sort(reverse=True)
	if compare == l:
		l.sort() # sort underlying list
		return l
	
	compare.sort()
	if compare == l:
		l[-2], l[-1] = l[-1], l[-2]
		return l 

	# for other cases, we do a linear scan from right to left and find the first number which is smaller than the number on its right 
	# suppose we generate all permuations and represented by a tree then one of the leaf node is our given list of digits
	# thus scanning from right to left is simulating we are walking up the tree from the leaf node to find the 
	# first parent node which is smaller than the leaf node.

	# once we find the first parent node, we then swap their position, this means that the original child node is now the next bigger number 
	# to replace that parent node. 
	# for example given [1,2,4,3] , 3 is the next bigger number to replace 2 thus it then become [1,3,4,2]
	# after that we need to maintain the lexicographic ordering after "3" ( which just is ascending order in our case as we are given digits)
	# therefore we just need to do a sort in ascending order after 3 to produce [1,3,2,4]

	# scan from right to left
	pos = -1
	for i in range(len(l)-2, -1, -1): # i feel we can start from 2nd last for easier indexing 
		if l[i] < l[i+1]: 
			pos = i # we had found the first digit or parent node to be replaced by the child node and we remember the index position
			break

	# next we swap 
	temp = l[-1]
	l[-1] = l[pos]
	l[pos] = temp 

	# on a side note i think we can replace the above with l[-1], l[pos] = l[pos], l[-1] as python support and we do not need a temp variable
	
	p1 = l[pos+1:] # create a new list
	p1.sort() 
	# change underlying list
	for i in range(0, len(p1)):
		l[pos+i+1] = p1[i]

	return l



print(solve([1,2,3])) # [1,3,2]
print(solve([3,2,1])) # [1,2,3]
print(solve([1,3,2])) # [2,1,3]
print(solve([1,2,4,3])) # [1,3,2,4]
