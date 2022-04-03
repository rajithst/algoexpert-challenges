def findSuccessor(tree, node):
    # for a given node,if given node has a right child,successor is in the right sub-tree
    # since this is inorder-traversal (left,root,right),successor should be left most node
    if node.right:
        return get_left_most_node(node.right)
    # if given node has no right subtree,successor is first ancestor that finished left subtree
    return get_first_parent_finished_left_subtree(node)


def get_left_most_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def get_first_parent_finished_left_subtree(node):
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent
