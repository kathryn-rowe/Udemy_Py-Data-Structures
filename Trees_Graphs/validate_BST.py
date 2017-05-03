class BinaryTree(object):

    def __init__(self, root):

        self.data = root
        self.leftChild = None
        self.rightChild = None

validate_tree = BinaryTree("example")
# implied that tree includes many other set-ups and nodes

tree_vals = []


def inorder(tree):
    if tree is not None:
        inorder(tree.leftChild)
        tree_vals.append(tree.root.data)
        inorder(tree.rightChild)


def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

inorder(validate_tree)
sort_check(validate_tree)
