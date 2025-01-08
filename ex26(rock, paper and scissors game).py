import random

options = ("rock", "paper", "scissors")
player = None
score = []

while True:
    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors): ")
    if computer == player:
        print("Draw, repeat the choice please")
    elif computer == "paper" and player == "rock":
        print("You loose")
    elif computer == "rock" and player == "scissors":
        print("You loose")
    elif computer == "scissors" and player == "paper":
        print("You loose")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    
    