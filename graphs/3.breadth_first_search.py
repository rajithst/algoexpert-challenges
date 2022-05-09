# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # use current node as starting node
        # iterate over bfs manner,level-by-level
        q = [self]
        # while queue is not empty
        while len(q) > 0:
            # pop the left most value
            cl = q.pop(0)
            # append name of the node to result array
            array.append(cl.name)
            # add children of current to queue
            for c in cl.children:
                q.append(c)
        return array
