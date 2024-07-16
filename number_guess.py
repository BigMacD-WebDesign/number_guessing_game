# from modules.art import logo
from random import randint

answer = randint(1, 100)

is_playing = False
EASY_LIVES = 5
DIFFICULT_LIFE = 10

def select_difficulty():
    difficulty = input("Please select difficulty. Type 'Hard' or 'Easy'\n").lower()
    if difficulty == "Hard":
        DIFFICULT_LIFE
        print(f"You have {DIFFICULT_LIFE} attempts.")
    else:
        EASY_LIVES
        print(f"You have {EASY_LIVES} attempts.")

select_difficulty()