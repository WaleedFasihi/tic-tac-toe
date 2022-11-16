from board import Board

board = Board()

pieces = ["X", "O"]
moves = ["1", "2", "3"]
score_1 = score_2 = 0

next_turn = True
while next_turn:
    for piece in pieces:
        # Display the Grid
        board.display()

        # Show which player moves it is currently
        print(f"Player {piece} - Move")

        # Player Moves making sure input is valid
        while True:
            row = input(f"Row (1, 2 or 3): ")

            # Check if input is valid
            if row not in moves:
                print(f"{row} is an invalid input. Enter a valid value.")
            else:
                row = int(row) - 1
                break

        while True:
            column = input(f"Column (1, 2 or 3): ")

            # Check if input is valid
            if column not in moves:
                print(f"{column} is an invalid input. Enter a valid value.")
            else:
                column = int(column) - 1
                break

        # Place Piece on the Grid
        board.place_piece(piece, row, column)
