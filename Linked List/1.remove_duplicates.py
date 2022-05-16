# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    previous = None
    while head:
        if previous and head.value == previous.value:
            previous.next = head.next
        else:
            previous = head
        head = head.next
    return linkedList
