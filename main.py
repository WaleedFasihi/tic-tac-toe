from board import Board
from score import Score

score = Score()
board = Board(score)

pieces = ["X", "O"]


# Function to Start a New Game
def start_game():
    next_turn = True
    while next_turn:
        for piece in pieces:
            # Display the Grid
            board.display()

            # Show which player moves it is currently
            print(f"Player {piece} - Move")

            piece_failed = True
            while piece_failed:
                # Player Moves making sure input is valid
                row = board.get_input("row")
                column = board.get_input("column")

                # Place Piece on the Grid and Check final move
                piece_failed = board.place_piece(piece, row, column)

            # Check if there is a winner or draw
            if board.is_winner(piece, row, column):
                next_turn = False
                break


# Ask player to restart or end game
is_playing = True
while is_playing:
    start_game()

    if input("Enter 'y' to Restart, 'n' to End: ").lower() != "y":
        is_playing = False
    else:
        board.reset_board()
