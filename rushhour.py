#!/usr/bin/env python3
# Spencer Toeg
# CS380
# Assignment 1 - Rush Hour
# Imports
import sys
from copy import copy, deepcopy
# Board Class: Creates a board from a givin string.
# Attributes: boardArrary - 2d array to represent the board
#             Cars - list of all the cars that appear in the array.
#             x - length of board array
class board:
    def __init__(self, input=""):
        # Splits input and then calls the create board method.
        self.boardArray = input.split("|")
        self.cars = []
        self.x = 0
        self.createBoard()
    # Called on creation of new board. Sets up the 2d array
    # Input: n/a
    # Output: n/a  (sets up the boardArray, Cars list, & x variable)
    def createBoard(self):
        self.x = len(self.boardArray)
        # Creates the column list out of each row.
        i = 0
        while i < self.x:
            self.boardArray[i] = list(self.boardArray[i])
            i += 1
        # Sets Up cars list. Iterates through boardArray and adds new letters to the list
        i = 0
        while i < self.x:
            y = len(self.boardArray[i])
            j = 0
            while j < y:
                n = self.boardArray[i][j]
                if n not in self.cars:
                    self.cars.append(n)
                j += 1
            i += 1
        # CleanUp: removes the ' ' (space) car from the list
        self.cars.remove(' ')
    # Overwrites string method. Used to print the board class in a presentable manner.
    # Input: n/a
    # Output: Boards in readable fasion
    def __str__(self):
        print(" ------ ")
        print("|" + ''.join(self.boardArray[0]) + "|")
        print("|" + ''.join(self.boardArray[1]) + "|")
        print("|" + ''.join(self.boardArray[2]) + " ")
        print("|" + ''.join(self.boardArray[3]) + "|")
        print("|" + ''.join(self.boardArray[4]) + "|")
        print("|" + ''.join(self.boardArray[5]) + "|")
        print(" ------ ")
        return ""
    # CarInfo: Gathers information about a specific car.
    # Input: car letter
    # Output: [[position], 'direction', length]
    #         postion = [x, y]   direction = 'v' || 'h'   length = 2 || 3
    def carInfo(self, car):
        # Error Check: make sure car exists
        if car not in self.cars:
            print("Error: Car does not exist")
            return 0
        # Set up output & component lists
        info = []
        pos = []
        direction = ''
        i = 0
        while i < self.x:
            y = len(self.boardArray[i])
            j = 0
            while j < y:
                # When car is found, save position.
                if car == self.boardArray[i][j]:
                    pos.append(i)
                    pos.append(j)
                    info.append(pos)
                    # Check one space to the right. If it is the same letter, car is
                    # horizontal, else vertical
                    try:
                        if car == self.boardArray[i][j + 1]:
                            direction = 'h'
                        else:
                            direction = 'v'
                    except:
                        direction = 'v'
                    # length starts at 1 - increment length for each movement. Broken up into vert. or horiz.
                    length = 1
                    n = 1
                    # if direction was horizontal, increase pos[0] (y) until you reach
                    # out of bounds or something other then car.
                    if direction == 'h':
                        while n < 6:
                            try:
                                if car == self.boardArray[pos[0]][pos[1] + n]:
                                    length += 1
                                else:
                                    info.append(direction)
                                    info.append(length)
                                    return info
                            except:
                                info.append(direction)
                                info.append(length)
                                return info
                            n += 1
                    # direction is vertical. increase pos[1] (x) until you reach out of bounds or
                    # other then car.
                    else:
                        while n < 6:
                            try:
                                if car == self.boardArray[pos[0] + n][pos[1]]:
                                    length += 1
                                else:
                                    info.append(direction)
                                    info.append(length)
                                    return info
                            except:
                                info.append(direction)
                                info.append(length)
                                return info
                            n += 1
                j += 1
            i += 1
        info.append(direction)
        info.append(length)
        return info
    # Clone: Creates a deep copy for the given input
    # Input: board(or given list)
    # Output: deep copy of the input
    def clone(self, board):
        temp = deepcopy(board)
        return temp
    # Next_for_car: Outputs a list of all possible boards after the input car has made 1 move.
    # Input: car
    # Output: list of all boards after the car has made 1 move.
    def next_for_car(self, car):
        # Setup output & get information on the car.
        nextBoards = []
        info = self.carInfo(car)
        pos = copy(info[0])
        direction = copy(info[1])
        length = copy(info[2])
        # Cars can either move vertically or horizontally
        # Movement for horizontal
        if (direction == 'h'):
            # Move Left
            tempBoard = self.clone(self.boardArray)
            while True:
                if pos[1] > 0:              # If car is not against left wall
                    try:                                                # Each direction follows this format:
                        if self.boardArray[pos[0]][pos[1] - 1] == ' ':  # If there is an open space to the left (right, up, down)
                            tempBoard = self.clone(tempBoard)           # Clone Board
                            tempBoard[pos[0]][pos[1] - 1] = car         # Change open space to car
                            pos[1] -= 1                                 # Move the position of car 1 left (right, up, down)
                            tempBoard[pos[0]][pos[1] + length] = ' '    # Erase the tail end of car
                            nextBoards.append(tempBoard)                # append board to output
                            continue
                        else:
                            break
                    except Exception as e:
                        # print(e, " - Move Left")
                        break
                else:
                    break
            # Move Right
            pos = copy(info[0])
            direction = copy(info[1])
            length = copy(info[2])
            tempBoard = self.clone(self.boardArray)
            while True:
                try:
                    if self.boardArray[pos[0]][pos[1] + length] == ' ':
                        tempBoard = self.clone(tempBoard)
                        tempBoard[pos[0]][pos[1] + length] = car
                        pos[1] += 1
                        tempBoard[pos[0]][pos[1] - 1] = ' '
                        nextBoards.append(tempBoard)
                        continue
                    else:
                        break
                except Exception as e:
                    # print(e, " - Move Right")
                    break
        # Vertical Movement
        else:
            # Move Up
            tempBoard = self.clone(self.boardArray)
            while True:
                if pos[0] > 0:
                    try:
                        if self.boardArray[pos[0] - 1][pos[1]] == ' ':
                            tempBoard = self.clone(tempBoard)
                            tempBoard[pos[0] - 1][pos[1]] = car
                            pos[0] -= 1
                            tempBoard[pos[0] + length][pos[1]] = ' '
                            nextBoards.append(tempBoard)
                            continue
                        else:
                            break
                    except Exception as e:
                        # print(e, " - Move Up")
                        break
                else:
                    break
            # Move Down
            pos = copy(info[0])
            direction = copy(info[1])
            length = copy(info[2])
            tempBoard = self.clone(self.boardArray)
            while True:
                try:
                    if self.boardArray[pos[0] + length][pos[1]] == ' ':
                        tempBoard = self.clone(tempBoard)
                        tempBoard[pos[0] + length][pos[1]] = car
                        pos[0] += 1
                        tempBoard[pos[0] - 1][pos[1]] = ' '
                        nextBoards.append(tempBoard)
                        continue
                    else:
                        break
                except Exception as e:
                    # print(e, " - Move Down")
                    break
        return nextBoards
    # isDone: Checks if the board is in a win state. Simply checks spot 2, 5 for the 'x' car
    # Input: n/a
    # Output: True at win state; false otherwise
    def isDone(self):
        if(self.boardArray[2][5] == 'x'):
            return True
        return False
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Main ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# get command and create board
command = sys.argv[1]
try:
    input = board(sys.argv[2])
