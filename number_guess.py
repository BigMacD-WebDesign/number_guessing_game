from modules.art import logo
import random

print(logo)
print("Welcome to GUESS THAT NUMBER!")

def computer_number():
    """Computer creates a random number between 1 and 100"""
    choice = random.randint(1, 100)
    return choice

computers_number = computer_number()
print(f"Psst, the correct answer is {computers_number}")

is_playing = False

difficulty = input("Please select difficulty. Type 'Hard' or 'Easy'\n").lower() 
if difficulty == "hard":
    player_lives = 5
    print(f"You have {player_lives} lives.")
elif difficulty == "easy":
    player_lives = 10
    print(f"You have {player_lives} lives.")


while not is_playing:
    player_guess = int(input("Please guess a number between 1 and 100: "))
    if player_guess > 100:
        print("Please select a number between 1 - 100.")   
    if player_guess >  computers_number:
       player_lives -= 1
       print(f"Too high. You have {player_lives} lives remaining.")
    elif player_guess < computers_number:
       player_lives -= 1
       print(f"Too low. You have {player_lives} lives remaining.")
       
    if player_lives == 0:
        print(f"Sorry you lose. You ran out of lives. The number was {computers_number}")
        is_playing = True   
    elif player_guess == computers_number:
        print(f"You win. The number is {computers_number}")
        is_playing = True       