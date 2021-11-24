class Node:
    def __init__(self, i, j):
        self.pos = (i,j)
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def remove_neighbour(self, node):
        self.neighbours.remove(node)


