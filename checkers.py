from engine import Table, checkForEndOfTheGame  # Work in progress on refactoring
from display import drawWindow, SQUARESIZE, messageDisplay
import pygame

FPS = 60
WIDTH = 67 * 8
HEIGHT = 67 * 9


def main():
    pygame.init()
    pygame.display.set_caption("Checkers")
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    startingTableOfCheckers = [
        [".", "w", ".", "w", ".", "w", ".", "w"],
        ["w", ".", "w", ".", "w", ".", "w", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "b", ".", "b", ".", "b", ".", "b"],
        ["b", ".", "b", ".", "b", ".", "b", "."],
    ]

    workingOnTableOfCheckers = Table(startingTableOfCheckers, True)
    clock = pygame.time.Clock()
    run = True
    validMoves = None
    previousMoves = None
    turn = "White"
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if checkForEndOfTheGame(workingOnTableOfCheckers):
                run = False
                break
            drawWindow(workingOnTableOfCheckers, WIN, validMoves=validMoves)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                x = int(mousePos[0] / SQUARESIZE)
                y = int(mousePos[1] / SQUARESIZE)

                if validMoves is None:
                    previousMoves = [x, y]

                    if (
                        workingOnTableOfCheckers._table[x][y].lower() == "w"
                        and turn == "White"
                    ) or (
                        workingOnTableOfCheckers._table[x][y].lower() == "b"
                        and turn == "Black"
                    ):
                        validMoves = workingOnTableOfCheckers.findValidMovesForPiece(
                            [x, y]
                        )
                        drawWindow(workingOnTableOfCheckers, WIN, validMoves)
                    else:
                        messageDisplay(
                            "Wrong click! try again",
                            30,
                            250,
                            HEIGHT - 40,
                            (0, 0, 0),
                            WIN,
                        )
                        pygame.display.update()
                elif validMoves is not None and previousMoves is not None:
                    goodMove = False
                    for moves in validMoves:
                        if moves[0] == x and moves[1] == y:
                            goodMove = True
                    if goodMove:
                        rawTableWithPosOfPieces = workingOnTableOfCheckers.playMove(
                            previousMoves, [x, y]
                        )
                        workingOnTableOfCheckers._table = rawTableWithPosOfPieces
                        if turn == "White":
                            turn = "Black"
                        else:
                            turn = "White"
                        previousMoves = None
                        validMoves = None
                    else:
                        messageDisplay(
                            "Wrong click! try again",
                            30,
                            250,
                            HEIGHT - 40,
                            (0, 0, 0),
                            WIN,
                        )
    pygame.quit()


if __name__ == "__main__":
    main()
