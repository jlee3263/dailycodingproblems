"""
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than 
or equal to the root and the key in the right child must be greater than or equal to the root
"""


class Node():
	def __init__(self, val):
		self.val = val
		self.left_child = None
		self.right_child = None


def solve(node):

	if node and not node.left_child and not node.right_child:
		return True

	if node:

		l = solve(node.left_child)
		r = solve(node.right_child)

		return node.left_child.val <= node.val and node.right_child.val >= node.val and l and r

	return False




n1 = Node(3)
n2 = Node(2)
n3 = Node(4)

n1.left_child = n2
n1.right_child = n3
print(solve(n1)) # True



n4 = Node(3)
n5 = Node(2)
n6 = Node(1)

n4.left_child = n5
n4.right_child = n6
print(solve(n4)) # False


n7 = Node(3)
n8 = Node(2)
n9 = Node(4)
n10 = Node(2)
n11 = Node(7)

n7.left_child = n8
n7.right_child = n9

n8.left_child = n10
n8.right_child = n11

print(solve(n7)) # True


n7 = Node(1)
n8 = Node(2)
n9 = Node(4)
n10 = Node(99)
n11 = Node(7)

n7.left_child = n8
n7.right_child = n9

n8.left_child = n10
n8.right_child = n11


print(solve(n7)) # False

