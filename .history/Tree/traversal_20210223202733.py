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
   r.insertLeft('b')
   r.insertRight('e')

   r.getLeftChild().insertLeft('c')
   r.getLeftChild().insertRight('d')

   r.getRightChild().insertLeft('f')
   r.getRightChild().insertRight('g')

   print(r.getRootVal())
   print(r.getLeftChild().getRootVal())
   print(r.getLeftChild().getLeftChild().getRootVal())


if __name__ == "__main__":
    create_tree()