#guess a number from 1-9 and the system will tell you if you need to guess higher or lower until you get it right

from random import randint

gameloop = True
guess = 0
num_of_guesses = 0
correct_guesses = 0

while gameloop == True:
    n = randint(1,9)
    
    while guess != n:
        guess = int(input("Please guess the number from 1 to 9: "))
        num_of_guesses += 1
        if guess == n:
            print("You guessed the number correctly!")
            correct_guesses += 1
            break
        elif guess > n:
            print("Lower.")
        else: 
            print("Higher.")
    
    s = input("Would you like to play again?").lower()
    if 'y' not in s:
        gameloop = False
        percentage = (str(round(correct_guesses/num_of_guesses * 100, 2)) + '%')

print("You made {} guesses and {} of them were correct.\nYou guessed correctly {} of the time!".format(num_of_guesses, correct_guesses, percentage))