import pygame

colors = {
    "SUMMER_SUN": (255, 196, 56),
    "BRIGHT_SUMMER_SUN": (255, 228, 196),
    "EARLY_ESPRESSO": (80, 57, 49),
    "MUSTARD": (205, 133, 63),
    "PACIFIC": (1, 128, 181),
    "BRIGHT_PACIFIC": (75, 198, 213),
    "BLACK": (19, 27, 29),
    "CHERRY": (165, 30, 44),
    "NIGHT_OF_NAVY": (33, 64, 95),
    "GREEN": (197, 244, 66),
}

SQUARESIZE = 67
PIECESIZE = 33
BOARDSIZE = SQUARESIZE * 8


def drawBoardSquares(WIN, validMoves=None):
    for x in range(8):
        for y in range(8):
            if ((x + y) % 2) == 1:
                colour = colors["EARLY_ESPRESSO"]
            else:
                colour = colors["MUSTARD"]
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
        colour = colors["NIGHT_OF_NAVY"]
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
    WIN.fill(colors["CHERRY"])
    drawBoardSquares(WIN, validMoves=validMoves)
    drawPieceCircles(tableOfCheckers, WIN)
    pygame.display.update()


def drawPieceCircles(tableOfCheckers, WIN):
    for x in range(8):
        for y in range(8):
            if tableOfCheckers._table[x][y] != ".":
                if tableOfCheckers._table[x][y].lower() == "b":
                    colour = colors["SUMMER_SUN"]
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
                        colors["BRIGHT_SUMMER_SUN"],
                        WIN,
                    )
                elif tableOfCheckers._table[x][y].lower() == "w":
                    colour = colors["PACIFIC"]
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
                        colors["BRIGHT_PACIFIC"],
                        WIN,
                    )
