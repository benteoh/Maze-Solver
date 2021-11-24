from collections import deque

def depth_first(nodelist, matrix):
    start, end = nodelist[0], nodelist[-1]
    width = len(matrix[0])
    height = len(matrix)
    stack = deque([start])
    prev = [None] * (width * height)
    visited = [False] * (width * height)

    while stack:
        current = stack.pop()
        if current == end:
            break

        visited[current.pos[0] * width + current.pos[1]] = True

        for node in current.neighbours:
            if node is not None:
                npos = node.pos[0] * width + node.pos[1]
                if not visited[npos]:
                    stack.append(node)
                    prev[npos] = current
    path = deque()
    current = end
    while current is not None:
        path.appendleft(current)
        current = prev[current.pos[0] * width + current.pos[1]]

    return path

