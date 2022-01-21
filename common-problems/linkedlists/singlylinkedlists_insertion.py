# Inserting a node in singly linked list :
# There are 3 ways by which you can add node in SLL:
# viz : At (1)Beginning (2)End (3)Given Position

start = "beginning"
end = "end"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Singly Linked List is a custom Data-Structure.
    # To print its content we are gaining to use __iter__
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_node(self, position, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if position == start or position == 0:
                new_node.next = self.head
                self.head = new_node
            elif position == end:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < (position - 1):
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


singly_linked_list = SinglyLinkedList()
singly_linked_list.insert_node(start, 1)
singly_linked_list.insert_node(start, 2)
singly_linked_list.insert_node(start, 3)
singly_linked_list.insert_node(start, 4)
singly_linked_list.insert_node(end, 9)
singly_linked_list.insert_node(end, 8)
singly_linked_list.insert_node(5, 4)
print([node.value for node in singly_linked_list])
