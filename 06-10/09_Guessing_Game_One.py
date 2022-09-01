#guess a number from 1-9 and the system will tell you if you need to guess higher or lower until you get it right

from random import randint

gameloop = True
guess = 0
num_of_guesses = 0
correct_guesses = 0

#will loop the game until user no longer wishes to play
while gameloop == True:
    n = randint(1,9)
    
    while guess != n:
        guess = int(input("Please guess the number from 1 to 9: "))
        num_of_guesses += 1
        
        if guess == n:
            print("You guessed the number correctly!")
            correct_guesses += 1
        elif guess > n:
            print("Lower.")
        else: 
            print("Higher.")
    
    s = input("Would you like to play again?").lower() # .lower() used to avoid having to do multiple check ('n' and 'N')
    if 'n' in s:
        gameloop = False
        percentage = (str(round(correct_guesses/num_of_guesses * 100, 2)) + '%') 

print(f"You made {num_of_guesses} guesses and {correct_guesses} of them were correct.\nYou guessed correctly {percentage} of the time!")