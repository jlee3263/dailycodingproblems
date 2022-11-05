"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.

"""


class Node():
	def __init__(self, label):
		self.label = label
		self.N = []
		self.S = []
		self.E = []
		self.W = []
		self.m = {
			"N": self.N,
			"S": self.S,
			"E": self.E,
			"W": self.W
		}

	def print_neighbours(self):
		print("local:", self.label)
		for k, d in self.m.items():
			for n in d:
				print(k, ":", n.label)


def is_loop(current_node, exit_gate, starting_node_label):

	if exit_gate == 'N':
		neigbours = [node.label for node in current_node.N]
		neigbour_nodes = [node for node in current_node.N]
	elif exit_gate == 'S':
		neigbours = [node.label for node in current_node.S]
		neigbour_nodes = [node for node in current_node.S]
	
	elif exit_gate == 'E':
		neigbours = [node.label for node in current_node.E]
		neigbour_nodes = [node for node in current_node.E]
	elif exit_gate == 'W':
		neigbours = [node.label for node in current_node.W]
		neigbour_nodes = [node for node in current_node.W]

	if starting_node_label in neigbours:
		print("loop detected!")
		print("starting_node_label:", starting_node_label)
		print("current_node_label:", current_node.label, "Gate:", exit_gate, "connected back to", starting_node_label)
		return True
	
	for neigbour_node in neigbour_nodes:
		maybe = is_loop(neigbour_node, exit_gate, starting_node_label)
		if maybe:
			return True
	return False
 
def is_validate(rules):

	# from example2, it does not matter A NW B or A N B
	# by convention, we used NE, NW, SE, SW for cardinal positions => we can ignored the 2nd letter (example take NE as N)
	
	# idea:
	# each node has 4 cardinal points (N,S,E,W)
	# every rule will create 2 new nodes and connect them accordingly
	# if nodes exists, then just connect accordingly 
	# example: 
	# A N B -> B:North <---> South:A (B:north is facing A, A:South is facing B) 
	# A N Z -> A:South <---> [ North:Z, North:B ] (A:South is also facing Z) 
	# here, we assume each cardinal "gate" can be connected to one or more nodes   

	# how to detect invalid rules ?
	# note: legal rules will create rules which does not cause any loops, therefore once a loop detected => rule is not legal
	# refer to the diagram_p87.png for illustration

	nodes = {}

	for rule in rules:
		n1 , pos, n2 = rule.split()
		pos = pos[0] # only care about the first direction
		#print(n1, pos, n2)
		n1_node = nodes.get(n1, Node(n1))
		n2_node = nodes.get(n2, Node(n2))
		if pos == 'N':
			# n1 is north of n2
			n1_node.S.append(n2_node)
			n2_node.N.append(n1_node)
			if is_loop(n1_node, "S", n1):
				return False

		elif pos == "S":
			# n1 is south of n2
			n1_node.N.append(n2_node)
			n2_node.S.append(n1_node)
			if is_loop(n1_node, "N", n1):
				return False

		elif pos == "E":
			# n1 is east of n2
			n1_node.W.append(n2_node)
			n2_node.E.append(n1_node)
			if is_loop(n1_node, "W", n1):
				return False

		elif pos == "W":
			# n1 is west of n2
			n1_node.E.append(n2_node)
			n2_node.W.append(n1_node)
			if is_loop(n1_node, "E", n1):
				return False

		nodes[n1] = n1_node
		nodes[n2] = n2_node
	return True

rules1 = [
  "A N B",
  "B NE C",
  "C N A"
]


print(is_validate(rules1)) # False

rules2 = [
 "A NW B",
  "A N B"
]

print(is_validate(rules2)) # True



rules3 = [

 "A N B", 
 "B N C", 
 "C N D",
 "D N E",
 "E N F",
 "A N F"

]

# some website (https://cppcodingzen.com/?p=2059) say that the above is False/Invalid as "A N F" will create a loop. 
# imo , i think is valid because the above relative position can translated into a sequence of inequality as follows
# A > B > C > D > E > F 
# A > F is a valid statement 

print(is_validate(rules3)) # True




rules3 = [

 "A N B", 
 "B N C", 
 "C N D",
 "D N E",
 "E N F",
 "A S F"

]

print(is_validate(rules3)) # False