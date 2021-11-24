"""
A node is defined as a point in the maze where a choice has to be made to go in a different direction
or a point which the line has to change direction to move on.
Start and End nodes only have one line connecting to them, whilst body nodes are connected to 2 to 4 lines and therefore 2 to 4 nodes.

"""
from nodes import *

def start_end_nodes(matrix):# Finds the start and end point, then creates Start and End nodes.
    for i in range(len(matrix[0])):
        if matrix[0][i] == 1:
            start_node = Node(0, i)
            matrix[0][i] = start_node
        if matrix[-1][i] == 1:
            end_node = Node(len(matrix)-1, i)
            matrix[-1][i] = end_node
    return start_node, end_node

def ret_adj_points(matrix, r, c):# Returns a list of the adjacent points
    adj_points = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
    for p in adj_points:
        if matrix[p[0]][p[1]] == 0:
            adj_points.remove(p)
    return adj_points

def adj_count(matrix, r, c):# Counts the number of adjacent points
    return len(ret_adj_points(matrix, r, c))

def nodelist(matrix): # returns list of all the nodes
    start_node, end_node = start_end_nodes(matrix) # obtains start and end nodes
    nodelist = [start_node]

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):

            if matrix[row][col] != 0:
                n = adj_count(matrix, row, col)

                if n == 2:  # nodes identified by the number of adjacent paths and their arrangements.
                    if not(matrix[row][col + 1] == matrix[row][col - 1] or matrix[row + 1][col] == matrix[row - 1][col]): # if not a straight path
                        node = Node(row, col)
                        nodelist.append(node)
                        matrix[row][col] = node

                else: # when n is 1 ,3 or 4
                    node = Node(row, col)
                    nodelist.append(node)
                    matrix[row][col] = node

    nodelist += [end_node]
    return nodelist, matrix

def add_to_matrix(nodelist, matrix): #fills a plain maze matrix with nodes
    for node in nodelist:
        row, col = node.pos
        matrix[row][col] = node
    return matrix

def find_neighbours(nodelist, matrix): #fills up neighbours list for each node.
    for node in nodelist[1:-1]:
        (row, col) = node.pos
        # up the column
        while True:
            row -= 1
            if isinstance(matrix[row][col], Node):
                node.add_neighbour(matrix[row][col])
                break
            elif matrix[row][col] == 0:
                break

        (row, col) = node.pos
        # down the column
        while True:
            row += 1
            if isinstance(matrix[row][col], Node):
                node.add_neighbour(matrix[row][col])
                break
            elif matrix[row][col] == 0:
                break

        (row, col) = node.pos
        # down the row (left)
        while True:
            col -= 1
            if isinstance(matrix[row][col], Node):
                node.add_neighbour(matrix[row][col])
                break
            elif matrix[row][col] == 0:
                break

        (row, col) = node.pos
        # up the row (right)
        while True:
            col += 1
            if isinstance(matrix[row][col], Node):
                node.add_neighbour(matrix[row][col])
                break
            elif matrix[row][col] == 0:
                break

    # add neighbours for start and end nodes
    start, end = nodelist[0], nodelist[-1]
    s_row, s_col = start.pos
    e_row, e_col = end.pos
    while True:
        s_row += 1
        if isinstance(matrix[s_row][s_col], Node):
            start.add_neighbour(matrix[s_row][s_col])
            break

    while True:
        e_row -= 1
        if isinstance(matrix[e_row][e_col], Node):
            end.add_neighbour(matrix[e_row][e_col])
            break

def remove_deadends(nodelist, matrix): # removes dead end nodes (nodes with only 1 neighbouring node)
    deadends = []
    for node in nodelist[1:-1]:
        if len(node.neighbours) == 1: # if the node only has one neighbour then it is a dead end node (other than start and end nodes)
            deadends += [node]
            nodelist.remove(node)
            r, c = node.pos # replaces dead end nodes in the matrix with whitespace(1)
            matrix[r][c] = 1

    # removes dead end nodes from other nodes' neighbours list
    for node in nodelist[1:-1]:
        deadend_neighbours = [] # list of neighbours that are considered dead ends
        for neighbour in node.neighbours:
            if neighbour in deadends:
                deadend_neighbours += [neighbour] # adds dead end nodes to the list

        if deadend_neighbours != []:
            for neighbour in deadend_neighbours:
                node.remove_neighbour(neighbour) # removes dead end nodes

    return nodelist, matrix

# applying remove_deadends function until number of nodes is constant
def filter_out(nodelist, matrix):
    prev_length = 0

    while len(nodelist) != prev_length:
        prev_length = len(nodelist)
        remove_deadends(nodelist, matrix)

    return nodelist, matrix # returns potential path




