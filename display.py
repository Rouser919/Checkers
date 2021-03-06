import pygame
from consts import SQUARESIZE, PIECESIZE, COLORS


def drawBoardSquares(WIN, validMoves=None):
    for x in range(8):
        for y in range(8):
            if ((x + y) % 2) == 1:
                colour = COLORS["EARLY_ESPRESSO"]
            else:
                colour = COLORS["MUSTARD"]
            pygame.draw.rect(
                WIN,
                colour,
                (
                    x * SQUARESIZE,
                    y * SQUARESIZE,
                    SQUARESIZE,
                    SQUARESIZE,
                ),
            )
    if validMoves is not None:
        colour = COLORS["NIGHT_OF_NAVY"]
        for moves in validMoves:
            pygame.draw.rect(
                WIN,
                colour,
                (
                    moves[0] * SQUARESIZE,
                    moves[1] * SQUARESIZE,
                    SQUARESIZE,
                    SQUARESIZE,
                ),
            )


def textObjects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def messageDisplay(text, text_size, text_orientation_w, text_orientation_h, color, WIN):
    menuText = pygame.font.Font("freesansbold.ttf", text_size)
    textSurf, textRect = textObjects(text, menuText, color)
    textRect.center = (text_orientation_w, text_orientation_h)
    WIN.blit(textSurf, textRect)


def drawWindow(tableOfCheckers, WIN, validMoves=None):
    WIN.fill(COLORS["CHERRY"])
    drawBoardSquares(WIN, validMoves=validMoves)
    drawPieceCircles(tableOfCheckers, WIN)
    pygame.display.update()


def drawPieceCircles(tableOfCheckers, WIN):
    for x in range(8):
        for y in range(8):
            if tableOfCheckers._table[x][y] != ".":
                if tableOfCheckers._table[x][y].lower() == "b":
                    colour = COLORS["SUMMER_SUN"]
                    pygame.draw.circle(
                        WIN,
                        colour,
                        (
                            x * SQUARESIZE + PIECESIZE,
                            y * SQUARESIZE + PIECESIZE,
                        ),
                        PIECESIZE,
                    )
                    messageDisplay(
                        tableOfCheckers._table[x][y],
                        30,
                        x * SQUARESIZE + PIECESIZE,
                        y * SQUARESIZE + PIECESIZE,
                        COLORS["BRIGHT_SUMMER_SUN"],
                        WIN,
                    )
                elif tableOfCheckers._table[x][y].lower() == "w":
                    colour = COLORS["PACIFIC"]
                    pygame.draw.circle(
                        WIN,
                        colour,
                        (
                            x * SQUARESIZE + PIECESIZE,
                            y * SQUARESIZE + PIECESIZE,
                        ),
                        PIECESIZE,
                    )
                    messageDisplay(
                        tableOfCheckers._table[x][y],
                        30,
                        x * SQUARESIZE + PIECESIZE,
                        y * SQUARESIZE + PIECESIZE,
                        COLORS["BRIGHT_PACIFIC"],
                        WIN,
                    )
