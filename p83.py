"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""


class Node():
    def __init__(self, val, left_child=None, right_child=None):
      self.val = val
      self.left_child = left_child
      self.right_child = right_child


root = Node('a')
n1 = Node('b')
n2 = Node('c')
n3 = Node('d')
n4 = Node('e')
n5 = Node('f')


root.left_child = n1
root.right_child = n2
n1.left_child = n3
n1.right_child = n4
n2.left_child = n5

def swap(node):

    if not node:
      return
    swap(node.left_child)
    swap(node.right_child) 
    temp = node.left_child
    node.left_child = node.right_child
    node.right_child = temp


def io(node, sf):
  if node:
    io(node.left_child, sf)
    sf.append(node.val)
    io(node.right_child, sf)

sf = []
io(root, sf)
print("before:", sf)
swap(root)
sf = []
io(root, sf)
print('after:', sf)
