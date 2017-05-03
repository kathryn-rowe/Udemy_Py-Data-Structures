# Preorder search
# example: Book, read it in order, from left to right, top to bottom
# Depth-first traversals, or depth-first search (DFS), are algorithms thatf irst
# traverse the structure's by its depth.
# DFS are usually implemented with LIFO structures such as stacks, so
# discovered nodes are tracked. Differently from tree, DFS needs to have a
# structure to mark the visited nodes when traversing graphs (otherwise they
# might be stuck in an infinite loop). The runtime is O(number of reachable
# nodes + total number of outgoing edges from these nodes) = O(V + E).
# DFS comes in three flavors, depending on when you print (or save) the
# current node's value: preorder, postorder, inorder.


def preorder1(tree):
    if tree:
        print (tree.getRootVal())
        preorder1(tree.getLeftChild())
        preorder1(tree.getRightChild())


def preorder2(self):
    print (self.key)

    if self.leftChild:
        self.leftChild.preorder2()
    if self.rightChild:
        self.rightChild.preorder2()

# Postorder search
# example: evaluating a parse tree; traverses left to right, bottom to top


def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print (tree.getRootVal())


# Inorder search
# example: evaluate in exact order, checking children, Binary Search Tree

def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print (tree.getRootVal())
        inorder(tree.getRightChild())

