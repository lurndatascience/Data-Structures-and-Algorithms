# Creation of singly linked list :
# Time and Space complexity of following program will be O(1)
# We won't be printing SLL as it is a custom data structure refer other programs in this folder for that

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


singly_linked_list = SinglyLinkedList()
# Created 2 Nodes
node1 = Node(value=1)
node2 = Node(value=2)

# Head is attached to node1
singly_linked_list.head = node1

# Next node will be node.next i.e. head.next
singly_linked_list.head.next = node2

# Tail will be node2
singly_linked_list.tail = node2
