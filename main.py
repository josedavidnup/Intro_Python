import random

options = ("Rock", "Paper", "Scissors")

user_option = input("Rock, paper or scissors: ")
user_option = user_option.capitalize()
if user_option in options:
  computer_option = random.choice(options)
  print(f"User option {user_option}")
  print(f"The computer option {computer_option}")

  if user_option == computer_option:
    print("It's a tie")
  elif user_option == "Rock":
    if computer_option == "Scissors":
      print("Rock wins to scissors")
      print("You wins ;)")
    else:
      print("Paper wins to rock")
      print("You lose :(")
  elif user_option == "Paper":
    if computer_option == "Rock":
      print("Paper wins to rock")
      print("You wins ;)")
    else:
      print("Scissors wins to Paper")
      print("You lose :(")
  elif user_option == "Scissors":
    if computer_option == "Paper":
      print("Scissors wins to paper")
      print("You wins ;)")
    else:
      print("Rock wins to scissors")
      print("You lose :(")
else:
  print('Option not valid')
