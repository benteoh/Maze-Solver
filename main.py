"""
Maze must follow the following criteria:
1) Entrance and Exit must be at the top and bottom
2) Maze must be made up of only black and white squares
3) Only one entrance and exit

Path finder Algorithms:
1) Node finding and filtering dead ends repeatedly.
2) Breadth-first Search Algorithm.
3) Depth-First Search Algorithm

"""
from imgtomatrix import *
from nodesfunctions import *
from depthfirst import *
from breadthfirst import *
from time import time
import argparse

# Command line Parser.
parser = argparse.ArgumentParser(description="Accept Image Name.")
parser.add_argument("-n", "--img", required=True, help="image")# add view img
parser.add_argument("--algo", required=True, help="algorithm")
# eg : python main.py --img maze1.png
args = vars(parser.parse_args())
img_name = "images/" + args["img"]
algorithm = args["algo"]

# Conversion of maze image to matrix of 1's and 0's.
t0 = time()

mat = pixelate(convert_to_matrix(img_name))

t1 = time()

print("Time Elapsed to Create Maze: ", t1-t0)
t0 = time()
# CODE TO SOLVE MAZE.
nodelist, mat = nodelist(mat)
find_neighbours(nodelist, mat)
n1 = len(nodelist)

# selection of algorithms to be used
if algorithm == "remove_deadends":

    path, solved = filter_out(nodelist, mat)

    t1 = time()

elif algorithm == "breadth_first":

    path = breadth_first(nodelist, mat)

    t1 = time()

    mat = pixelate(convert_to_matrix(img_name))
    solved = add_to_matrix(path, mat)

elif algorithm == "depth_first":

    path = depth_first(nodelist, mat)

    t1 = time()

    mat = pixelate(convert_to_matrix(img_name))
    solved = add_to_matrix(path, mat)

elif algorithm == "view":
    convert_to_image(mat, n1, "-")
    quit()

else:
    print("Typed something wrong.")
    quit()

# CODE TO SOLVE MAZE.

# Calculating the algorithm's speed.
print("Time Elapsed to Solve Maze: ", t1-t0)

# Creates and shows the solved maze.
create_path(solved)
convert_to_image(solved, n1, len(path))

