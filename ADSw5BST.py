import math


INT_MAX = math.inf
INT_MIN = -math.inf


class Node:
    def __init__(self, key=0, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(root, node):
    if root.key < node.key:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

#######################################################


def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_max(root):

    if root is None:
        return -math.inf

    if root.left is not None or root.right is not None:
        return max(max(tree_max(root.left), tree_max(root.right)), root.key)
    else:
        return root.key


def _check_BST(root, minimum, maximum):

    if root is None:
        return True

    if root.key < minimum or root.key > maximum:
        return False

    return (_check_BST(root.left, minimum, root.key) and
            _check_BST(root.right, root.key, maximum))


def check_BST(root):
    return _check_BST(root, INT_MIN, INT_MAX)


def _min_diff(root, target=math.inf):
    if root is None:
        return target

    if root.left is not None:
        left = abs(root.key - root.left.key)
        target = min(target, left)

    if root.right is not None:
        right = abs(root.right.key - root.key)
        target = min(target, right)

    left_diff = _min_diff(root.left, target)
    right_diff = _min_diff(root.right, target)
    return min(left_diff, right_diff)


def min_diff(root):
    return _min_diff(root)


def _count_distinct(root, values):

    if root is not None:
        _count_distinct(root.left, values)
        values.add(root.key)
        _count_distinct(root.right, values)


def count_distinct(root):
    unique_values = set()
    _count_distinct(root, unique_values)
    return len(unique_values)
