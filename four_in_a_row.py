"""Four-in-a-Row
A tile-dropping game to get four-in-a-row, similar to Connect Four."""

import sys

# Constants used for displaying the board:
EMPTY_SPACE = "."  # A period is easier to count than a space.
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = """
  1234567
  +-------+
  |{}{}{}{}{}{}{}|
  |{}{}{}{}{}{}{}|
  |{}{}{}{}{}{}{}|
  |{}{}{}{}{}{}{}|
  |{}{}{}{}{}{}{}|
  |{}{}{}{}{}{}{}|
  +-------+"""


def main():
    """Runs a single game of four-in-a-row."""
    print(
        """Four-in-a-Row
  Two players take turns dropping tiles into one of seven columns, trying
  to make four-in-a-row horizontally, vertically or diagonally.
  """
    )
  # set up a new game:
  gameBoard = getNewBoard()
  playerTurn = PLAYER_X

  while True: # Runs a player's turn
    # Display the board and get player's move:
    displayBoard(gameBoard)
    playerMove = getPlayerMove(playerTurn, gameBoard)
    gameBoard[playerMove] = playerTurn

    # Check for a win or tie
    if isWinner(playerTurn, gameBoard):
        displayBoard(gameBoard)  # Display the board one last time.
        print("Player {} has won!".format(playerTurn))
        sys.exit()
    elif isFull(gameBoard):
        displayBoard(gameBoard)  # Display the board one last time.
        print("There is a tie!")
        sys.exit()

    # Switch turns to other player:
    if playerTurn == PLAYER_X:
        playerTurn = PLAYER_O
    elif playerTurn == PLAYER_O:
        playerTurn = PLAYER_X