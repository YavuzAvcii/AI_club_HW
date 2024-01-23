import random

choices = ["Rock", "Paper", "Scissors"]

player_choice = int(input("0 for rock, 1 for paper, 2 for scissors \n "))

comp_choice = random.randint(0, 2)

if (player_choice == 0 and comp_choice == 2):
  print(f"Computer: {choices[comp_choice]}")
  print(f"User: {choices[player_choice]}")
  print("You won")
elif (comp_choice == 0 and player_choice == 2):
  print(f"Computer: {choices[comp_choice]}")
  print(f"User: {choices[player_choice]}")
  print("You lost!")
elif (player_choice > comp_choice):
  print(f"Computer: {choices[comp_choice]}")
  print(f"User: {choices[player_choice]}")
  print("You won!!")
elif (player_choice < comp_choice):
  print(f"Computer: {choices[comp_choice]}")
  print(f"User: {choices[player_choice]}")
  print("You lost!!")
elif (player_choice == comp_choice):
  print(f"Computer: {choices[comp_choice]}")
  print(f"User: {choices[player_choice]}")
  print("It is a draw")
else:
  print("Invalid number")