# Implements a tree using lists

# myTree = ['a', #root
#            ['b', #left subtree
#              ['d', [], [] ],
#              ['e', [], [] ]
#            ],
#            ['c', #right subtree
#              ['f', [], [] ],
#              []
#            ]
#          ]


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insertRight(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


