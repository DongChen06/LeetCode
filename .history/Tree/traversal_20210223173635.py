import sys
sys.path.append("../")

from tree.binary_tree import BinaryTree

"""
we will create a binary tree looks like,
         a
      /      \
     b        e
   /   \    /   \
   c   d   f     g

Then use three traversal methods to traverse the tree
"""

def create_tree():
   # create the binary tree
   r = BinaryTree('a')

   b = BinaryTree('b')
   b.insertLeft('c')
   b.insertRight('d')

   e = BinaryTree('e')
   e.insertLeft('f')
   e.insertRight('g')

   r.insertLeft(b)
   r.insertRight(e)

   print(r.getRootVal())
   print(r.getLeftChild().getRootVal())

if __name__ == "__main__":
    create_tree()