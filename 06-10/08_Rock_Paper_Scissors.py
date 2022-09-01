#rock paper scissors game

def get_move():
    return input("Please enter you hand (rock, paper, or scissors): ").lower()

def check_game(p1move, p2move):
    if p1move == p2move:
        print("Tie game")
    elif (p1move == "rock" and p2move == "scissors") or (p1move == "paper" and p2move == "rock") or (p1move == "scissors" and p2move == "paper"):
        print("Player 1 wins")
    else: 
        print("Player 2 wins")


gameloop = True

while gameloop == True:
    p1 = get_move()
    p2 = get_move()

    check_game(p1, p2)

    playAgain = input("Woud you like to play again? ").lower()
    if 'n' in playAgain:
        gameloop = False