import cv2
from matplotlib import pyplot as plt
from nodes import *

def convert_to_matrix(img_path): # Convert image to matrix equivalent.
    img = cv2.imread(img_path, 0)
    matrix = img/255
    return matrix

def pixelate(matrix): # Reduces size of matrix by only having 1 pixel per square.
    row1 = matrix[0]
    n = 0
    for i in row1:
        if i == 1:
            n += 1 # number of pixels long for each block
    compressed = []
    for r in range(0, len(matrix), n):
        row = []
        for c in range(0, len(matrix[0]), n):
            row.append(int(matrix[r][c]))
        compressed.append(row)
    return compressed

def create_path(matrix):
    start = [i for i in matrix[0] if isinstance(i, Node)][0]
    end = [i for i in matrix[-1] if isinstance(i, Node)][0]
    width = len(matrix[0])
    height = len(matrix)

    node = start
    prev_move = None

    while True:
        (row, col) = node.pos
        through = False
        if node == end:
            break
        #up the column
        if prev_move != "d" and not(through):
            while True:
                row -= 1
                if row < 0:
                    break
                if isinstance(matrix[row][col], Node):
                    next_node = matrix[row][col]
                    prev_move = "u"
                    through = True
                    break
                elif matrix[row][col] == 0:
                    break

        (row, col) = node.pos
        # down the column
        if prev_move != "u" and not(through):
            while True:
                row += 1
                if row > height:
                    break
                if isinstance(matrix[row][col], Node):
                    next_node = matrix[row][col]
                    prev_move = "d"
                    through = True
                    break
                elif matrix[row][col] == 0:
                    break

        (row, col) = node.pos
        # down the row (left)
        if prev_move != "r" and not(through):
            while True:
                col -= 1
                if col < 0:
                    break
                if isinstance(matrix[row][col], Node):
                    next_node = matrix[row][col]
                    prev_move = "l"
                    through = True
                    break
                elif matrix[row][col] == 0:
                    break

        (row, col) = node.pos
        # up the row (right)
        if prev_move != "l" and not(through):
            while True:
                col += 1
                if col > width:
                    break
                if isinstance(matrix[row][col], Node):
                    next_node = matrix[row][col]
                    prev_move = "r"
                    through = True
                    break
                elif matrix[row][col] == 0:
                    break

        (row, col) = node.pos
        (n_row, n_col) = next_node.pos
        if row == n_row:
            if col > n_col:
                for c in range(n_col + 1, col):
                    matrix[row][c] = 13.5
            else:
                for c in range(col + 1, n_col):
                    matrix[row][c] = 13.5
        else:
            if row > n_row:
                for r in range(n_row + 1, row):
                    matrix[r][col] = 13.5
            else:
                for r in range(row + 1, n_row):
                    matrix[r][col] = 13.5

        node = next_node

def convert_to_image(matrix, n1, n2): # Converts matrix to pyplot image
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] = 15
            if isinstance(matrix[row][col], Node):
                matrix[row][col] = 3
    plt.matshow(matrix, cmap="nipy_spectral")
    plt.title("Initial Number of Nodes : " + str(n1) + "\n Final Number of Nodes : " + str(n2))
    plt.show()





