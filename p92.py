"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

class Node():
	def __init__(self, val):
		self.val = val
		self.neigs = []

# dfs 
def dfs(node, s, visited):
	if visited[node.val]:
		return

	visited[node.val] = True
	for neig in node.neigs:
		dfs(neig, s, visited)

	s.append(node.val)


def  solve(m):

	# use topological sorting 

	s = []
	visited = {}

	# create the graph
	nodes = {}
	for k, pres in m.items():
		n = nodes.get(k, Node(k))
		nodes[k] = n 
		visited[k] = False
		for pre in pres:
			nn = nodes.get(pre, Node(pre))
			n.neigs.append(nn)
			nodes[pre] = nn
			visited[pre] = False

	for _, n in nodes.items():
		dfs(n, s, visited)
	return s


print(solve({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []})) # ['CSC100', 'CSC200', 'CSCS300']




