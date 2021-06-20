from copy import deepcopy
from display import messageDisplay
from consts import HEIGHT


class Table(object):
    def __init__(self, table):
        self._table = table

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


def checkForEndOfTheGame(workingOnTableOfCheckers, WIN):

    numberOfFigures = workingOnTableOfCheckers.countOfPieces()
    if numberOfFigures[0] == 0:
        messageDisplay(
            "Black Won!",
            30,
            250,
            HEIGHT - 40,
            (0, 0, 0),
            WIN,
        )
        return True
    if numberOfFigures[1] == 0:
        messageDisplay(
            "White Won!",
            30,
            250,
            HEIGHT - 40,
            (0, 0, 0),
            WIN,
        )
        return True
    if numberOfFigures[0] + numberOfFigures[1] == 2:
        messageDisplay(
            "Tie!",
            30,
            250,
            HEIGHT - 40,
            (0, 0, 0),
            WIN,
        )
        return True

    return False
