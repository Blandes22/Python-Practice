#rock paper scissors game

def get_move():
    return input("Please enter you hand (rock, paper, or scissors): ").lower()

gameloop = True

while gameloop == True:
    p1move = get_move()
    p2move = get_move()

    if p1move == p2move:
        print("Tie game")
    elif (p1move == "rock" and p2move == "scissors") or (p1move == "paper" and p2move == "rock") or (p1move == "scissors" and p2move == "paper"):
        print("Player 1 wins")
    else: 
        print("Player 2 wins")

    playAgain = input("Woud you like to play again? ").lower()
    if 'y' in playAgain:
        gameloop = True
    else:
        gameloop = False