except:
    input = board("  o aa|  o   |xxo   |ppp  q|     q|     q")
# Execute correct command
if ( command == "print" ):
    print(input)
elif ( command == "done"):
    print(input.isDone())
elif ( command == "next" ):
    # Get next boards for every car
    cars = input.cars
    nextBoards = []
    for i in cars:
        t = input.next_for_car(i)
        if t == False:
            continue
        else:
            nextBoards.append(t)
    # store length of board length & number of boards
    boardLength = len(nextBoards)
    numberOfBoards = 0
    for i in range(boardLength):
        for j in range(len(nextBoards[i])):
            if len(nextBoards[i][j]) > 0:
                numberOfBoards += 1
    # Print top boarder for boards
    for i in range(numberOfBoards - 1):
        print(' ------ ', end='  ')
    print(' ------ ')
    # Print horizontally. Every first row, then ever second, etc.
    row = 0
    while row < 6:
        print('', end='')
        for i in range(boardLength):
            for j in range(len(nextBoards[i])):
                # Leave gap for the exit in row 2
                if row == 2:
                    print("|" + ''.join(nextBoards[i][j][row]) + " ", end='  ')
                else:
                    print("|" + ''.join(nextBoards[i][j][row]) + "|", end='  ')
        print("\n", end='')
        row += 1
    # Print Bottom Boarder
    for i in range(numberOfBoards):
        print(' ------ ', end='  ')
    print('\n')
else:
    print("Error: invalid command")
