# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, visited, node_value):
        self.visited = visited
        self.node_value = node_value


def findKthLargestValueInBst(tree, k):
    info = TreeInfo(0, -1)
    reverseInOrder(tree, info, k)
    # finally return tree info node_value ,the kth largest value
    return info.node_value


def reverseInOrder(node, info, k):
    # if a leaf node or visited nodes are >= k,return from the function
    if not node or info.visited >= k:
        return
    # go to right subtree as deep as possible,that is the largest value
    reverseInOrder(node.right, info, k)
    # before backtracking,check if number of visited nodes are completed
    # only if visited nodes are less than k,we need to check left tree
    # since this is backtracking,we can update visited count and last visited node value
    if info.visited < k:
        info.visited += 1
        info.node_value = node.value
        reverseInOrder(node.left, info, k)