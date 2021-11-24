"""
This assumes that a matrix of the maze with nodes in and a nodes list is already available
"""
from collections import deque

def breadth_first(nodelist, matrix):
    start, end = nodelist[0], nodelist[-1]
    width = len(matrix[0])
    height = len(matrix)

    queue = deque([start])

    prev = [None] * (width * height)
    visited = [False] * (width * height)

    (s_row, s_col) = start.pos
    visited[s_row * width + s_col] = True

    while queue:
        current = queue.pop()
        if current == end:
            break

        for node in current.neighbours:
            if node is not None:
                (n_row, n_col) = node.pos
                npos = n_row * width + n_col
                if not(visited[npos]):
                    queue.appendleft(node)
                    visited[npos] = True
                    prev[npos] = current

    path = deque()
    current = end
    while current is not None:

        path.appendleft(current)
        c_row, c_col = current.pos
        current = prev[c_row * width + c_col]

    return path






