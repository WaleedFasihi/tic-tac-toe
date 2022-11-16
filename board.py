import os


class Board():

    def __init__(self):
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def display(self):
        # Clear the Console Screen
        os.system('cls')

        # Display the Grid
        for i in range(0, len(self.grid)):
            # Show the Row
            row = " " + " | ".join(self.grid[i]) + " "
            print(row)

            # Show the Divider except the final row
            if i != 2:
                print("-----------")

    def place_piece(self, piece, row, column):
        self.grid[row][column] = piece
