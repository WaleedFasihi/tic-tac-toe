from board import Board

board = Board()

pieces = ["X", "O"]

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
