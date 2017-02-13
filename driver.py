import sys
import resource
import time
from method import *

method = sys.argv[1]
inputList = sys.argv[2].split(',')
inputList = [int(x) for x in inputList]

board = Board(inputList)
Board.initialize(inputList)
board.setborders()

if method == 'bfs':
    start = time.time()
    path = bfs(board)
    end = time.time()
    time_measure = end - start


    movements = path[0]
    movement_name = [move.movement for move in path[0]]

    for node in movements:
        print(node.movement)
        node.board.displayBoard()

    print("cost of path: %d" % (len(movement_name) - 1))
    print("nodes expanded %d" % path[1])
    print("fringe_size: %d" % path[2])
    print("max_fringe_size: %d" % path[3])
    print("search_depth: %d" % path[4])
    print("max_search_depth: %d" % (path[5]+1))
    print("resource:" + str((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)))
    print("the total time is " + str(time_measure) + " seconds")

    with open("Output.txt", "w") as outputfile:
        count = 1
        outputfile.write("path_to_goal:[")
        for i in movement_name[1:]:
            outputfile.write("'" + i + "'")
            if count < len(movement_name[1:]):
                outputfile.write(", ")
                count += 1
        outputfile.write("]" + '\n')
        outputfile.write("cost_of_path: " + str(len(movement_name) - 1) + '\n')
        outputfile.write("nodes_expanded: " + str(path[1]) + '\n')
        outputfile.write("fringe_size: " + str(path[2]) + '\n')
        outputfile.write("max_fringe_size: " + str(path[3]) + '\n')
        outputfile.write("search_depth: " + str(path[4]) + '\n')
        outputfile.write("max_search_depth: " + str(path[5]) + '\n')
        outputfile.write("running_time: " + str(time_measure) + '\n')
        outputfile.write("max_ram_usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + '\n')


elif method == 'dfs':
    start = time.time()
    path = dfs(board)
    end = time.time()
    time_measure = end - start

    movements = path[0]
    movement_name = [move.movement for move in path[0]]

    with open("Output.txt", "w") as outputfile:
        count = 1
        outputfile.write("path_to_goal:[")
        for i in movement_name[1:]:
            outputfile.write("'" + i + "'")
            if count < len(movement_name[1:]):
                outputfile.write(", ")
                count += 1
        outputfile.write("]" + '\n')
        outputfile.write("cost_of_path: " + str(len(movement_name) - 1) + '\n')
        outputfile.write("nodes_expanded: " + str(path[1]) + '\n')
        outputfile.write("fringe_size: " + str(path[2]) + '\n')
        outputfile.write("max_fringe_size: " + str(path[3]) + '\n')
        outputfile.write("search_depth: " + str(path[4]) + '\n')
        outputfile.write("max_search_depth: " + str(path[5]) + '\n')
        outputfile.write("running_time: " + str(time_measure) + '\n')
        outputfile.write("max_ram_usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + '\n')

    for node in path[0]:
        print(node.movement)
        node.board.displayBoard()
    print("cost of path: %d" % (len(movement_name) - 1))
    print("nodes expanded %d" % path[1])
    print("fringe_size: %d" % path[2])
    print("max_fringe_size: %d" % path[3])
    print("search_depth: %d" % path[4])
    print("max_search_depth: %d" % path[5])
    print("resource:" + str((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)))
    print("the total time is " + str(time_measure) + " seconds")

elif method == 'ast':

    start = time.time()
    path = ast(board)
    end = time.time()
    time_measure = end - start
    movements = path[0]
    movement_name = [move.movement for move in path[0]]

    with open("Output.txt", "w") as outputfile:
        count = 1
        outputfile.write("path_to_goal:[")
        for i in movement_name[1:]:
            outputfile.write("'" + i + "'")
            if count < len(movement_name[1:]):
                outputfile.write(", ")
                count += 1
        outputfile.write("]" + '\n')
        outputfile.write("cost_of_path: " + str(len(movement_name) - 1) + '\n')
        outputfile.write("nodes_expanded: " + str(path[1]) + '\n')
        outputfile.write("fringe_size: " + str(path[2]) + '\n')
        outputfile.write("max_fringe_size: " + str(path[3]) + '\n')
        outputfile.write("search_depth: " + str(path[4]) + '\n')
        outputfile.write("max_search_depth: " + str(path[5]) + '\n')
        outputfile.write("running_time: " + str(time_measure) + '\n')
        outputfile.write("max_ram_usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + '\n')

    for node in path[0]:
        print(node.movement)
        node.board.displayBoard()
    print("cost of path: %d" % (len(movement_name) - 1))
    print("nodes expanded %d" % path[1])
    print("fringe_size: %d" % path[2])
    print("max_fringe_size: %d" % path[3])
    print("search_depth: %d" % path[4])
    print("max_search_depth: %d" % path[5])
    print("resource:" + str((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)))
    print("the total time is " + str(time_measure) + " seconds")


elif method == 'ida':
    start = time.time()
    path = ida(board)
    end = time.time()
    time_measure = end - start

    movements = path[0]
    movement_name = [move.movement for move in path[0]]

    with open("Output.txt", "w") as outputfile:
        count = 1
        outputfile.write("path_to_goal:[")
        for i in movement_name[1:]:
            outputfile.write("'" + i + "'")
            if count < len(movement_name[1:]):
                outputfile.write(", ")
                count += 1
        outputfile.write("]" + '\n')
        outputfile.write("cost_of_path: " + str(len(movement_name) - 1) + '\n')
        outputfile.write("nodes_expanded: " + str(path[1]) + '\n')
        outputfile.write("fringe_size: " + str(path[2]) + '\n')
        outputfile.write("max_fringe_size: " + str(path[3]) + '\n')
        outputfile.write("search_depth: " + str(path[4]) + '\n')
        outputfile.write("max_search_depth: " + str(path[5]) + '\n')
        outputfile.write("running_time: " + str(time_measure) + '\n')
        outputfile.write("max_ram_usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + '\n')

    for node in path[0]:
        print(node.movement)
        node.board.displayBoard()
    print("nodes expanded %d" % path[1])
    print("cost of path: %d" % (len(movement_name) - 1))
    print("fringe_size: %d" % path[2])
    print("max_fringe_size: %d" % path[3])
    print("search_depth: %d" % path[4])
    print("max_search_depth: %d" % path[5])
    print("resource:" + str((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)))
    print("the total time is " + str(time_measure) + " seconds")

else:
    print("mistake with input or data")
