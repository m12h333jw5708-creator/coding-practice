import random
while True:
    player_choice = input("Rock, Paper, Scissors:")
    computer_choice = random.choice(["Scissors", "Rock", "Paper"])
    if player_choice == computer_choice:
        print(f"c:{computer_choice}, player:{player_choice}, a tie")
    elif player_choice == "Scissors" and computer_choice == "Paper" or player_choice == "Paper" and computer_choice == "Rock" or player_choice == "Rock" and computer_choice == "Scissors":
        print(f"computer:{computer_choice}, player:{player_choice}, player win")
    elif player_choice == "Paper" and computer_choice == "Scissors" or player_choice == "Scissors" and computer_choice == "Rock" or player_choice == "Rock" and computer_choice == "Paper":
        print(f"computer:{computer_choice}, player:{player_choice}, computer win")
    a = input("Would you like to go on? Y/N").upper()
    if a == "Y":
        continue
    if a == "N":
        break
    else :
        break