class Node:
    # Nodes of a directed graph.
    def __init__(self, name):
        self.name = name
        # list of child nodes
        self.children = list()
        self.num_parents = 0
        self.color = "WHITE"  # used for cycle check

    def add_child(self, c_node):
        # add this node as a child of p_node
        if c_node not in self.children:
            self.children.append(c_node)
            c_node.num_parents += 1


class Graph:
    # Represents a directed graph. A user of this class should create
    # all nodes in the graph before adding edges
    def __init__(self):
        self.nodes = list()

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def find_node(self, name):
        for node in self.nodes:
            if name == node.name:
                return node
        return None

    # returns true if a cycle exists in the graph. Using Graph Coloring
    def cycle_check(self):
        cycle = False
        # mark all nodes in graph as unchecked
        for i in range(0, len(self.nodes)):
            self.nodes[i].color = "WHITE"
        for i in range(0, len(self.nodes)):
            # if this node is unchecked, check it and all children
            if self.nodes[i].color == "WHITE":
                cycle = cycle or self.cycle_check_util(self.nodes[i])
        return cycle

    def cycle_check_util(self, node):
        # A WHITE node has not yet been checked.
        # A GREY node has started being checked.
        # A BLACK node has been checked.
        node.color = "GREY"

        # if any adjacent node is GREY, then there is a loop.
        for child in node.children:
            if child.color == "GREY":
                return True
            elif child.color == "WHITE" and self.cycle_check_util(child):
                return True

        # mark node as fully processed
        node.color = "BLACK"
        return False

    # implements topological sort using Khan's Algorithm
    def sort(self):
        # number of parents per node
        degree = list(range(0, len(self.nodes)))
        # nodes that can be added to the sorted list at any time
        queue = list()
        # list of nodes sorted topologically
        sorted_nodes = list()
        for i in range(0, len(self.nodes)):
            degree[i] = self.nodes[i].num_parents
            if degree[i] == 0:
                # this node has no parents, so it may be added to the sorted list.
                queue.append(self.nodes[i])
        while len(queue) != 0:
            # there will be at least one node with no parents because this is a DAG
            first = queue.pop(0)
            sorted_nodes.append(first)
            for child in first.children:
                # find all children of the node we are adding
                for i in range(0, len(self.nodes)):
                    if self.nodes[i] == child:
                        # subtract degree of node
                        degree[i] -= 1
                        if degree[i] == 0:
                            queue.append(child)
        self.nodes = sorted_nodes
