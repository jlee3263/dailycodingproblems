"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""

class Node():
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def solve(arr):

	mn = Node()
	current = mn
	seen = set() # keep track of which link list has finished looping

	while len(seen) < len(arr):

		smallest = float('inf')
		choice = -1

		for i in range(len(arr)):
			if not arr[i]:
				seen.add(i)
				continue

			if arr[i].val < smallest:
				choice = i
				smallest = arr[i].val

		# update
		if choice != -1:
			current.next = arr[choice]
			current = current.next
			arr[choice] = arr[choice].next
		

	return mn.next


n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n1.next = n2
n2.next = n3

n4 = Node(4)
n5 = Node(8)
n6 = Node(10)
n4.next = n5
n5.next = n6

n7 = Node(5)
n8 = Node(6)
n9 = Node(7)
n10 = Node(50)
n7.next = n8
n8.next = n9
n9.next = n10

h = solve([n1, n4, n7])
while h:
	print(h.val)
	h = h.next


