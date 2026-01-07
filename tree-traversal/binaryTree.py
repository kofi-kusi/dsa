class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return
        return self.queue[0].value

    def __len__(self):
        return len(self.queue)


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)


    # DSF
    def preorder(self, start, traversal):
        """
        Traverse the tree using the pattern: Root -> Left -> Right
        start: starting node of the traversal (mostly the root)
        traversal (list): an empty list of traversed node values
        Return traversal(list): a list containing the node values from searching
        """
        if start is None:
            return

        traversal.append(start.value)

        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        return traversal

    def inorder(self, start, traversal):
        """
        Traverse the tree using the pattern: Left -> Root ->  Right
        start: starting node of the traversal (mostly the root)
        traversal (list): an empty list of traversed node values
        Return traversal(list): a list containing the node values from searching
        """
        if start is None:
            return

        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)

        return traversal


    def postorder(self, start, traversal):
        """
        Traverse the tree using the pattern: Left -> Right -> Root
        start: starting node of the traversal (mostly the root)
        traversal (list): an empty list of traversed node values
        Return traversal(list): a list containing the node values from searching
        """
        if start is None:
            return

        self.postorder(start.left, traversal)
        traversal.append(start.value)
        self.postorder(start.right, traversal)

        return traversal


    # BFS
    def levelorder(self, start):
        if start is None:
            return

        queue = Queue()
        traversal = []
        queue.enqueue(start)

        while len(queue) > 0:
            traversal.append(queue.peek())

            cur_node = queue.dequeue()

            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)

        return traversal


if __name__ == '__main__':
    bTree = BinaryTree(3)
    bTree.root.left = Node(4)
    bTree.root.left.left = Node(6)
    bTree.root.left.right = Node(7)

    bTree.root.right = Node(5)
    bTree.root.right.left = Node(8)
    bTree.root.right.right = Node(9)

    print(bTree.levelorder(bTree.root))
