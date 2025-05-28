class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        self.head = new_node


    # add node at the last position
    def insert_end(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node


    def insert_at_position(self, val, pos):
        temp = 1
        new_node = Node(val)
        curr = self.head

        # move to the node just before the required position
        while temp < pos:
            curr = curr.next
            temp += 1

        new_node.next = curr.next
        curr.next = new_node


    # removing a node at an index
    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1

        if curr:
            curr.next = curr.next.next


    def print(self):
        curr = self.head
        while curr:
            print(curr.val, "->")
