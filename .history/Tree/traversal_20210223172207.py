from Tree.binary_tree import BinaryTree

"""
         a
      /      \
     b        e
   /   \    /   \
   c   d   f     g

"""


r = BinaryTree('a')

b = BinaryTree('b')
b.insertLeft('c')
b.insertRight('d')

e = BinaryTree('e')
e.insertLeft('f')
e.insertRight('g')

r.insertLeft(b)
r.insertRight(e)
