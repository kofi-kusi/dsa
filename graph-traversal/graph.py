class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self.visited = False


# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, node):
#         self.queue.append(node)
#
#     def dequeue(self):
#         return self.queue.pop(0)
#
#     def __len__(self):
#         return len(self.queue)

class Graph:
    def BFS(self, node):
        queue = []
        traversal = []
        queue.append(node)

        while queue:
            cur_node = queue.pop(0)
            traversal.append(cur_node.value)

            for element in cur_node.adjacent_list:
                if not element.visited:
                    queue.append(element)
                    element.visited = True

        return traversal

    def DFS(self, node, traversal):
        node.visited = True
        traversal.append(node.value)

        for element in node.adjacent_list:
            self.DFS(element, traversal)

        return traversal



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)

graph = Graph()
print(graph.BFS(node1))
print(graph.DFS(node1, []))

