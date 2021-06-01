from copy import deepcopy


class Table(object):
    def __init__(self, table, white_to_move=True):
        self._table = table
        self._nextMoves = None
        self._whiteToMove = white_to_move

    def getNextMoves(self):
        if self._nextMoves is None:
            self.generateNextMoves()
        return self._nextMoves

    def countOfPieces(self):
        numWhite = 0
        numBlack = 0
        for i in range(len(self._table)):
            for j in range(len(self._table[i])):
                if self._table[i][j].lower() == "b":
                    numBlack += 1
                if self._table[i][j].lower() == "w":
                    numWhite += 1
        return numWhite, numBlack

    def generateNextMoves(self):
        self._nextMoves = []
        captures = []
        all_moves = []

        for i in range(len(self._table)):
            for j in range(len(self._table[i])):
                if self._whiteToMove:
                    if self._table[i][j].lower() == "b":
                        validMoves = self.findValidMovesForPiece((i, j))
                        for move in validMoves:
                            if move[0] - i == 2 or move[0] - i == -2:
                                new_table = self.generateNewState((i, j), move)
                                position = Table(new_table, not self._whiteToMove)
                                captures.append(position)
                            else:
                                new_table = self.generateNewState((i, j), move)
                                position = Table(new_table, not self._whiteToMove)
                                all_moves.append(position)

                else:
                    if self._table[i][j].lower() == "w":
                        validMoves = self.findValidMovesForPiece((i, j))
                        for move in validMoves:
                            if move[0] - i == 2 or move[0] - i == -2:
                                new_table = self.generateNewState((i, j), move)
                                position = Table(new_table, not self._whiteToMove)
                                captures.append(position)
                            else:
                                new_table = self.generateNewState((i, j), move)
                                position = Table(new_table, not self._whiteToMove)
                                all_moves.append(position)
        else:
            self._nextMoves = captures + all_moves

    def generateNewState(self, actualPositionForPiece, newPositionForPiece):
        coppiedTable = deepcopy(self._table)
        typeOfFigure = coppiedTable[actualPositionForPiece[0]][
            actualPositionForPiece[1]
        ]
        if typeOfFigure.lower() == "b":
            if newPositionForPiece[0] == 0:
                coppiedTable[actualPositionForPiece[0]][actualPositionForPiece[1]] = "B"
            if (
                actualPositionForPiece[0] - newPositionForPiece[0] == 2
                or actualPositionForPiece[0] - newPositionForPiece[0] == -2
            ):
                row = (
                    actualPositionForPiece[0]
                    + (newPositionForPiece[0] - actualPositionForPiece[0]) // 2
                )
                column = (
                    actualPositionForPiece[1]
                    + (newPositionForPiece[1] - actualPositionForPiece[1]) // 2
                )
                coppiedTable[row][column] = "."
        if typeOfFigure.lower() == "w":
            if newPositionForPiece[0] == 7:
                coppiedTable[actualPositionForPiece[0]][actualPositionForPiece[1]] = "W"
            if (
                actualPositionForPiece[0] - newPositionForPiece[0] == 2
                or actualPositionForPiece[0] - newPositionForPiece[0] == -2
            ):
                row = (
                    actualPositionForPiece[0]
                    + (newPositionForPiece[0] - actualPositionForPiece[0]) // 2
                )
                column = (
                    actualPositionForPiece[1]
                    + (newPositionForPiece[1] - actualPositionForPiece[1]) // 2
                )
                coppiedTable[row][column] = "."
        (
            coppiedTable[actualPositionForPiece[0]][actualPositionForPiece[1]],
            coppiedTable[newPositionForPiece[0]][newPositionForPiece[1]],
        ) = (
            coppiedTable[newPositionForPiece[0]][newPositionForPiece[1]],
            coppiedTable[actualPositionForPiece[0]][actualPositionForPiece[1]],
        )

        return coppiedTable

    def playMove(self, actualPositionForPiece, newPositionForPiece):
        tableOfCheckers = self.generateNewState(
            actualPositionForPiece, newPositionForPiece
        )
        return tableOfCheckers

    def findValidMovesForPiece(self, coord):
        captures = []
        validMoves = []
        figure = self._table[coord[0]][coord[1]]
        if figure != "b":
            if 0 <= coord[0] < 7:
                if (coord[1] - 1) >= 0:
                    if self._table[coord[0] + 1][coord[1] - 1] == ".":
                        validMoves.append((coord[0] + 1, coord[1] - 1))
                    elif coord[0] + 2 < 8 and coord[1] - 2 >= 0:
                        if self._table[coord[0] + 2][coord[1] - 2] == ".":
                            if (
                                figure.lower()
                                != self._table[coord[0] + 1][coord[1] - 1].lower()
                            ):
                                captures.append((coord[0] + 2, coord[1] - 2))
                if (coord[1] + 1) < 8:
                    if self._table[coord[0] + 1][coord[1] + 1] == ".":
                        validMoves.append((coord[0] + 1, coord[1] + 1))
                    elif coord[0] + 2 < 8 and coord[1] + 2 < 8:
                        if self._table[coord[0] + 2][coord[1] + 2] == ".":
                            if (
                                figure.lower()
                                != self._table[coord[0] + 1][coord[1] + 1].lower()
                            ):
                                captures.append((coord[0] + 2, coord[1] + 2))

        if figure != "w":
            if 0 < coord[0] < 8:
                if (coord[1] - 1) >= 0:
                    if self._table[coord[0] - 1][coord[1] - 1] == ".":
                        validMoves.append((coord[0] - 1, coord[1] - 1))
                    elif coord[0] - 2 >= 0 and coord[1] - 2 >= 0:
                        if self._table[coord[0] - 2][coord[1] - 2] == ".":
                            if (
                                figure.lower()
                                != self._table[coord[0] - 1][coord[1] - 1].lower()
                            ):
                                captures.append((coord[0] - 2, coord[1] - 2))

                if (coord[1] + 1) < 8:
                    if self._table[coord[0] - 1][coord[1] + 1] == ".":
                        validMoves.append((coord[0] - 1, coord[1] + 1))
                    elif coord[0] - 2 >= 0 and coord[1] + 2 < 8:
                        if self._table[coord[0] - 2][coord[1] + 2] == ".":
                            if (
                                figure.lower()
                                != self._table[coord[0] - 1][coord[1] + 1].lower()
                            ):
                                captures.append((coord[0] - 2, coord[1] + 2))
        return captures + validMoves


def checkForEndOfTheGame(workingOnTableOfCheckers):
    posibleMoves = workingOnTableOfCheckers.getNextMoves()

    numberOfFigures = workingOnTableOfCheckers.countOfPieces()
    if numberOfFigures[0] == 0:
        print("Black won!")
        return True
    if numberOfFigures[1] == 0:
        print("White won!")
        return True
    if numberOfFigures[0] + numberOfFigures[1] == 2:
        print("Tie!")
        return True
    if not posibleMoves:
        print("There are no possible moves left! Game is finished!")
        return True
    return False
