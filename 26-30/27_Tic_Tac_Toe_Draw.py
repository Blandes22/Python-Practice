"""
This exercise will take user input and determine where to player a player marker on the board with it

1   2   3
4   5   6
7   8   9

the user will pick a number from 1 to 9 to determine their placement
if the user picks 5 the program will need to know to put the marker at 1,1

where N is the users number:
we can use the equation ((N - 1) // 3) to determine row
we can use the equation ((N - 1) % 3) to determine column

"""


def place_marker(n: int, marker: str, board: list):
    row = ((n - 1) // 3)
    col = ((n - 1) % 3)
    board[row][col] = marker
    return board


if __name__ =="__main__":
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    marker = 'X'
    for i in board:
        print(i)
    user_placement = int(input("Please enter the number you would like to place your marker at: "))
    board = place_marker(user_placement, marker, board)
    for i in board:
        print(i)