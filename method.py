import math
from heapq import heappush, heappop,heapify
from priorityqueue import PriorityQueue


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
                self.board.swappUp()
            elif move == "Down":
                self.board.swappDown()
            elif move == "Left":
                self.board.swappLeft()
            elif move == "Right":
                self.board.swappRight()
            else:
                print("It's problem when swapping")

    def goalTest(self):
        
        checkCount = 0
        for x in self.board.array:
                if x != checkCount:
                    return False
                checkCount += 1
        return True


class Board:
    leftBorder = []
    rightBorder = []
    boardSize = 0
    n_dim = 0
    element = 0

    def __init__(self, tilesList):
        self.__moveDirections = {'Up': True, 'Down': True, 'Left': True, 'Right': True}
        self.array = tilesList
        self.blankPosition = self.array.index(0)

    @staticmethod
    def initializeStaticVariables(tilesList):
        Board.boardSize = len(tilesList)
        Board.n_dim = int(math.sqrt(Board.boardSize))

    def displayBoard(self):
        for x in range(0, Board.boardSize):
            print(self.array[x], end=' ')
            if x in self.rightBorder:
                print()

    def checkDirectionsMovement(self):

        if self.blankPosition < self.n_dim:
            self.__moveDirections['Up'] = False
        else:
            self.__moveDirections['Up'] = True
        if self.blankPosition >= self.boardSize - self.n_dim:
            self.__moveDirections['Down'] = False
        else:
            self.__moveDirections['Down'] = True
        if self.__checkIfRightBorder():
            self.__moveDirections['Right'] = False
        else:
            self.__moveDirections['Right'] = True
        if self.__checkIfLeftBorder():
            self.__moveDirections['Left'] = False
        else:
            self.__moveDirections['Left'] = True
        return self.__moveDirections

    def designateBorders(self):
        left = 0
        while left < self.boardSize:
            Board.leftBorder.append(left)
            left += self.n_dim

        right = Board.n_dim-1
        while right <= Board.boardSize:
            Board.rightBorder.append(right)
            right += Board.n_dim

    def __checkIfLeftBorder(self):
        return self.blankPosition in Board.leftBorder

    def __checkIfRightBorder(self):
        return self.blankPosition in Board.rightBorder

    def swappUp(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def swappDown(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def swappLeft(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def swappRight(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]




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
            state = frontier.pop(0)   ##queue
            if max_search_depth < state.depth:
                max_search_depth = state.depth
            if state.goalTest():
                fringe_size = len(frontier)
                search_depth = state.depth
                
                while state != None:
                    #print(state)
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()

                return nodeList, nodes_expanded-1, fringe_size, max_fringe,search_depth,max_search_depth
           
            
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




def dfs(board):
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
                while state != None:
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()
                return nodeList, nodes_expanded-1, fringe_size, max_fringe,search_depth,max_search_depth

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

def astar(board):
    initialState = State(board)
    frontier = []
    explored = set(str(initialState.board.array))
   
    heappush(frontier,(0,initialState))
   

    ######  data to return for the program output
    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)
    print(length)

    while length > 0:
        if length > max_fringe:
            max_fringe = length

        state = heappop(frontier)[1]
        print("EEEEEEEEEEEEEEEEEEEEEE"+str(state))

        if max_search_depth < state.depth:
            max_search_depth = state.depth

        #e###########################################
        if state.goalTest():
            fringe_size = len(frontier)
            search_depth = state.depth
            while state != None:
                print(state)
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()
            return nodeList, nodes_expanded-1, fringe_size, max_fringe, search_depth, max_search_depth
        ##############################################################
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
        
        heurist_val = astar_heuristic(state.board)
        heappush(frontier,(int(heurist_val),newState))

        length = len(frontier)
    return []




def astar_heuristic(board):
    value = 0
    print(board.boardSize)
    print("start--------------")
    for x in range(0,board.boardSize):
        print (x) 
        value = value + math.fabs(x - board.array[x])
    print("******")
    return value
