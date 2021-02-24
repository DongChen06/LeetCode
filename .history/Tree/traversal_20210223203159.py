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
   r = BinaryTree('book')
   r.insertLeft('chapter1')
   r.insertRight('chapter2')

   r.getLeftChild().insertLeft('section1.1')
   r.getLeftChild().insertRight('section1.2')

   r.getRightChild().insertLeft('section2.1')
   r.getRightChild().insertRight('section2.2')

   print(r.getRootVal())
   print(r.getLeftChild().getRootVal())
   print(r.getLeftChild().getLeftChild().getRootVal())


def preorder_traversal(tree):
       if tree:
         print(tree.getRootVal())
         preorder_traversal(tree.getLeftChild)
         preorder_traversal(tree.getRightChild)


def inorder_traversal(root):
       pass

def postorder_traversal(root):
       pass


if __name__ == "__main__":
    create_tree()

