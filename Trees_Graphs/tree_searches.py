# Preorder search
# example: Book, read it in order, from left to right, top to bottom


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
# example: evaluate in exact order, checking children

def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print (tree.getRootVal())
        inorder(tree.getRightChild())

