#Guessing Game.........

import random

# Generates a random number from 1 to 10 
number = random.randint(1,10)
print("______________Welcome to Guessing game_____________")
player_name = input("What's your name? ").strip()

print("Hello {}!".format(player_name),"I am guessing a number between 1 and 10")
print("  Try to guess....   ")

#resticting number of guesses to 3
#checking whether num_guess is equal,greater or less than the number 

for i in range(1,4):
    num_guess = int(input())
    if num_guess<number:
        print("Your guess is too low...........")
    if num_guess>number:
        print("Your guess is too high..........")
    if num_guess == number:
        break

if num_guess==number:
    print("Correct Guess,You guessed in {} number of tries.....".format(i))
else:
    print("You lose the game")
    print("Wrong guess,The correct number was {}".format(number))
    
    
    
    
    
    
    