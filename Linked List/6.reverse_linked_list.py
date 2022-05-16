# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    previous = None
    next_node = None
    while head:
        next_node = head.next
        head.next = previous
        previous = head
        head = next_node
    return previous
