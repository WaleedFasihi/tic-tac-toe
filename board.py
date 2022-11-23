import os
from score import Score


class Board:

    def __init__(self, score: Score):
        self.score = score
        self.moves = 0
        self.accepted_moves = ["1", "2", "3"]
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        super().__init__()

    # Generate the Grid in the console
    def display(self):
        # Clear the Console Screen
        os.system('cls')

        # Show Player Scores
        print(f"X: {self.score.score_x} | O: {self.score.score_o}")

        # Display the Grid
        for i in range(0, len(self.grid)):
            # Show the Row
            row = " " + " | ".join(self.grid[i]) + " "
            print(row)

            # Show the Divider except the final row
            if i != 2:
                print("-----------")

    # Get and check if input is accepted
    def get_input(self, where):
        while True:
            move = input(f"{where.title()} (1, 2 or 3): ")

            # Check if input is valid
            if move not in self.accepted_moves:
                print(f"{move} is an invalid input. Enter a valid value.")
            else:
                return int(move) - 1

    # Enter the Piece into the Grid
    def place_piece(self, piece, row, column):
        # Check if piece is placed
        if self.grid[row][column] != " ":
            print("Piece is already placed in this cell. Pick another.")
            return True

        # Add piece into the grid
        self.grid[row][column] = piece

        # Add total moves
        self.moves += 1

        return False

    def is_final_round(self):
        if self.moves == 9:
            return True
        return False

    def is_winner(self, piece, row, column):
        # Check if Piece is placed in a single row
        check_row = (self.grid[row][0] == piece
                     and self.grid[row][1] == piece
                     and self.grid[row][2] == piece)

        # Check if Piece is placed in a single column
        check_column = (self.grid[0][column] == piece
                        and self.grid[1][column] == piece
                        and self.grid[2][column] == piece)

        # Check if Piece is placed diagonally
        check_diag = ((
                        self.grid[0][0] == piece
                        and self.grid[1][1] == piece
                        and self.grid[2][2] == piece
                    ) or (
                        self.grid[0][2] == piece
                        and self.grid[1][1] == piece
                        and self.grid[2][0] == piece
                    ))

        # Check if winner is decided or it is a draw
        if check_row or check_column or check_diag:
            self.score.increase_score(piece)
            self.display()
            print(f"Player {piece} Wins!")
            return True
        elif self.is_final_round():
            self.display()
            print("All Turns Completed. Draw!")
            return True

        return False

    def reset_board(self):
        self.moves = 0
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
