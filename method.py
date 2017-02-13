import math
from heapq import *
import copy

class Orderable(object):

    def __init__(self, firstname, lastname, *args):
        self.first = firstname
        self.last = lastname
        self.numbers = args
    def __lt__(self, other):
        return ("%s, %s" % (self.last, self.first) <"%s, %s" % (other.last, other.first))
    def __repr__(self):
        return "%s %s" % (self.first, self.last)
    def __getitem__(self, item):
        return self.numbers[item]


class State:
    def __init__(self, prevState, move="Initialization"):
        self.parent = prevState
        if move == "Initialization":
            self.board = prevState
            self.depth = 0
            self.parent = None
            self.movement = None
        else:
            self.board = Board(prevState.board.array[:])
            self.movement = move
            self.depth = self.parent.depth + 1
            if move == "Up":
                self.board.switchUp()
            elif move == "Down":
                self.board.switchDown()
            elif move == "Left":
                self.board.switchLeft()
            elif move == "Right":
                self.board.switchRight()
            else:
                print("switch error")


    def goalTest(self):

        Count = 0
        for x in self.board.array:
            if x != Count:
                return False
            Count += 1
        return True


class Board:
    leftBorder = []
    rightBorder = []
    boardSize = 0
    n_dim = 0


    def __init__(self, tilesList):
        self.__moveDirections = {'Up': True, 'Down': True, 'Left': True, 'Right': True}
        self.array = tilesList
        self.blankPosition = self.array.index(0)

    @staticmethod
    def initialize(tilesList):
        Board.boardSize = len(tilesList)
        Board.n_dim = int(math.sqrt(Board.boardSize))

    def displayBoard(self):
        for x in range(0, Board.boardSize):
            print(self.array[x], end=' ')
            if x in self.rightBorder:
                print()

    def checkDirectionsMovement(self):
        self.__moveDirections['Up']=False if self.blankPosition < self.n_dim else True
        self.__moveDirections['Down'] = False if self.blankPosition >= self.boardSize - self.n_dim else True
        self.__moveDirections['Right'] =False if self.__checkIfRightBorder() else True
        self.__moveDirections['Left'] =False if self.__checkIfLeftBorder() else True
        return self.__moveDirections

    def setborders(self):
        left = 0
        while left < self.boardSize:
            Board.leftBorder.append(left)
            left += self.n_dim
        right = Board.n_dim - 1
        while right <= Board.boardSize:
            Board.rightBorder.append(right)
            right += Board.n_dim

    def __checkIfLeftBorder(self):
        return self.blankPosition in Board.leftBorder

    def __checkIfRightBorder(self):
        return self.blankPosition in Board.rightBorder

    def switchUp(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[
            self.blankPosition]

    def switchDown(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[
            self.blankPosition]

    def switchLeft(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[
            self.blankPosition]

    def switchRight(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[
            self.blankPosition]


######################################   Algorithm  implement ################################################

def bfs(board):
    initialState = State(board)
    frontier = [initialState]
    explored = set(str(initialState.board.array))

    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)

    while length != 0:
        if length > max_fringe:
            max_fringe = length
        state = frontier.pop(0)  ##queue
        if max_search_depth < state.depth:
            max_search_depth = state.depth
        if state.goalTest():
            fringe_size = len(frontier)
            search_depth = state.depth

            while state :
                # print(state)
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()

            return nodeList, nodes_expanded - 1, fringe_size, max_fringe, search_depth, max_search_depth

        nodes_expanded += 1
        directions = state.board.checkDirectionsMovement()

        if directions['Up']:
            newState = State(state, 'Up')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Down']:
            newState = State(state, 'Down')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Left']:
            newState = State(state, 'Left')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Right']:
            newState = State(state, 'Right')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        length = len(frontier)
    return []


def dfs(board):  ##input 1,2,3,4
    initialState = State(board)
    frontier = [initialState]
    explored = set(str(initialState.board.array))
    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)

    while length != 0:
        if length > max_fringe:
            max_fringe = length
        state = frontier.pop()  ##stack

        if max_search_depth < state.depth:
            max_search_depth = state.depth

        if state.goalTest():
            fringe_size = len(frontier)
            search_depth = state.depth
            while state :
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()
            return nodeList, nodes_expanded - 1, fringe_size, max_fringe, search_depth, max_search_depth

        nodes_expanded += 1
        directions = state.board.checkDirectionsMovement()
        if directions['Right']:
            newState = State(state, 'Right')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Left']:
            newState = State(state, 'Left')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Down']:
            newState = State(state, 'Down')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        if directions['Up']:
            newState = State(state, 'Up')
            strState = str(newState.board.array)
            if strState not in explored:
                frontier.append(newState)
                explored.add(strState)
        length = len(frontier)
    return []


def ast(board):
    initialState = State(board)
    frontier = []
    explored = set(str(initialState.board.array))
    key_index=0
    heappush(frontier, (0,key_index,initialState))
    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)

    while length > 0:
        if length > max_fringe:
            max_fringe = length
        (h,key,state) = heappop(frontier)
        if max_search_depth < state.depth:
            max_search_depth = state.depth


        if state.goalTest():
            fringe_size = len(frontier)
            search_depth = state.depth
            while state:
                print(state)
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()
            return nodeList, nodes_expanded - 1, fringe_size, max_fringe, search_depth, max_search_depth



        nodes_expanded += 1

        directions = state.board.checkDirectionsMovement()

        if directions['Up']:
            newState = State(state, 'Up')
            strState = str(newState.board.array)
            if strState not in explored:
                explored.add(strState)
                heurist_val = astar_heuristic(state.board)
                key_index +=1
                heappush(frontier, (int(heurist_val+state.depth), key_index,newState))

        if directions['Down']:
            newState = State(state, 'Down')
            strState = str(newState.board.array)
            if strState not in explored:
                explored.add(strState)
                heurist_val = astar_heuristic(state.board)
                key_index += 1
                heappush(frontier, (int(heurist_val+state.depth), key_index, newState))

        if directions['Left']:
            newState = State(state, 'Left')
            strState = str(newState.board.array)
            if strState not in explored:
                explored.add(strState)
                heurist_val = astar_heuristic(state.board)
                key_index += 1
                heappush(frontier, (int(heurist_val+state.depth), key_index, newState))

        if directions['Right']:
            newState = State(state, 'Right')
            strState = str(newState.board.array)
            if strState not in explored:
                explored.add(strState)
                heurist_val = astar_heuristic(state.board)
                key_index += 1
                heappush(frontier, (int(heurist_val+state.depth), key_index, newState))
        length = len(frontier)
    return []


def astar_heuristic(board):
    value = 0
    for k in range(0, board.boardSize):
        value = value + math.fabs(k - board.array[k])
    return value


'''
(1) Implement DFS.
(2) Give it a depth limit. Now you have DLS.
(3) Use this DLS repeatedly, incrementing the limit. Now you have IDS.
(4) Ditch the depth limit, and use a path cost + heuristic limit instead. Voila, now you have IDA*.'''

def ida(board): #For each iteration,  handle node ordering as you would in dfs
    initialState = State(board)
    frontier = [initialState]
    explored = set(str(initialState.board.array))
    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)
    depth_limit = astar_heuristic(board)


    while not initialState.goalTest():

        while length > 0:

            state = frontier.pop()

            if length > max_fringe:
                max_fringe = length
            if max_search_depth < state.depth:
                max_search_depth = state.depth
            if state.goalTest():
                fringe_size = len(frontier)
                search_depth = state.depth

                while state :
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()

                return nodeList, nodes_expanded - 1, fringe_size, max_fringe, search_depth, max_search_depth
            nodes_expanded += 1

            directions = state.board.checkDirectionsMovement()
            if directions['Right']  and depth_limit> astar_heuristic(State(state, 'Right').board):
                newState = State(state, 'Right')
                strState = str(newState.board.array)
                if strState not in explored :
                    frontier.append(newState)
                    explored.add(strState)

            if directions['Left'] and depth_limit>  astar_heuristic(State(state, 'Left').board):
                newState = State(state, 'Left')
                strState = str(newState.board.array)
                if strState not in explored :
                    frontier.append(newState)
                    explored.add(strState)

            if directions['Down']  and depth_limit> astar_heuristic(State(state, 'Down').board):
                newState = State(state, 'Down')
                strState = str(newState.board.array)
                if strState not in explored :
                    frontier.append(newState)
                    explored.add(strState)

            if directions['Up']  and depth_limit> astar_heuristic(State(state, 'Up').board):
                newState = State(state, 'Up')
                strState = str(newState.board.array)
                if strState not in explored :
                    frontier.append(newState)
                    explored.add(strState)

            length = len(frontier)

            if length == 0:

                depth_limit += 1
                frontier=[state]
                length = len(frontier)

            '''else:
                if length > max_fringe:
                    max_fringe = length
                if max_search_depth < state.depth:
                    max_search_depth = state.depth

                fringe_size = len(frontier)
                search_depth = state.depth
                while state != None:
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()
                print("Final NODELIST!!!!!!!!!!!" + str(nodeList))
                return nodeList, nodes_expanded - 1, fringe_size, max_fringe, search_depth, max_search_depth'''

    return []


