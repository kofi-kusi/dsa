class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        cur = self.head

        while index != 0:
            cur = cur.next
            index -= 1

        return cur.val


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif self.size == index:
            self.addAtTail(val)
        else:
            new_node = Node(val)

            cur = self.head
            while index != 1:   # move to the node just before the insertion index
                cur = cur.next
                index -= 1

            new_node.next = cur.next
            cur.next.prev = new_node

            cur.next = new_node
            new_node.prev = cur

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            cur = self.head.next
            if cur:
                cur.prev = None
            self.head = cur
            self.size -= 1

            if self.size == 0:
                self.tail = None
        elif index == self.size -1:
            cur = self.tail.prev
            if cur:
                cur.next = None
            self.tail = cur
            self.size -= 1

            if self.size == 0:
                self.head = None
        else:
            cur = self.head

            while index != 1:
                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur

            self.size -= 1


