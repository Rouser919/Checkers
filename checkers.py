from engine import Table, checkForEndOfTheGame
from display import drawWindow, SQUARESIZE, messageDisplay
import pygame

FPS = 60
WIDTH = SQUARESIZE * 8
HEIGHT = SQUARESIZE * 9
WINSOUNDPATH = "SoundEffects/391539__mativve__electro-win-sound.wav"
CORRECTCLICKSOUNDPATH = "SoundEffects/121195__gusgus26__hit-plastic-box.wav"
INCORRECTCLICKSOUNDPATH = (
    "SoundEffects/528956__beetlemuse__wrong-answer-incorrect-error.wav"
)
BACKGROUNDMUSICPATH = "Music/bensound-creativeminds.mp3"

if __name__ == "__main__":

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load(BACKGROUNDMUSICPATH)
    pygame.mixer.music.play(-1)
    WinSound = pygame.mixer.Sound(WINSOUNDPATH)
    CorrectClick = pygame.mixer.Sound(CORRECTCLICKSOUNDPATH)
    InCorrectClick = pygame.mixer.Sound(INCORRECTCLICKSOUNDPATH)

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
                WinSound.play()
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
                        CorrectClick.play()
                        validMoves = workingOnTableOfCheckers.findValidMovesForPiece(
                            [x, y]
                        )
                        drawWindow(workingOnTableOfCheckers, WIN, validMoves)
                    else:
                        InCorrectClick.play()
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
                        CorrectClick.play()
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
                        InCorrectClick.play()
                        messageDisplay(
                            "Wrong click! try again",
                            30,
                            250,
                            HEIGHT - 40,
                            (0, 0, 0),
                            WIN,
                        )
    pygame.mixer.music.stop()
    pygame.quit()
