class Node:
    # Nodes of a directed graph.
    def __init__(self, name):
        self.name = name
        self.edges = list()
        self.parents = 0
        self.color = "WHITE"  # used for cycle check

    def add_edge(self, e):
        # add the child node
        self.edges.append(e)
        e.add_parent()

    def add_parent(self):
        self.parents += 1


class Graph:
    # Represents a directed graph. A user of this class should create
    # all nodes in the graph before adding edges
    def __init__(self):
        self.nodes = list()

    def add_node(self, node):
        self.nodes.append(node)

    def find_node(self, name):
        for node in self.nodes:
            if name == node.name:
                return node
        return None

    def cycle_check(self):
        # returns true if a cycle exists in the graph
        for i in range(0, len(self.nodes)):
            self.nodes[i].color = "WHITE"
        for i in range(0, len(self.nodes)):
            if self.nodes[i].color == "WHITE":
                return self.cycle_check_util(self.nodes[i])

    def cycle_check_util(self, node):
        # A WHITE node has not yet been checked.
        # A GREY node has started being checked.
        # A BLACK node has been checked.
        node.color = "GREY"

        # if any adjacent node is GREY, then there is a loop.
        for child in node.edges:
            if child.color == "GREY":
                return True
            elif child.color == "WHITE" and self.DFSUtil(child):
                return True

        # mark node as fully processed
        node.color = "BLACK"
        return False

    # implements topological sort using Khan's Algorithm
    def sort(self):
        # number of parents per node
        degree = list()  # should be the size of self.nodes
        # nodes that can be added to the sorted list at any time
        queue = list()
        # list of nodes sorted topologically
        sorted = list()
        for i in range(0, len(self.nodes)):
            degree[i] = self.nodes[i].parents
            if degree[i] == 0:
                # this node has no parents, so it may be added to the sorted list.
                queue.append(self.nodes[i])
        while len(queue) != 0:
            # there will be at least one node with no parents because this is a DAG
            first = queue.pop(0)
            sorted.append(first)
            for child in first.edges:
                # find all children of the node we are adding
                for i in range(0, len(self.nodes)):
                    if self.nodes[i] == child:
                        # subtract degree of node
                        degree[i] -= 1
                        if degree[i] == 0:
                            queue.append(child)
        self.nodes = sorted
